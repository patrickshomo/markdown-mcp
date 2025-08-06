# Pandoc Setup Guide

## Quick Start

### 1. Install Pandoc
```bash
# macOS
brew install pandoc

# Ubuntu/Debian
sudo apt install pandoc

# Windows
# Download from https://pandoc.org/installing.html
```

### 2. Install Dependencies
```bash
uv sync
```

### 3. Test Conversion
```bash
uv run python test_pandoc_demo.py
```

### 4. Run MCP Server
```bash
uv run python run_mcp_server.py
```

## What Changed

✅ **Before (Manual Mapping)**: 1000+ lines of complex style mapping  
✅ **After (Pandoc)**: ~100 lines of clean, reliable code  

✅ **Before**: Partial GFM support with bugs  
✅ **After**: Complete GFM support via Pandoc  

✅ **Before**: Complex maintenance  
✅ **After**: Battle-tested Pandoc handles everything  

## Benefits

- **Perfect GFM Support** - All GitHub Flavored Markdown features
- **Zero Maintenance** - Pandoc handles format updates
- **Reliable** - Industry standard document converter
- **Clean Code** - Minimal, readable implementation
- **Future-Proof** - Pandoc supports new formats automatically