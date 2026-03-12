# Example: Running the Multi-Agent Workflow

## Purpose

This example demonstrates how the multi-agent development workflow can be applied to a target repository.

The goal is to show a realistic end-to-end loop involving analysis, planning, implementation, review, and validation.

---

# Example Scenario

Target repository:

    example-project/

Goal:

    Improve repository documentation and make the project easier for new contributors to understand.

The workflow will demonstrate how agents collaborate to achieve this goal.

---

# Step 1 — Human Defines the Goal

The human defines the development objective.

Example instruction:

    Improve the documentation and repository structure so that a new contributor can understand how the project works.

This goal becomes the context for the agents.

---

# Step 2 — Analyst Agent Runs

The Analyst agent inspects the repository.

Prompt:

    Read docs/mvp.md and prompts/agents/analyst.md.

    Analyze the target repository and produce a structured analysis.

Expected output:

    analysis/repo-analysis.md

Example findings:

- project lacks a clear README
- repository structure is unclear
- no contributor guide exists
- technologies detected: Python, FastAPI

---

# Step 3 — Planner Agent Runs

The Planner agent converts the analysis into backlog tasks.

Prompt:

    Read analysis/repo-analysis.md and prompts/agents/planner.md.

    Generate backlog tasks that move the repository toward the goal.

Example tasks created:

    TASK-001 create project overview in README
    TASK-002 add contributor guide
    TASK-003 document repository structure

These tasks are stored in:

    backlog/tasks/

---

# Step 4 — Human Reviews Backlog

The human reviews the proposed tasks.

Possible actions:

- approve tasks
- adjust priorities
- split large tasks
- reject tasks

The human selects the next task to implement.

Example selected task:

    TASK-001 create project overview in README

---

# Step 5 — Developer Agent Runs

The Developer agent implements the selected task.

Prompt:

    Read the task and prompts/agents/developer.md.

    Implement the task in the repository.

Outputs:

- README.md updated
- implementation summary
- list of modified files

---

# Step 6 — Reviewer Agent Runs

The Reviewer agent evaluates the implementation.

Prompt:

    Read the task, the developer output, and prompts/agents/reviewer.md.

    Review the implementation.

Output:

    reviews/review-TASK-001.md

Example result:

    APPROVED

---

# Step 7 — Tester Agent Runs

The Tester agent validates the implementation.

Prompt:

    Read the task, the developer output, and the reviewer report.

    Validate that the acceptance criteria are satisfied.

Output:

    validation/test-TASK-001.md

Example result:

    PASSED

---

# Step 8 — Human Accepts Result

The human reviews the results and accepts the task.

The backlog status becomes:

    done

---

# Iteration Continues

The workflow repeats:

1. Planner may refine backlog
2. Human selects next task
3. Developer implements it
4. Reviewer evaluates the change
5. Tester validates it

This loop continues until the goal is achieved.

---

# Outcome

The repository gradually improves through small, controlled iterations.

The system enables structured collaboration between humans and AI agents.

Each agent focuses on a specific responsibility, similar to a real software team.
