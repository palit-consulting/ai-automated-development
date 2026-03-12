# Developer Handoff

## Goal
Advance the next missing MVP item from docs/mvp.md using the next eligible backlog task.

## Date
2026-03-13

## Repository Path
`/home/sp/workspace/github/ai-automated-development`

## Selected Task Code
`TASK-036`

## Source Task File Path
`agents/ai-automated-development/backlog/tasks/TASK-036-include-review-artifacts-in-pushed-task-state.md`

## Objective
Make the developer commit/push workflow produce a reviewable pushed task state that includes the final task status and any required developer artifacts, so reviewer inspection is grounded in a coherent pushed snapshot rather than a mix of pushed code and local-only artifacts.

## Required Inputs
- `agents/ai-automated-development/backlog/tasks/TASK-036-include-review-artifacts-in-pushed-task-state.md`
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
- Pushed commit hash for reviewer reference: `39aed5440de52db39c2a1d932b803adeba55d087`

## Commit Reference
- Pushed commit hash: `39aed5440de52db39c2a1d932b803adeba55d087`
- Reviewer should inspect the pushed commit referenced below, not only the local worktree.

## Full Task Content
```md
# TASK-036 Include review-relevant artifacts in pushed task state

## Status
done

## Priority
high

## Objective
Make the developer commit/push workflow produce a reviewable pushed task state that includes the final task status and any required developer artifacts, so reviewer inspection is grounded in a coherent pushed snapshot rather than a mix of pushed code and local-only artifacts.

## Scope
- Update `scripts/run_developer.py` commit ordering so the pushed commit contains the final task file plus the review-relevant developer artifacts needed for downstream review.
- If the pushed commit hash must appear inside a committed artifact, use a deterministic finalization strategy such as a second local rewrite plus amend/recommit before push.
- Keep the workflow focused on the existing MVP direct-to-main model and the current target-scoped artifact layout.
- Ensure the resulting pushed state stays consistent with reviewer consumption in `scripts/run_reviewer.py`.

## Out of Scope
- Switching to feature branches or pull requests.
- Changing analyst artifact handling.
- Reworking tester logic beyond consuming the consistent pushed/developer-review state.

## Implementation Notes
- Exact existing files that should change:
  - `scripts/run_developer.py`
  - `scripts/run_reviewer.py` only if needed for the updated artifact expectation
- The final design should avoid leaving the committed task state and the local developer handoff out of sync.
- Keep the commit history focused; do not introduce unrelated workflow refactors.

## Acceptance Criteria
- After a successful developer execution, the pushed commit contains the final task file marked `done` and the developer artifacts required for reviewer follow-up.
- Reviewer follow-up can inspect the pushed commit and find the expected task-completion artifacts in committed repository state rather than relying on a local-only handoff write after push.
- `python -m py_compile scripts/run_developer.py scripts/run_reviewer.py` succeeds after the change.

## Dependencies
None

## Notes
Generated from a manual workflow audit after the developer push flow was observed to write the final handoff after commit/push, leaving review-relevant artifacts outside the pushed task snapshot.
Grounding:
- `scripts/run_developer.py` currently creates the git commit before writing the final developer handoff, so the pushed commit and the latest local handoff can diverge.
- `docs/mvp.md` requires reviewer decisions to be grounded in the pushed task result and recorded developer verification evidence.

```
