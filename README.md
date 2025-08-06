# Markdown to Word MCP Server

**Pandoc-powered** FastMCP server that converts Markdown documents to Microsoft Word format with **complete GitHub Flavored Markdown (GFM) support**.

## Features

### ✅ Pandoc-Powered Implementation
- **Perfect GFM Support** - Pandoc handles all GitHub Flavored Markdown features
- **Zero Mapping Complexity** - No manual style management needed
- **Battle-Tested** - Uses Pandoc, the gold standard for document conversion
- **Clean Codebase** - ~100 lines vs 1000+ lines of manual mapping
- **All GFM Features** - Task lists, tables, strikethrough, code blocks, everything
- **Batch Processing** - Convert entire directories
- **Validation** - Markdown analysis and feature detection
- **Metadata Support** - Document properties (title, author)

## MCP Functions

- `convert_markdown_to_docx()` - Convert markdown using Pandoc with full GFM support
- `validate_markdown_compatibility()` - Analyze markdown features and compatibility
- `batch_convert_directory()` - Convert entire directories
- `get_conversion_features()` - Get supported features and capabilities

## Usage

### Basic Conversion
```python
from src.mcp.markdown_converter.pandoc_converter import PandocConverter

converter = PandocConverter()
output_path = converter.convert(
    markdown_content, 
    "output.docx",
    {"title": "My Document", "author": "Author Name"}
)
```

### With Validation
```python
# Validate before conversion
validation = converter.validate_markdown(markdown_content)
if validation['valid']:
    print(f"Features: {validation['features_detected']}")
    converter.convert(markdown_content, "output.docx")
```

### Supported GFM Features
- ✅ **Task Lists**: `- [x] Done` `- [ ] Todo`
- ✅ **Tables**: Full alignment support
- ✅ **Strikethrough**: `~~deleted text~~`
- ✅ **Code Blocks**: ```python with syntax info
- ✅ **Complex Emphasis**: *italic **bold** text*
- ✅ **Links & Images**: Full reference link support

## VSCode Integration

Perfect for:
- **Cline/Q-Dev Workflow** - Generate markdown docs, convert to Word for clients
- **Report Generation** - Technical specs → Professional Word documents
- **Proposal Creation** - Markdown drafts → Formatted proposals
- **Documentation Pipeline** - README.md → Professional documentation

## Structure

- `src/mcp/markdown_converter/` - MCP server implementation
  - `pandoc_converter.py` - Pandoc-powered converter (clean & minimal)
  - `server.py` - FastMCP server with all functions
- `tests/` - Test suite including Pandoc converter tests
- `run_mcp_server.py` - MCP server runner

## Requirements

- **Pandoc** - Install with `brew install pandoc` (macOS) or equivalent
- **Python 3.11+** with dependencies from `pyproject.toml`