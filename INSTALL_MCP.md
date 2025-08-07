# MCP Client Installation for Q-Dev

## Quick Setup

### 1. Install Dependencies
```bash
cd /Users/pat/Documents/Dev/markdown-mcp
uv sync
```

### 2. Install Pandoc
```bash
brew install pandoc
```

### 3. Configure Q-Dev MCP Client

Add this to your Q-Dev MCP configuration file:

```json
{
  "mcpServers": {
    "markdown-converter": {
      "command": "uv",
      "args": ["run", "python", "run_mcp_server.py"],
      "cwd": "/Users/pat/Documents/Dev/markdown-mcp"
    }
  }
}
```

**Configuration File Locations:**

**Option 1: Personal Directory (Recommended)**
- `~/.amazonq/mcp_servers.json`

**Option 2: Application Directory**
- **macOS**: `~/Library/Application Support/Amazon Q/mcp_config.json`
- **Linux**: `~/.config/amazonq/mcp_config.json`
- **Windows**: `%APPDATA%\Amazon Q\mcp_config.json`

### 4. Test the Server
```bash
# Test locally first
uv run python run_mcp_server.py
```

### 5. Restart Q-Dev
Restart Q-Dev to load the new MCP server configuration.

## Available Functions

Once configured, you can use these functions in Q-Dev:

- `convert_markdown_to_docx()` - Convert markdown to Word with full GFM support
- `validate_markdown_compatibility()` - Check markdown features
- `batch_convert_directory()` - Convert entire directories
- `get_conversion_features()` - List supported features

## Usage Example

In Q-Dev chat:
```
Convert this markdown to Word format:
# My Document
- [x] Task completed
- [ ] Task pending
```

The MCP server will handle the conversion using Pandoc with complete GitHub Flavored Markdown support.