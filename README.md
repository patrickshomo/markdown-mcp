# Markdown to Word MCP Server

FastMCP server that converts Markdown documents to Microsoft Word format with **full GitHub Flavored Markdown (GFM) support** and professional formatting.

## Features

### ✅ Fully Implemented
- **GFM Compliance** - Complete GitHub Flavored Markdown support
- **Task Lists** - Checkbox rendering (`- [x]` → ☑, `- [ ]` → ☐)
- **Tables** - Full GFM table support with alignment
- **Strikethrough** - `~~text~~` formatting support
- **Code Blocks** - Fenced code blocks with language detection
- **Enhanced Formatting** - Complex emphasis, links, images
- **Template System** - Corporate, technical, and simple templates
- **Image Handling** - Embed images referenced in markdown
- **Mermaid Diagrams** - Convert diagrams to embedded images
- **Batch Processing** - Convert entire directories
- **Validation** - Comprehensive markdown analysis and feature detection
- **Metadata Injection** - Document properties (title, author, subject)

## MCP Functions

- `convert_markdown_to_docx()` - Convert markdown with full GFM support
- `validate_markdown_compatibility()` - Analyze markdown features and compatibility
- `list_available_templates()` - List available Word templates
- `batch_convert_directory()` - Convert entire directories
- `get_conversion_features()` - Get supported features and capabilities

## Usage

### Basic Conversion
```python
from src.mcp.markdown_converter.simple_improved_converter import SimpleImprovedConverter

converter = SimpleImprovedConverter()
doc = converter.convert(markdown_content, {"title": "My Document"})
doc.save("output.docx")
```

### With Validation
```python
# Validate before conversion
validation = converter.validate_markdown(markdown_content)
if validation['valid']:
    print(f"Features: {validation['features_detected']}")
    doc = converter.convert(markdown_content)
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
  - `simple_improved_converter.py` - Enhanced GFM-compliant converter
  - `enhanced_server.py` - Full-featured MCP server
- `tests/` - Comprehensive test suite
- `CONVERSION_IMPROVEMENTS.md` - Detailed feature comparison
- `IMPLEMENTATION_SUMMARY.md` - Complete implementation guide