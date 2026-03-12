# Developer Handoff

## Goal
Replace the current heuristic-only empty-backlog planner fallback with an AI-backed planning step that evaluates remaining MVP gaps for the active target repository and generates one grounded next task.

## Date
2026-03-12

## Repository Path
`/home/sp/workspace/github/ai-automated-development`

## Selected Task Code
`TASK-029`

## Source Task File Path
`agents/ai-automated-development/backlog/tasks/TASK-029-use-ai-planner-for-mvp-gap-evaluation.md`

## Objective
Replace the current heuristic-only empty-backlog planner fallback with an AI-backed planning step that evaluates remaining MVP gaps for the active target repository and generates one grounded next task.

## Required Inputs
- `agents/ai-automated-development/backlog/tasks/TASK-029-use-ai-planner-for-mvp-gap-evaluation.md`
- `agents/ai-automated-development/analysis/repo-analysis.md`
- `AGENTS.md`
- `docs/agent-workflow.md`
- `docs/agent-handoff-contract.md`

## Implementation Rules
- Implement exactly one approved backlog task in a focused change set.
- Set the selected task status to `in-progress` before implementation.
- Implement only in-scope changes required by the task.
- Keep unrelated refactors out of scope.
- Run relevant checks before completion.
- Set task status to `done` when acceptance criteria are met, or `blocked` if work cannot proceed.

## Expected Output
- A small, working repository change set that implements the selected task.
- The selected backlog task updated through the required status transitions.
- A developer handoff/report aligned with `docs/agent-handoff-contract.md` and ready for reviewer follow-up.
- Pushed commit hash for reviewer reference: `c0d69f790ab7bed34baccc56c8fb63b3ffa3c049`

## Commit Reference
- Pushed commit hash: `c0d69f790ab7bed34baccc56c8fb63b3ffa3c049`
- Reviewer should inspect the pushed commit referenced below, not only the local worktree.

## Full Task Content
```md
# TASK-029 Use AI planner for MVP gap evaluation

## Status
done

## Priority
high

## Objective
Replace the current heuristic-only empty-backlog planner fallback with an AI-backed planning step that evaluates remaining MVP gaps for the active target repository and generates one grounded next task.

## Scope
- Update `scripts/run_planner.py` so the empty-backlog fallback can call the AI model to evaluate `docs/mvp.md`, the target-scoped analysis artifact, and the current repository state
- Use the active target-scoped artifact paths under `agents/<target-name>/...` as planning inputs and output locations
- Require the AI-backed planner to generate at most one implementation-ready backlog task per run
- Prevent duplicate task generation by checking existing task slugs/objectives before writing a new task
- Keep the existing clean-stop behavior when the model cannot justify a grounded next task

## Out of Scope
- Replacing deterministic selection when an eligible backlog task already exists
- Broad redesign of the analyst, developer, reviewer, or tester phases
- Multi-task planning or autonomous execution beyond generating one next task

## Acceptance Criteria
- When the target-scoped backlog has no eligible task, the planner can invoke an AI-backed fallback instead of relying only on hardcoded gap detectors
- The AI-backed fallback uses `docs/mvp.md` plus `agents/<target-name>/analysis/repo-analysis.md` and current repository evidence to propose the next task
- The generated task is written to `agents/<target-name>/backlog/tasks/` and is limited to one focused, implementation-ready slice
- Existing completed or active tasks with the same slug/objective are not regenerated
- If the model cannot justify a grounded next task, the planner stops cleanly with an explanation instead of writing low-confidence backlog work
- Verification includes a dry-run command that demonstrates the AI-backed planning path for an exhausted backlog

## Dependencies
- None

## Notes
Generated after confirming the current planner still stops once hardcoded MVP gap detectors are exhausted.
Grounding:
- `docs/mvp.md` requires repository-aware planning grounded in the current target codebase
- `agents/ai-automated-development/analysis/repo-analysis.md` still notes that planner output quality is heuristic in the current thin-slice
- Repository evidence: `scripts/run_planner.py` currently depends on a small set of hardcoded MVP gap detectors and cannot reliably decide whether MVP is complete
Slug: `use-ai-planner-for-mvp-gap-evaluation`

```
