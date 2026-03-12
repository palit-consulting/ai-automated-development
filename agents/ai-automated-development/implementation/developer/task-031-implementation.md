# Developer Implementation Prompt

## Date
2026-03-13

## Selected Task
- Code: `TASK-031`
- File: `agents/ai-automated-development/backlog/tasks/TASK-031-ai-auto-tester-stop-signal.md`
- Goal: Close the loop-control gap where `scripts/run_cycle.py` auto-continues through the tester phase without consuming a clear tester outcome. Implement deterministic tester outcome parsing and use it to continue only on explicit READY/continue-style results, while writing a visible stop reason artifact when the tester reports retry or blocked.

## Implementation Objective
Close the loop-control gap where `scripts/run_cycle.py` auto-continues through the tester phase without consuming a clear tester outcome. Implement deterministic tester outcome parsing and use it to continue only on explicit READY/continue-style results, while writing a visible stop reason artifact when the tester reports retry or blocked.

## Exact Files Likely To Change
- `agents/ai-automated-development/backlog/tasks/TASK-031-ai-auto-tester-stop-signal.md`
- `scripts/run_tester.py`
- `scripts/run_cycle.py`

## Exact Constraints
- Implement exactly one approved backlog task in a focused change set.
- Keep changes scoped to the selected task `agents/ai-automated-development/backlog/tasks/TASK-031-ai-auto-tester-stop-signal.md`.
- Avoid unrelated refactors.
- Update task status from `todo` to `in-progress` before implementation and to `done` only after verification.
- If blocked, set the task status to `blocked` and explain why.
- Out of scope: Changing reviewer or developer verification policy beyond what is needed for tester outcome consumption.
- Out of scope: Adding new external services, schedulers, or notification channels.
- Out of scope: Redesigning the full artifact schema for all phases.

## Exact Acceptance Criteria
- Running `python scripts/run_tester.py --repo . --task agents/ai-automated-development/backlog/tasks/<task-file>.md --dry-run` prints a tester report that includes a deterministic explicit outcome line such as `Outcome: READY`, `Outcome: RETRY`, or `Outcome: BLOCKED`.
- When `python scripts/run_cycle.py --repo . --phase tester --auto-continue --dry-run` reaches a tester report whose outcome is not ready/continue, the cycle summary indicates auto-continuation stops because of the tester result instead of silently proceeding to another cycle.
- If current `MVP` state policy would otherwise rewrite `--phase tester`, this task must update that policy enough for the above tester-gated dry-run path to execute intentionally rather than being redirected before tester runs.
- In a non-dry-run execution, the run writes a visible target-scoped log artifact under `agents/ai-automated-development/logs/` whose recorded reason reflects the tester-driven stop condition.
- `python -m py_compile scripts/run_cycle.py scripts/run_tester.py` completes successfully.

## Step-by-Step Implementation Plan
1. Review `agents/ai-automated-development/backlog/tasks/TASK-031-ai-auto-tester-stop-signal.md` and confirm the task is still in scope.
2. Update `agents/ai-automated-development/backlog/tasks/TASK-031-ai-auto-tester-stop-signal.md` status from `todo` to `in-progress` before making changes.
3. Apply the required repository changes in `scripts/run_tester.py`, `scripts/run_cycle.py`.
4. Run the smallest relevant verification commands for the changed files.
5. Update `agents/ai-automated-development/backlog/tasks/TASK-031-ai-auto-tester-stop-signal.md` to `done` only after the acceptance criteria are met.
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
Goal: Close the loop-control gap where `scripts/run_cycle.py` auto-continues through the tester phase without consuming a clear tester outcome. Implement deterministic tester outcome parsing and use it to continue only on explicit READY/continue-style results, while writing a visible stop reason artifact when the tester reports retry or blocked.
Selected task file: `agents/ai-automated-development/backlog/tasks/TASK-031-ai-auto-tester-stop-signal.md`

Files likely to change:
- `agents/ai-automated-development/backlog/tasks/TASK-031-ai-auto-tester-stop-signal.md`
- `scripts/run_tester.py`
- `scripts/run_cycle.py`

Constraints:
- Implement exactly one approved backlog task in a focused change set.
- Keep changes scoped to the selected task `agents/ai-automated-development/backlog/tasks/TASK-031-ai-auto-tester-stop-signal.md`.
- Avoid unrelated refactors.
- Update task status from `todo` to `in-progress` before implementation and to `done` only after verification.
- If blocked, set the task status to `blocked` and explain why.
- Out of scope: Changing reviewer or developer verification policy beyond what is needed for tester outcome consumption.
- Out of scope: Adding new external services, schedulers, or notification channels.
- Out of scope: Redesigning the full artifact schema for all phases.

Acceptance criteria:
- Running `python scripts/run_tester.py --repo . --task agents/ai-automated-development/backlog/tasks/<task-file>.md --dry-run` prints a tester report that includes a deterministic explicit outcome line such as `Outcome: READY`, `Outcome: RETRY`, or `Outcome: BLOCKED`.
- When `python scripts/run_cycle.py --repo . --phase tester --auto-continue --dry-run` reaches a tester report whose outcome is not ready/continue, the cycle summary indicates auto-continuation stops because of the tester result instead of silently proceeding to another cycle.
- If current `MVP` state policy would otherwise rewrite `--phase tester`, this task must update that policy enough for the above tester-gated dry-run path to execute intentionally rather than being redirected before tester runs.
- In a non-dry-run execution, the run writes a visible target-scoped log artifact under `agents/ai-automated-development/logs/` whose recorded reason reflects the tester-driven stop condition.
- `python -m py_compile scripts/run_cycle.py scripts/run_tester.py` completes successfully.

Implementation plan:
1. Review `agents/ai-automated-development/backlog/tasks/TASK-031-ai-auto-tester-stop-signal.md` and confirm the task is still in scope.
2. Update `agents/ai-automated-development/backlog/tasks/TASK-031-ai-auto-tester-stop-signal.md` status from `todo` to `in-progress` before making changes.
3. Apply the required repository changes in `scripts/run_tester.py`, `scripts/run_cycle.py`.
4. Run the smallest relevant verification commands for the changed files.
5. Update `agents/ai-automated-development/backlog/tasks/TASK-031-ai-auto-tester-stop-signal.md` to `done` only after the acceptance criteria are met.
6. Prepare a concise developer completion report for the reviewer with changed files, assumptions, and verification results.

Selected task content:
```md
# TASK-031 Add tester stop-condition signaling to auto-continue runner

## Status
todo

## Priority
high

## Objective
Close the loop-control gap where `scripts/run_cycle.py` auto-continues through the tester phase without consuming a clear tester outcome. Implement deterministic tester outcome parsing and use it to continue only on explicit READY/continue-style results, while writing a visible stop reason artifact when the tester reports retry or blocked.

## Scope
- Update `scripts/run_tester.py` to emit a deterministic machine-readable outcome field in the tester report content, for example an explicit `Outcome: READY|RETRY|BLOCKED` line, in the existing target-scoped tester artifacts under `agents/<target-name>/test/`.
- Update `scripts/run_cycle.py` to read the latest tester artifact for the selected task, parse the tester outcome, and treat non-ready outcomes as stop conditions during `--auto-continue`.
- If needed, update the current `MVP` phase-gating logic in `scripts/run_cycle.py` so a controlled `--phase tester --auto-continue` path can actually reach tester outcome evaluation instead of being rewritten to reviewer before the tester phase runs.
- If not already present in the continuation path, write a visible stop artifact/log entry via the existing run logging flow under `agents/ai-automated-development/logs/` that records the tester-driven stop reason.

## Out of Scope
- Changing reviewer or developer verification policy beyond what is needed for tester outcome consumption.
- Adding new external services, schedulers, or notification channels.
- Redesigning the full artifact schema for all phases.

## Acceptance Criteria
- Running `python scripts/run_tester.py --repo . --task agents/ai-automated-development/backlog/tasks/<task-file>.md --dry-run` prints a tester report that includes a deterministic explicit outcome line such as `Outcome: READY`, `Outcome: RETRY`, or `Outcome: BLOCKED`.
- When `python scripts/run_cycle.py --repo . --phase tester --auto-continue --dry-run` reaches a tester report whose outcome is not ready/continue, the cycle summary indicates auto-continuation stops because of the tester result instead of silently proceeding to another cycle.
- If current `MVP` state policy would otherwise rewrite `--phase tester`, this task must update that policy enough for the above tester-gated dry-run path to execute intentionally rather than being redirected before tester runs.
- In a non-dry-run execution, the run writes a visible target-scoped log artifact under `agents/ai-automated-development/logs/` whose recorded reason reflects the tester-driven stop condition.
- `python -m py_compile scripts/run_cycle.py scripts/run_tester.py` completes successfully.

## Dependencies
- None

## Notes
Generated by `scripts/run_planner.py` because the backlog was exhausted during an AI-backed MVP gap evaluation.
Grounding:
- `docs/mvp.md` requires the orchestrator to stop cleanly on failures/blockers and requires tester output to report a clear continue / retry / blocked outcome that the orchestrator can use for loop continuation decisions.
- `scripts/run_cycle.py` currently includes auto-continue logic and stop-reason handling, but the repository evidence does not show tester outcome parsing being consumed by the runner.
- `scripts/run_tester.py` currently derives a coarse `READY` vs not-ready status in report generation under `agents/<target-name>/test/`, but no repository evidence shows a deterministic contract that `scripts/run_cycle.py` reads to enforce tester-gated continuation.
- Current `MVP` runner policy rewrites `--phase tester` to reviewer, so tester-gated continuation is not yet reachable without a focused runner change in `scripts/run_cycle.py`.
- The target-scoped analysis explicitly notes that future phases still need integration points and output contracts, making tester-to-orchestrator integration a grounded remaining MVP gap.
Slug: `ai-auto-tester-stop-signal`

```

````
