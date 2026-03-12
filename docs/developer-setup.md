# Developer Setup

This document explains how developers can run the **AI Automated Development agents** locally.

---

# Prerequisites

Required tools:

- Linux / WSL
- Git
- Python 3.11+
- OpenAI API key
- GitHub personal access token

Optional:

- MS Teams webhook for notifications

---

# 1. Clone the Repository

```bash
git clone https://github.com/palit-consulting/ai-automated-development.git
cd ai-automated-development
```

---

# 2. Create Python Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 3. Environment Variables

Create a `.env` file or export variables in your shell.

Example:

```bash
export OPENAI_API_KEY="your-openai-api-key"
export GITHUB_TOKEN="your-github-token"
export MS_TEAMS_WEBHOOK_URL="https://outlook.office.com/webhook/..." # optional
```

Required variables:

| Variable | Description |
|--------|--------|
| OPENAI_API_KEY | API key for OpenAI models |
| GITHUB_TOKEN | GitHub token used for repo access |

Optional:

| Variable | Description |
|--------|--------|
| MS_TEAMS_WEBHOOK_URL | Sends agent notifications |

---

# 4. GitHub Token Permissions

Create a token here:

https://github.com/settings/tokens

Recommended permissions:

```
repo
workflow
read:org
```

The token allows the agent to:

- read issues
- create branches
- push commits
- open pull requests

---

# 5. Running Agents

Run the main agent script:

```bash
./run-agents.sh
```

Or directly:

```bash
python tools/agents/run_agents.py
```

Typical workflow:

1. Agent scans GitHub issues
2. Selects a task
3. Generates code using OpenAI
4. Creates a branch
5. Opens a Pull Request

---

# 6. Running Agents Continuously

Example loop:

```bash
while true
do
  ./run-agents.sh
  sleep 300
done
```

This checks for new tasks every **5 minutes**.

---

# 7. GitHub Integration

Agents interact with the repository by:

- reading backlog tasks
- creating branches
- committing changes
- opening pull requests

Typical branch naming:

```
agent/issue-123
```

---

# 8. Notifications

If `MS_TEAMS_WEBHOOK_URL` is configured, agents send updates:

- task started
- PR created
- task failed

---

# 9. Troubleshooting

## Missing API key

```
OPENAI_API_KEY not set
```

Solution:

```bash
export OPENAI_API_KEY=...
```

---

## GitHub authentication failure

Verify token:

```bash
export GITHUB_TOKEN=...
```

---

## Python dependencies missing

Reinstall:

```bash
pip install -r requirements.txt
```

---

# 10. Recommended Workflow

1. Create tasks in:

```
backlog/tasks/
```

2. Run agents.

3. Review Pull Requests.

4. Merge approved changes.

---

# Directory Overview

```
ai-automated-development
│
├─ backlog/
│   └─ tasks/
│
├─ tools/
│   └─ agents/
│
├─ scripts/
│
└─ docs/
    └─ developer-setup.md
```
