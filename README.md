# laboratorio-agentes-cloud

Minimal cloud lab for running OpenAI agent experiments from GitHub Actions.

## What this repo does

This repository lets you test small agents without running anything on your local machine.

The flow is:

1. Edit or add an agent in `agents/`.
2. Open the `Actions` tab in GitHub.
3. Select `Run agent`.
4. Click `Run workflow`.
5. Read the result in the workflow logs.

## Required secret

Before running the workflow, add this repository secret:

```text
OPENAI_API_KEY
```

Path in GitHub:

```text
Settings -> Secrets and variables -> Actions -> New repository secret
```

Do not commit API keys to the repository.

## Manual run

The workflow accepts one optional input:

```text
text
```

If you leave it empty, the workflow uses a default short text.

## Files

```text
agents/test_agent.py
.github/workflows/run-agent.yml
requirements.txt
```

## Local execution

Local execution is not required for this lab. The intended execution surface is GitHub Actions.
