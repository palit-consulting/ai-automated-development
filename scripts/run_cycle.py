#!/usr/bin/env python3
"""Thin-slice local CLI for the first multi-agent workflow phases.

Current phases:
1. analyst
2. planner

The script intentionally keeps all logic local and file-based so that later
phases (developer/reviewer/tester) can be added without changing the CLI shape.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path
from typing import Callable

PHASE_ORDER = ["analyst", "planner", "developer", "reviewer", "tester"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a thin-slice AI-dev cycle against this repository."
    )
    parser.add_argument(
        "goal",
        help="Human goal for this cycle (used by analyst and planner outputs).",
    )
    parser.add_argument(
        "--phase",
        choices=["analyst", "planner"],
        default="planner",
        help="Last phase to run. analyst runs analyst only; planner runs analyst+planner.",
    )
    parser.add_argument(
        "--repo",
        default=".",
        help="Target repository path. Defaults to current repository.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print outputs without writing files.",
    )
    return parser.parse_args()


def run_phase(phase: str, handlers: dict[str, Callable[[], None]]) -> None:
    handler = handlers.get(phase)
    if handler is None:
        raise ValueError(f"Phase '{phase}' is not implemented yet.")
    handler()


def collect_repo_snapshot(repo_root: Path) -> dict[str, object]:
    files = [p for p in repo_root.rglob("*") if p.is_file() and ".git" not in p.parts]
    top_level_dirs = sorted([p.name for p in repo_root.iterdir() if p.is_dir() and p.name != ".git"])

    def read_if_exists(path: str) -> str:
        candidate = repo_root / path
        return candidate.read_text(encoding="utf-8") if candidate.exists() else ""

    readme = read_if_exists("README.md")
    mvp = read_if_exists("docs/mvp.md")

    return {
        "file_count": len(files),
        "top_level_dirs": top_level_dirs,
        "has_backlog": (repo_root / "backlog/tasks").exists(),
        "has_prompts": (repo_root / "prompts/agents").exists(),
        "readme_preview": "\n".join(readme.splitlines()[:12]),
        "mvp_preview": "\n".join(mvp.splitlines()[:12]),
    }


def build_analysis_markdown(goal: str, repo_root: Path) -> str:
    snapshot = collect_repo_snapshot(repo_root)
    today = dt.date.today().isoformat()

    return f"""## Context
- Goal: {goal}
- Current step: Repository analysis
- Date: {today}
- Inputs reviewed:
  - README.md
  - docs/mvp.md
  - docs/agent-handoff-contract.md
  - Repository structure under {repo_root.resolve()}

## Decisions
- The repository is already structured for AI-assisted development and is suitable for a thin-slice runnable loop.
- A local CLI should keep outputs file-based to preserve human review and easy iteration.
- Analyst output should be regenerated each run to keep planning grounded in current state.

## Artifacts
- analysis/repo-analysis.md: This analysis snapshot.

## Open Questions / Risks
- Future phases (developer/reviewer/tester) still need integration points and output contracts.
- Planner output quality is heuristic in this thin-slice and should be reviewed by a human.

## Recommended Next Step
- Next agent: Planner
- Instruction: Convert analysis into small, dependency-safe backlog tasks.

---

## Repository Snapshot
- File count (excluding .git): {snapshot['file_count']}
- Top-level directories: {", ".join(snapshot['top_level_dirs'])}
- backlog/tasks present: {snapshot['has_backlog']}
- prompts/agents present: {snapshot['has_prompts']}

### README.md (preview)
```
{snapshot['readme_preview']}
```

### docs/mvp.md (preview)
```
{snapshot['mvp_preview']}
```
"""


def next_task_number(task_dir: Path) -> int:
    max_id = 0
    for path in task_dir.glob("TASK-*.md"):
        match = re.match(r"TASK-(\d{3})-", path.name)
        if match:
            max_id = max(max_id, int(match.group(1)))
    return max_id + 1


def slugify(value: str, max_words: int = 6) -> str:
    words = re.sub(r"[^a-zA-Z0-9\s-]", "", value.lower()).split()
    trimmed = words[:max_words] if words else ["planned-work"]
    return "-".join(trimmed)


def build_task_markdown(task_id: int, goal: str) -> str:
    task_code = f"TASK-{task_id:03d}"
    slug = slugify(goal)

    return f"""# {task_code} Planner Follow-up: {goal}

## Status
todo

## Priority
high

## Objective
Translate the latest analyst findings into concrete implementation work aligned with this goal: {goal}

## Scope
- Use `analysis/repo-analysis.md` as the planning input
- Define one focused implementation slice that can be completed in a single cycle
- Keep task boundaries explicit and implementation-ready

## Out of Scope
- Implementing the task itself
- Introducing unrelated refactors

## Acceptance Criteria
- Backlog task is specific and executable
- Acceptance criteria are testable
- Dependencies are explicitly listed

## Dependencies
- None

## Notes
Generated by `scripts/run_cycle.py` (planner phase).
Slug: `{slug}`
"""


def upsert_planner_task(repo_root: Path, goal: str, dry_run: bool) -> Path:
    task_dir = repo_root / "backlog" / "tasks"
    task_dir.mkdir(parents=True, exist_ok=True)

    marker = f"Planner Follow-up: {goal}"
    existing = None
    for path in sorted(task_dir.glob("TASK-*.md")):
        if marker in path.read_text(encoding="utf-8"):
            existing = path
            break

    if existing is None:
        task_id = next_task_number(task_dir)
        filename = f"TASK-{task_id:03d}-{slugify(goal)}.md"
        target = task_dir / filename
    else:
        task_id_match = re.match(r"TASK-(\d{3})-", existing.name)
        task_id = int(task_id_match.group(1)) if task_id_match else next_task_number(task_dir)
        target = existing

    content = build_task_markdown(task_id=task_id, goal=goal)

    if dry_run:
        print(f"[dry-run] Would write planner task: {target}")
        print(content)
    else:
        target.write_text(content, encoding="utf-8")

    return target


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo).resolve()

    analysis_path = repo_root / "analysis" / "repo-analysis.md"

    def analyst_handler() -> None:
        content = build_analysis_markdown(goal=args.goal, repo_root=repo_root)
        if args.dry_run:
            print(f"[dry-run] Would write analyst output: {analysis_path}")
            print(content)
            return

        analysis_path.parent.mkdir(parents=True, exist_ok=True)
        analysis_path.write_text(content, encoding="utf-8")
        print(f"Analyst output written: {analysis_path}")

    def planner_handler() -> None:
        if not analysis_path.exists() and not args.dry_run:
            raise FileNotFoundError(
                "Planner phase requires analysis/repo-analysis.md. Run analyst first."
            )
        task_path = upsert_planner_task(repo_root=repo_root, goal=args.goal, dry_run=args.dry_run)
        print(f"Planner task ready: {task_path}")

    handlers: dict[str, Callable[[], None]] = {
        "analyst": analyst_handler,
        "planner": planner_handler,
    }

    stop_idx = PHASE_ORDER.index(args.phase)
    for phase in PHASE_ORDER[: stop_idx + 1]:
        if phase in handlers:
            print(f"Running phase: {phase}")
            run_phase(phase, handlers)
        else:
            print(f"Skipping unimplemented phase: {phase}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
