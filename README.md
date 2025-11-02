# langgraph_agents

A lightweight framework for building and orchestrating language-model agents and agent workflows. Designed to help prototype, test, and run conversational or task-oriented agents that interact with language models and structured graphs.

## Key features
- Simple agent abstraction for prompts, actions, and state
- Pluggable model backends (local, API-based)
- Workflow composition and chaining of agents
- Utilities for prompt templates, retries, and logging
- Example agents and test harnesses

## Quick start

Prerequisites
- Python 3.10+
- pip

Install
```bash
pip install -r requirements.txt
```

## Project layout
- langgraph_agents/        — package source
- agents/                  — agent implementations using notebooks
- README.md                — this file
- requirements.txt         — dependencies