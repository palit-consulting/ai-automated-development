# Developer Implementation Prompt

## Date
2026-03-12

## Selected Task
- Code: `TASK-029`
- File: `agents/ai-automated-development/backlog/tasks/TASK-029-use-ai-planner-for-mvp-gap-evaluation.md`
- Goal: Replace the current heuristic-only empty-backlog planner fallback with an AI-backed planning step that evaluates remaining MVP gaps for the active target repository and generates one grounded next task.

## Implementation Objective
Replace the current heuristic-only empty-backlog planner fallback with an AI-backed planning step that evaluates remaining MVP gaps for the active target repository and generates one grounded next task.

## Exact Files Likely To Change
- `agents/ai-automated-development/backlog/tasks/TASK-029-use-ai-planner-for-mvp-gap-evaluation.md`
- `scripts/run_planner.py`
- `run_llm_planner(...)`
- `docs/mvp.md`
- `scripts/run_analyst.py`

## Exact Constraints
- Implement exactly one approved backlog task in a focused change set.
- Keep changes scoped to the selected task `agents/ai-automated-development/backlog/tasks/TASK-029-use-ai-planner-for-mvp-gap-evaluation.md`.
- Avoid unrelated refactors.
- Update task status from `todo` to `in-progress` before implementation and to `done` only after verification.
- If blocked, set the task status to `blocked` and explain why.
- Out of scope: Replacing deterministic selection when an eligible backlog task already exists
- Out of scope: Docs-only updates without planner code changes
- Out of scope: Task-artifact-only updates (`agents/.../backlog`, `agents/.../handoff`, `agents/.../implementation`) with no planner implementation
- Out of scope: Changing only this task file, generated implementation prompts, or developer handoff files
- Out of scope: Broad redesign of the analyst, developer, reviewer, or tester phases
- Out of scope: Multi-task planning or autonomous execution beyond generating one next task

## Exact Acceptance Criteria
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

## Step-by-Step Implementation Plan
1. Review `agents/ai-automated-development/backlog/tasks/TASK-029-use-ai-planner-for-mvp-gap-evaluation.md` and confirm the task is still in scope.
2. Update `agents/ai-automated-development/backlog/tasks/TASK-029-use-ai-planner-for-mvp-gap-evaluation.md` status from `todo` to `in-progress` before making changes.
3. Apply the required repository changes in `scripts/run_planner.py`, `run_llm_planner(...)`, `docs/mvp.md`, `scripts/run_analyst.py`.
4. Run the smallest relevant verification commands for the changed files.
5. Update `agents/ai-automated-development/backlog/tasks/TASK-029-use-ai-planner-for-mvp-gap-evaluation.md` to `done` only after the acceptance criteria are met.
6. Prepare a concise developer completion report for the reviewer with changed files, assumptions, and verification results.

## Copy-Paste Prompt For The Coding Agent
````text
# Developer Agent Prompt

You are the **Developer Agent**.

## Mission

Implement exactly one approved backlog task in a focused change set.

## Required Inputs

- Selected task file in `agents/backlog/tasks/`
- Repository context and relevant docs
- `AGENTS.md`
- `docs/agent-workflow.md`
- `docs/agent-handoff-contract.md`

## Execution Rules

1. Confirm the selected task is approved and currently `todo`.
2. Set task status to `in-progress` before implementation.
3. Implement only in-scope changes required by the task.
4. Keep unrelated refactors out of scope.
5. Run relevant checks.
6. After acceptance criteria are met, create a small focused commit for the task changes and push that commit to the active branch.
7. Include the pushed commit hash in the developer handoff so the reviewer can review the exact committed state.
8. Set task status to `done` after acceptance criteria are met and the handoff is ready for review.

If blocked, set status to `blocked` and explain why.

## Required Output Format

Use the handoff contract sections:

- Context
- Decisions
- Artifacts
- Open Questions / Risks
- Recommended Next Step

Include changed files, assumptions, verification commands, and the pushed commit hash in `Artifacts`.

## Done Criteria

- Acceptance criteria satisfied
- Relevant verification completed
- Task changes committed and pushed
- Status updated (`in-progress` → `done`)
- Output ready for Reviewer

Repository path: `/home/sp/workspace/github/ai-automated-development`
Goal: Replace the current heuristic-only empty-backlog planner fallback with an AI-backed planning step that evaluates remaining MVP gaps for the active target repository and generates one grounded next task.
Selected task file: `agents/ai-automated-development/backlog/tasks/TASK-029-use-ai-planner-for-mvp-gap-evaluation.md`

Files likely to change:
- `agents/ai-automated-development/backlog/tasks/TASK-029-use-ai-planner-for-mvp-gap-evaluation.md`
- `scripts/run_planner.py`
- `run_llm_planner(...)`
- `docs/mvp.md`
- `scripts/run_analyst.py`

Constraints:
- Implement exactly one approved backlog task in a focused change set.
- Keep changes scoped to the selected task `agents/ai-automated-development/backlog/tasks/TASK-029-use-ai-planner-for-mvp-gap-evaluation.md`.
- Avoid unrelated refactors.
- Update task status from `todo` to `in-progress` before implementation and to `done` only after verification.
- If blocked, set the task status to `blocked` and explain why.
- Out of scope: Replacing deterministic selection when an eligible backlog task already exists
- Out of scope: Docs-only updates without planner code changes
- Out of scope: Task-artifact-only updates (`agents/.../backlog`, `agents/.../handoff`, `agents/.../implementation`) with no planner implementation
- Out of scope: Changing only this task file, generated implementation prompts, or developer handoff files
- Out of scope: Broad redesign of the analyst, developer, reviewer, or tester phases
- Out of scope: Multi-task planning or autonomous execution beyond generating one next task

Acceptance criteria:
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

Implementation plan:
1. Review `agents/ai-automated-development/backlog/tasks/TASK-029-use-ai-planner-for-mvp-gap-evaluation.md` and confirm the task is still in scope.
2. Update `agents/ai-automated-development/backlog/tasks/TASK-029-use-ai-planner-for-mvp-gap-evaluation.md` status from `todo` to `in-progress` before making changes.
3. Apply the required repository changes in `scripts/run_planner.py`, `run_llm_planner(...)`, `docs/mvp.md`, `scripts/run_analyst.py`.
4. Run the smallest relevant verification commands for the changed files.
5. Update `agents/ai-automated-development/backlog/tasks/TASK-029-use-ai-planner-for-mvp-gap-evaluation.md` to `done` only after the acceptance criteria are met.
6. Prepare a concise developer completion report for the reviewer with changed files, assumptions, and verification results.

Selected task content:
```md
# TASK-029 Use AI planner for MVP gap evaluation

## Status
todo

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

```

````
