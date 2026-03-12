# Developer Implementation Prompt

## Date
2026-03-12

## Selected Task
- Code: `TASK-030`
- File: `agents/ai-automated-development/backlog/tasks/TASK-030-ai-auto-mvp-loop-stop-artifact.md`
- Goal: Implement a state-aware orchestrator mode that can continue running eligible analyst/planner/developer/reviewer cycles automatically while the target repository state is `MVP`, and writes a visible artifact when the loop stops because no grounded next task exists, policy changes phase behavior, or another stop condition is hit.

## Implementation Objective
Implement a state-aware orchestrator mode that can continue running eligible analyst/planner/developer/reviewer cycles automatically while the target repository state is `MVP`, and writes a visible artifact when the loop stops because no grounded next task exists, policy changes phase behavior, or another stop condition is hit.

## Exact Files Likely To Change
- `agents/ai-automated-development/backlog/tasks/TASK-030-ai-auto-mvp-loop-stop-artifact.md`
- `scripts/run_cycle.py`

## Exact Constraints
- Implement exactly one approved backlog task in a focused change set.
- Keep changes scoped to the selected task `agents/ai-automated-development/backlog/tasks/TASK-030-ai-auto-mvp-loop-stop-artifact.md`.
- Avoid unrelated refactors.
- Update task status from `todo` to `in-progress` before implementation and to `done` only after verification.
- If blocked, set the task status to `blocked` and explain why.
- Out of scope: Implementing distributed scheduling, cron, or background workers.
- Out of scope: Adding notifications, observability dashboards, or non-MVP state policies beyond what is needed to make the local `MVP` loop continue/stop correctly.

## Exact Acceptance Criteria
- A runner invocation can execute repeated cycles automatically while the resolved target repository state is `MVP`, stopping only when a defined stop condition is reached or no further eligible/grounded task exists.
- When the loop stops, a target-scoped artifact is written that records the stop reason in a human-visible form, including at least the no-grounded-next-task path.
- Continuation/stop artifacts are grounded in actual phase results from this repository's existing planner/developer/reviewer/tester flow rather than placeholder text.
- Existing single-cycle usage remains available, and non-`MVP` states still apply their current safety restrictions instead of forcing autonomous continuation.

## Step-by-Step Implementation Plan
1. Review `agents/ai-automated-development/backlog/tasks/TASK-030-ai-auto-mvp-loop-stop-artifact.md` and confirm the task is still in scope.
2. Update `agents/ai-automated-development/backlog/tasks/TASK-030-ai-auto-mvp-loop-stop-artifact.md` status from `todo` to `in-progress` before making changes.
3. Apply the required repository changes in `scripts/run_cycle.py`.
4. Run the smallest relevant verification commands for the changed files.
5. Update `agents/ai-automated-development/backlog/tasks/TASK-030-ai-auto-mvp-loop-stop-artifact.md` to `done` only after the acceptance criteria are met.
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
Goal: Implement a state-aware orchestrator mode that can continue running eligible analyst/planner/developer/reviewer cycles automatically while the target repository state is `MVP`, and writes a visible artifact when the loop stops because no grounded next task exists, policy changes phase behavior, or another stop condition is hit.
Selected task file: `agents/ai-automated-development/backlog/tasks/TASK-030-ai-auto-mvp-loop-stop-artifact.md`

Files likely to change:
- `agents/ai-automated-development/backlog/tasks/TASK-030-ai-auto-mvp-loop-stop-artifact.md`
- `scripts/run_cycle.py`

Constraints:
- Implement exactly one approved backlog task in a focused change set.
- Keep changes scoped to the selected task `agents/ai-automated-development/backlog/tasks/TASK-030-ai-auto-mvp-loop-stop-artifact.md`.
- Avoid unrelated refactors.
- Update task status from `todo` to `in-progress` before implementation and to `done` only after verification.
- If blocked, set the task status to `blocked` and explain why.
- Out of scope: Implementing distributed scheduling, cron, or background workers.
- Out of scope: Adding notifications, observability dashboards, or non-MVP state policies beyond what is needed to make the local `MVP` loop continue/stop correctly.

Acceptance criteria:
- A runner invocation can execute repeated cycles automatically while the resolved target repository state is `MVP`, stopping only when a defined stop condition is reached or no further eligible/grounded task exists.
- When the loop stops, a target-scoped artifact is written that records the stop reason in a human-visible form, including at least the no-grounded-next-task path.
- Continuation/stop artifacts are grounded in actual phase results from this repository's existing planner/developer/reviewer/tester flow rather than placeholder text.
- Existing single-cycle usage remains available, and non-`MVP` states still apply their current safety restrictions instead of forcing autonomous continuation.

Implementation plan:
1. Review `agents/ai-automated-development/backlog/tasks/TASK-030-ai-auto-mvp-loop-stop-artifact.md` and confirm the task is still in scope.
2. Update `agents/ai-automated-development/backlog/tasks/TASK-030-ai-auto-mvp-loop-stop-artifact.md` status from `todo` to `in-progress` before making changes.
3. Apply the required repository changes in `scripts/run_cycle.py`.
4. Run the smallest relevant verification commands for the changed files.
5. Update `agents/ai-automated-development/backlog/tasks/TASK-030-ai-auto-mvp-loop-stop-artifact.md` to `done` only after the acceptance criteria are met.
6. Prepare a concise developer completion report for the reviewer with changed files, assumptions, and verification results.

Selected task content:
```md
# TASK-030 Add MVP auto-continue orchestrator loop with visible stop artifact

## Status
todo

## Priority
high

## Objective
Implement a state-aware orchestrator mode that can continue running eligible analyst/planner/developer/reviewer cycles automatically while the target repository state is `MVP`, and writes a visible artifact when the loop stops because no grounded next task exists, policy changes phase behavior, or another stop condition is hit.

## Scope
- Extend the local runner/orchestrator path in `scripts/run_cycle.py` (and any small supporting helpers) with an explicit auto-continue loop mode for `MVP` state instead of a single pass only.
- Persist per-cycle continuation/stop decisions as target-scoped artifacts so humans and later agents can see why the loop continued or stopped, including the no-grounded-next-task case required by the MVP.

## Out of Scope
- Implementing distributed scheduling, cron, or background workers.
- Adding notifications, observability dashboards, or non-MVP state policies beyond what is needed to make the local `MVP` loop continue/stop correctly.

## Acceptance Criteria
- A runner invocation can execute repeated cycles automatically while the resolved target repository state is `MVP`, stopping only when a defined stop condition is reached or no further eligible/grounded task exists.
- When the loop stops, a target-scoped artifact is written that records the stop reason in a human-visible form, including at least the no-grounded-next-task path.
- Continuation/stop artifacts are grounded in actual phase results from this repository's existing planner/developer/reviewer/tester flow rather than placeholder text.
- Existing single-cycle usage remains available, and non-`MVP` states still apply their current safety restrictions instead of forcing autonomous continuation.

## Dependencies
- None

## Notes
Generated by `scripts/run_planner.py` because the backlog was exhausted during an AI-backed MVP gap evaluation.
Grounding:
- `docs/mvp.md` requires 'automatic continuation while the target repository state is `MVP`' and says stop reasons must be written as a visible artifact for human follow-up.
- Current `scripts/run_cycle.py` is a thin orchestrator that runs through a selected phase once and applies some state-based phase adjustments, but the provided evidence does not show an autonomous repeat-until-stop loop or a dedicated stop-reason artifact.
- The analysis artifact explicitly flags future phase integration points as still needed and recommends planner evaluation of remaining MVP gaps when backlog work is exhausted, which aligns with implementing loop continuation and clean stopping behavior.
Slug: `ai-auto-mvp-loop-stop-artifact`

```

````
