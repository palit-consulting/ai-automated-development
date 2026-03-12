# Target Repository Context

## Purpose

This document explains how agents should understand and interact with a target repository.

The system is designed to run agents against an external repository to analyze, plan, implement, review, and validate improvements.

Agents must first build a clear understanding of the target repository before performing any changes.

---

## Repository Overview

Agents should first determine:

- what the repository does
- what problem it solves
- who the expected users are
- the overall maturity of the project

If documentation exists (README, docs folder), it should be analyzed first.

---

## Technology Identification

Agents should identify the technology stack used in the repository.

Examples:

- programming languages
- frameworks
- build systems
- package managers
- testing frameworks
- infrastructure tools

Understanding the stack helps prevent incompatible changes.

---

## Repository Structure

Agents must inspect the directory structure to understand how the project is organized.

Important things to identify:

- source code directories
- documentation directories
- configuration files
- test directories
- scripts or automation

Agents should infer the architectural structure from the directory layout.

---

## Architecture Understanding

Agents should summarize the architecture.

Examples:

- monolithic application
- layered architecture
- microservices
- modular system
- frontend/backend separation

The analysis should describe the major components and their relationships.

---

## Conventions

Agents must identify project conventions such as:

- naming conventions
- directory patterns
- testing practices
- documentation style
- dependency management

Agents should respect these conventions when making changes.

---

## Quality Signals

Agents should evaluate the maturity of the project by looking for signals such as:

- presence of automated tests
- documentation completeness
- CI/CD configuration
- linting or formatting tools
- dependency management practices

These signals help guide improvement priorities.

---

## Risks and Gaps

Agents should identify potential weaknesses such as:

- missing documentation
- missing tests
- unclear architecture
- inconsistent code structure
- duplicated logic

These findings should be highlighted in the analysis.

---

## Improvement Opportunities

Agents should identify areas where the project can improve.

Examples:

- missing developer documentation
- unclear project structure
- lack of examples
- missing contributor guidance
- missing automation

These observations will be used by the Planner agent to generate backlog tasks.

---

## Expected Output

The Analyst agent must produce a structured report stored in:

    analysis/repo-analysis.md

The report should contain:

- repository overview
- technology stack
- architecture summary
- key components
- conventions
- risks
- improvement opportunities

This output becomes the primary input for the Planner agent.
