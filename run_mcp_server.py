#!/usr/bin/env python3
"""Run the MCP server."""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from src.mcp.markdown_converter.server import mcp

if __name__ == "__main__":
    print("🚀 Starting Pandoc Markdown Converter MCP Server...")
    mcp.run()