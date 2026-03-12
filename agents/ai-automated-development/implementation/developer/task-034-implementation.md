# Developer Implementation Prompt

## Date
2026-03-13

## Selected Task
- Code: `TASK-034`
- File: `agents/ai-automated-development/backlog/tasks/TASK-034-align-running-guide-with-target-scoped-workflow.md`
- Goal: Advance the next missing MVP item from docs/mvp.md using the next eligible backlog task.

## Implementation Objective
Update the main running guide so it matches the current target-scoped artifact layout, reviewer/tester paths, and MVP auto-continue behavior, reducing operator confusion and keeping the documented workflow aligned with the actual runner.

## Exact Files Likely To Change
- `agents/ai-automated-development/backlog/tasks/TASK-034-align-running-guide-with-target-scoped-workflow.md`
- `docs/running-the-system.md`
- `scripts/shared/artifact_paths.py`
- `run-agents.sh`

## Exact Constraints
- Implement exactly one approved backlog task in a focused change set.
- Keep changes scoped to the selected task `agents/ai-automated-development/backlog/tasks/TASK-034-align-running-guide-with-target-scoped-workflow.md`.
- Avoid unrelated refactors.
- Update task status from `todo` to `in-progress` before implementation and to `done` only after verification.
- If blocked, set the task status to `blocked` and explain why.
- Out of scope: Changing runner code in `scripts/`.
- Out of scope: Redesigning the workflow or artifact model.
- Out of scope: Broad documentation cleanup beyond the main running guide and one directly necessary consistency fix if required.

## Exact Acceptance Criteria
- `docs/running-the-system.md` no longer references stale paths like `agents/handoff/...`, `agents/implementation/...`, `agents/review/...`, or `agents/test/...` without the active target name segment.
- The guide describes the current wrapper behavior for `./run-agents.sh`, `./run-agents.sh --dry-run`, and the distinction between supervised runs and `MVP` auto-continue.
- Reviewer and tester output examples in the guide match the current target-scoped artifact paths and terminology.
- `rg -n "agents/(handoff|implementation|review|test)/" docs/running-the-system.md` returns no matches.

## Step-by-Step Implementation Plan
1. Review `agents/ai-automated-development/backlog/tasks/TASK-034-align-running-guide-with-target-scoped-workflow.md` and confirm the task is still in scope.
2. Update `agents/ai-automated-development/backlog/tasks/TASK-034-align-running-guide-with-target-scoped-workflow.md` status from `todo` to `in-progress` before making changes.
3. Apply the required repository changes in `docs/running-the-system.md`, `scripts/shared/artifact_paths.py`, `run-agents.sh`.
4. Run the smallest relevant verification commands for the changed files.
5. Update `agents/ai-automated-development/backlog/tasks/TASK-034-align-running-guide-with-target-scoped-workflow.md` to `done` only after the acceptance criteria are met.
6. Prepare a concise developer completion report for the reviewer with changed files, assumptions, and verification results.

## Copy-Paste Prompt For The Coding Agent
````text
# Developer Agent Prompt

You are the **Developer Agent**.

## Mission

Implement exactly one approved backlog task in a focused change set.

## Required Inputs

- Selected task file in `agents/<target-name>/backlog/tasks/`
- Repository context and relevant docs
- `AGENTS.md`
- `docs/agent-workflow.md`
- `docs/agent-handoff-contract.md`

## Execution Rules

1. Confirm the selected task is approved and currently `todo`.
2. Set task status to `in-progress` before implementation.
3. Implement only in-scope changes required by the task.
4. Keep unrelated refactors out of scope.
5. Run the task-appropriate verification commands and record their outcomes.
6. After acceptance criteria are met, create a small focused commit for the task changes and push that commit to the active branch.
7. Include the pushed commit hash in the developer handoff so the reviewer can review the exact committed state.
8. Set task status to `done` after acceptance criteria are met and the handoff is ready for review.

If blocked, set status to `blocked` and explain why.

Do not treat task-file-only edits, prompt-only edits, or handoff-only churn as task completion.
Do not mark the task `done` if the intended implementation files were not changed or required verification did not pass.

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
- Developer handoff includes changed files, verification evidence, and pushed commit hash

Repository path: `/home/sp/workspace/github/ai-automated-development`
Goal: Advance the next missing MVP item from docs/mvp.md using the next eligible backlog task.
Selected task file: `agents/ai-automated-development/backlog/tasks/TASK-034-align-running-guide-with-target-scoped-workflow.md`

Files likely to change:
- `agents/ai-automated-development/backlog/tasks/TASK-034-align-running-guide-with-target-scoped-workflow.md`
- `docs/running-the-system.md`
- `scripts/shared/artifact_paths.py`
- `run-agents.sh`

Constraints:
- Implement exactly one approved backlog task in a focused change set.
- Keep changes scoped to the selected task `agents/ai-automated-development/backlog/tasks/TASK-034-align-running-guide-with-target-scoped-workflow.md`.
- Avoid unrelated refactors.
- Update task status from `todo` to `in-progress` before implementation and to `done` only after verification.
- If blocked, set the task status to `blocked` and explain why.
- Out of scope: Changing runner code in `scripts/`.
- Out of scope: Redesigning the workflow or artifact model.
- Out of scope: Broad documentation cleanup beyond the main running guide and one directly necessary consistency fix if required.

Acceptance criteria:
- `docs/running-the-system.md` no longer references stale paths like `agents/handoff/...`, `agents/implementation/...`, `agents/review/...`, or `agents/test/...` without the active target name segment.
- The guide describes the current wrapper behavior for `./run-agents.sh`, `./run-agents.sh --dry-run`, and the distinction between supervised runs and `MVP` auto-continue.
- Reviewer and tester output examples in the guide match the current target-scoped artifact paths and terminology.
- `rg -n "agents/(handoff|implementation|review|test)/" docs/running-the-system.md` returns no matches.

Implementation plan:
1. Review `agents/ai-automated-development/backlog/tasks/TASK-034-align-running-guide-with-target-scoped-workflow.md` and confirm the task is still in scope.
2. Update `agents/ai-automated-development/backlog/tasks/TASK-034-align-running-guide-with-target-scoped-workflow.md` status from `todo` to `in-progress` before making changes.
3. Apply the required repository changes in `docs/running-the-system.md`, `scripts/shared/artifact_paths.py`, `run-agents.sh`.
4. Run the smallest relevant verification commands for the changed files.
5. Update `agents/ai-automated-development/backlog/tasks/TASK-034-align-running-guide-with-target-scoped-workflow.md` to `done` only after the acceptance criteria are met.
6. Prepare a concise developer completion report for the reviewer with changed files, assumptions, and verification results.

Selected task content:
```md
# TASK-034 Align running guide with target-scoped workflow

## Status
todo

## Priority
medium

## Objective
Update the main running guide so it matches the current target-scoped artifact layout, reviewer/tester paths, and MVP auto-continue behavior, reducing operator confusion and keeping the documented workflow aligned with the actual runner.

## Scope
- Update `docs/running-the-system.md` to use the current target-scoped artifact paths under `agents/<target-name>/...`.
- Correct stale developer, reviewer, and tester artifact references so they match the current helpers in `scripts/shared/artifact_paths.py`.
- Align the running guide with the current runner behavior for `./run-agents.sh`, `--dry-run`, `--execute`, and `MVP` auto-continue wording.
- Keep the change documentation-focused and limited to the main running guide unless one directly linked line in another doc must be adjusted for consistency.

## Out of Scope
- Changing runner code in `scripts/`.
- Redesigning the workflow or artifact model.
- Broad documentation cleanup beyond the main running guide and one directly necessary consistency fix if required.

## Implementation Notes
- Exact existing file that should change:
  - `docs/running-the-system.md`
- Use the current target-scoped artifact model as the source of truth:
  - `agents/<target-name>/analysis/`
  - `agents/<target-name>/backlog/tasks/`
  - `agents/<target-name>/handoff/developer/`
  - `agents/<target-name>/implementation/developer/`
  - `agents/<target-name>/review/reviewer/`
  - `agents/<target-name>/test/`
  - `agents/<target-name>/orchestrator/stop-reasons/`

## Acceptance Criteria
- `docs/running-the-system.md` no longer references stale paths like `agents/handoff/...`, `agents/implementation/...`, `agents/review/...`, or `agents/test/...` without the active target name segment.
- The guide describes the current wrapper behavior for `./run-agents.sh`, `./run-agents.sh --dry-run`, and the distinction between supervised runs and `MVP` auto-continue.
- Reviewer and tester output examples in the guide match the current target-scoped artifact paths and terminology.
- `rg -n "agents/(handoff|implementation|review|test)/" docs/running-the-system.md` returns no matches.

## Dependencies
None

## Notes
Generated from a manual MVP gap audit after the planner stopped cleanly without deriving another grounded task.
Grounding:
- `docs/mvp-readiness-checklist.md` still marks docs/scripts alignment to the target-scoped artifact model and state-aware auto-continue behavior as partial.
- `docs/running-the-system.md` still contains stale artifact paths and older supervised-flow wording that no longer matches the current runner and target-scoped artifact helpers.

```

````
