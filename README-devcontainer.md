# Development containers and GitHub Codespaces

This repository can be used with VS Code Dev Containers and GitHub Codespaces. The steps below provide a practical starting point for contributors who want a ready-to-use Python environment.

## Prerequisites

- Docker Desktop for local Dev Containers
- VS Code with the Dev Containers extension
- A GitHub account for GitHub Codespaces

## VS Code Dev Containers

1. Install Docker Desktop and the Dev Containers extension.
2. Open this repository in VS Code.
3. Run the command palette action "Dev Containers: Reopen in Container".
4. Wait for the container to build and then run the setup commands below:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make install
```

## GitHub Codespaces

1. Open the repository on GitHub.
2. Select "Code" and then "Create codespace on main".
3. Once the environment is ready, run the same setup commands shown above.

## Useful follow-up commands

- `make zope-start` to start the Plone instance
- `make test` to run the test suite
