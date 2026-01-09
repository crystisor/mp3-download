# MP3 Downloader Agent

A Python tool that acts as both a **Conversational AI Agent** and a **Model Context Protocol (MCP) Server** to download MP3s automatically.

## Features

- **Conversational Interface**: Chat with the agent; it automatically detects download requests.
- **MCP Server Support**: Exposes a `download_song` tool for MCP-compliant clients.
- **Smart Extraction**: Uses `ollama` to extract song titles from natural language.
- **Web Scraping**: Automates downloads from mp3juice using Playwright.

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running.

## Installation

1.  **Install Python Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Install Playwright Browsers**:
    ```bash
    playwright install
    ```

3.  **Pull the AI Model**:
    The agent uses a specific Ollama model.
    ```bash
    ollama pull huihui_ai/qwen3-abliterated:8b
    ```

## Usage

### 1. Conversational Agent
Run the interactive CLI agent to chat and download music:
```bash
python agent.py
```

### 2. MCP Server
Start the MCP server to expose tools to other agents:
```bash
python main.py
```
