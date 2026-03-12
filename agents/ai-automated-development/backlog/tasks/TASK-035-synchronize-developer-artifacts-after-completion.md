# TASK-035 Synchronize developer artifacts after task completion

## Status
todo

## Priority
high

## Objective
Ensure the developer handoff and implementation artifacts reflect the final completed task state and pushed commit metadata, so reviewer and tester do not see stale developer artifacts immediately after a successful developer run.

## Scope
- Update `scripts/run_developer.py` so successful `--execute` runs regenerate the developer handoff and implementation artifact from the final task content after status transitions are complete.
- Keep the developer artifact paths target-scoped under `agents/<target-name>/handoff/developer/` and `agents/<target-name>/implementation/developer/`.
- Eliminate false stale-artifact signals caused only by the task status moving from `in-progress` to `done` or by the pushed commit hash being added after the initial artifact write.
- Adjust `scripts/run_reviewer.py` only if needed so its stale-artifact detection is based on meaningful divergence, not just expected final completion metadata.

## Out of Scope
- Changing the overall backlog task model.
- Reworking reviewer decision policy beyond stale-artifact handling.
- Broad documentation updates unrelated to developer artifact synchronization.

## Implementation Notes
- Exact existing files that should change:
  - `scripts/run_developer.py`
  - `scripts/run_reviewer.py` only if required
- Preserve the existing target-scoped artifact helpers in `scripts/shared/artifact_paths.py`.
- Keep the developer completion path compatible with the existing reviewer and tester entry points.

## Acceptance Criteria
- After a successful developer execution, the latest developer handoff includes the final pushed commit hash and the final completed task status context instead of a stale pre-push snapshot.
- After a successful developer execution, the latest implementation artifact is synchronized with the final selected task content closely enough that `python scripts/run_reviewer.py --repo . --dry-run` does not flag it as stale solely because the task status changed to `done` or the pushed commit hash was added.
- `python -m py_compile scripts/run_developer.py scripts/run_reviewer.py` succeeds after the change.

## Dependencies
None

## Notes
Generated from a manual workflow audit after reviewer dry-runs continued to report stale implementation artifacts immediately after successful developer completion.
Grounding:
- Reviewer dry-runs on recent completed tasks still report that the implementation artifact appears stale relative to the task file.
- The current developer flow writes implementation artifacts before completion, then updates task state and handoff metadata later in the execution path.
