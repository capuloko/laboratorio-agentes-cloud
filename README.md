# laboratorio-agentes-cloud

Cloud-based AI agent lab for testing small agent ideas with GitHub Actions and the OpenAI API.

## What this repo is for

This repository lets you:

- create new agents easily
- run agents on demand from GitHub Actions
- keep agent code reusable
- see clear output in workflow logs
- save run output under `results/`

No local Python, Docker, server, or database is required to run the first agent.

## Structure

```text
agents/
  base_agent.py
  test_agent.py

core/
  config.py
  runner.py

evals/
  simple_eval.py

results/
  .gitkeep

.github/workflows/
  run-agent.yml

requirements.txt
README.md
```

## Required GitHub secret

Create this repository secret before running the workflow:

```text
OPENAI_API_KEY
```

Path:

```text
Settings -> Secrets and variables -> Actions -> New repository secret
```

Do not commit API keys to the repository.

Optional model override:

```text
OPENAI_MODEL
```

If not set, the code uses:

```text
gpt-5.4-mini
```

## How to run the agent

1. Open this repository on GitHub.
2. Go to `Actions`.
3. Select `Run agent`.
4. Click `Run workflow`.
5. Open the workflow run logs.
6. Read the output under:

```text
=====
AGENT RESULT
=====
```

The workflow also uploads the `results/` folder as an artifact named `agent-results`.

## How to create a new agent

1. Create a new file in `agents/`, for example:

```text
agents/my_agent.py
```

2. Subclass `BaseAgent` from `agents/base_agent.py`.
3. Implement `build_prompt()`.
4. Add a runner function that returns `AgentOutput`.
5. Register that function in `core/runner.py` inside the `AGENTS` dictionary.

Minimal shape:

```python
class MyAgent(BaseAgent):
    name = "my_agent"

    def build_prompt(self, agent_input: AgentInput) -> str:
        return f"Analyze this: {agent_input.text}"
```

## Where results appear

Results appear in three places:

- GitHub Actions logs
- `results/<agent_name>_result.txt` during the workflow run
- the uploaded `agent-results` artifact

## Current agent

The default `test_agent` summarizes a business-related idea in one sentence and runs a basic evaluation that checks the output is not empty and has enough length.
