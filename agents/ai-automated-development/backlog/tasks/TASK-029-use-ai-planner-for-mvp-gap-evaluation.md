# TASK-029 Use AI planner for MVP gap evaluation

## Status
done

## Priority
high

## Objective
Replace the current heuristic-only empty-backlog planner fallback with an AI-backed planning step that evaluates remaining MVP gaps for the active target repository and generates one grounded next task.

## Scope
- Implement the empty-backlog AI planning path in `scripts/run_planner.py`; this task is not complete unless that file changes materially
- Reuse or extend the existing `run_llm_planner(...)` path in `scripts/run_planner.py` instead of adding a docs-only workaround or a separate planning script
- Make the planner read the active target-scoped inputs from `docs/mvp.md` and `agents/<target-name>/analysis/repo-analysis.md`, then generate one grounded next task when the backlog is exhausted
- If needed, update `scripts/run_analyst.py` so the target-scoped analysis output gives the AI planner enough grounding to evaluate remaining MVP gaps
- Use the active target-scoped artifact paths under `agents/<target-name>/...` as planning inputs and output locations
- Require the AI-backed planner to generate at most one implementation-ready backlog task per run
- Prevent duplicate task generation by checking existing task slugs/objectives before writing a new task
- Keep the existing clean-stop behavior when the model cannot justify a grounded next task
- Update only the minimal supporting code needed for this path; keep deterministic task selection unchanged when an eligible backlog task already exists

## Out of Scope
- Replacing deterministic selection when an eligible backlog task already exists
- Docs-only updates without planner code changes
- Task-artifact-only updates (`agents/.../backlog`, `agents/.../handoff`, `agents/.../implementation`) with no planner implementation
- Changing only this task file, generated implementation prompts, or developer handoff files
- Broad redesign of the analyst, developer, reviewer, or tester phases
- Multi-task planning or autonomous execution beyond generating one next task

## Acceptance Criteria
- When the target-scoped backlog has no eligible task, the planner can invoke an AI-backed fallback instead of relying only on hardcoded gap detectors
- The AI-backed fallback is implemented in `scripts/run_planner.py` by changing executable planner code, not by changing only task wording or generated artifacts
- The AI-backed fallback uses `docs/mvp.md` plus `agents/<target-name>/analysis/repo-analysis.md` and current repository evidence to propose the next task
- The generated task is written to `agents/<target-name>/backlog/tasks/` and is limited to one focused, implementation-ready slice
- Existing completed or active tasks with the same slug/objective are not regenerated
- If the model cannot justify a grounded next task, the planner stops cleanly with an explanation instead of writing low-confidence backlog work
- `scripts/run_planner.py` is changed materially; task-file-only or artifact-only output does not satisfy this task
- Completion requires at least one substantive code change in `scripts/run_planner.py` and optionally `scripts/run_analyst.py`; changing only task metadata or generated prompts is insufficient
- Verification includes a dry-run command that demonstrates the AI-backed planning path for an exhausted backlog
- A valid implementation must change at least one of these files: `scripts/run_planner.py` or `scripts/run_analyst.py`; if neither file changes, the task is not done
- The generated task must still be grounded enough to avoid duplicate or obviously generic backlog entries

## Dependencies
- None

## Notes
Generated after confirming the current planner still stops once hardcoded MVP gap detectors are exhausted.
Grounding:
- `docs/mvp.md` requires repository-aware planning grounded in the current target codebase
- `agents/ai-automated-development/analysis/repo-analysis.md` still notes that planner output quality is heuristic in the current thin-slice
- Repository evidence: `scripts/run_planner.py` currently depends on a small set of hardcoded MVP gap detectors and cannot reliably decide whether MVP is complete
Slug: `use-ai-planner-for-mvp-gap-evaluation`
- Previous developer attempt changed only task artifacts and did not modify `scripts/run_planner.py`; that outcome must be treated as a failure, not as task completion.
- Developer should start from the existing planner implementation in `scripts/run_planner.py`, especially the current empty-backlog fallback and `run_llm_planner(...)`, instead of inventing a new parallel workflow.
