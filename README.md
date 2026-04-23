# Hermes Agent

A fork of [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — an autonomous AI agent framework powered by Hermes models with tool-calling and structured reasoning capabilities.

> **Personal fork notes:** I'm using this with a local Ollama backend. Setting `OPENAI_API_BASE=http://localhost:11434/v1` and `MODEL_NAME=hermes3` works well. I've also found that dropping `TEMPERATURE` to `0.3` gives more consistent tool-calling behavior.

## Features

- 🤖 **Hermes Model Integration** — Optimized for NousResearch Hermes series models
- 🛠️ **Tool Calling** — Native function/tool calling with structured JSON outputs
- 🔄 **Agentic Loops** — ReAct-style reasoning and action cycles
- 🐳 **Docker Support** — Containerized deployment out of the box
- 🔧 **Configurable** — Extensive environment-based configuration

## Quick Start

### Prerequisites

- Python 3.10+
- An OpenAI-compatible API endpoint (e.g., vLLM, Ollama, OpenAI)
- Docker (optional)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-org/hermes-agent.git
cd hermes-agent

# Copy environment configuration
cp .env.example .env

# Edit .env with your settings
nano .env

# Install dependencies
pip install -r requirements.txt
```

### Running with Docker

```bash
docker compose up --build
```

### Running Locally

```bash
python -m hermes_agent
```

## Configuration

All configuration is handled via environment variables. See [`.env.example`](.env.example) for a full list of options.

### Key Settings

| Variable | Description | Default |
|---|---|---|
| `OPENAI_API_BASE` | API base URL for your LLM backend | `http://localhost:8000/v1` |
| `OPENAI_API_KEY` | API key (can be dummy for local) | `sk-dummy` |
| `MODEL_NAME` | Model identifier to use | `NousResearch/Hermes-3-Llama-3.1-8B` |
| `MAX_ITERATIONS` | Max agentic loop iterations | `10` |
| `TEMPERATURE` | Sampling temperature | `0.3` |

### Ollama Setup

If you're running locally with Ollama:

```bash
OPENAI_API_BASE=http://localhost:11434/v1
OPENAI_API_KEY=ollama
MODEL_NAME=hermes3
TEMPERATURE=0.3  # lower temp helps with reliable tool call formatting
```

## Architecture

```
hermes_agent/
├── __main__.py          # Entry point
├── agent.py             # Core agent loop
├── tools/               # Tool definitions and implementations
│   ├── __init__.py
│   ├── base.py
│   └── builtins.py
├── models/              # Pydantic models / schemas
├── prompts/             # System and user prompt templates
└── utils/               # Utility helpers
```

## Contributing

Please open an issue before submitting a PR. See the [issue templates](.github/ISSUE_TEMPLATE/) for bug reports, feature requests, and setup help.

## License

MIT — see [LICENSE](LICENSE) for details.
