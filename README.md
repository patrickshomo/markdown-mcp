# Markdown to Word MCP Server

FastMCP server that converts Markdown documents to Microsoft Word format with template support and professional formatting.

## Features

### ✅ Implemented
- **Basic Conversion** - Markdown to DOCX with proper formatting
- **Headers & Paragraphs** - Full heading hierarchy support
- **Code Blocks** - Monospace formatting for code sections
- **Metadata Injection** - Document properties (title, author, subject)
- **Template System** - Foundation for Word template support
- **Validation** - Check markdown compatibility before conversion

### 🚧 In Development
- **Template Support** - Corporate, technical, and simple templates
- **Image Handling** - Embed images referenced in markdown
- **Table Conversion** - Preserve markdown table formatting
- **Mermaid Diagrams** - Convert diagrams to embedded images
- **Batch Processing** - Convert entire directories
- **TOC Generation** - Automatic table of contents

## MCP Functions

- `convert_markdown_to_docx()` - Convert markdown content to Word document
- `list_available_templates()` - List available Word templates
- `validate_markdown()` - Validate markdown for conversion compatibility

## Usage

```python
from src.mcp.markdown_converter.converter import MarkdownConverter

converter = MarkdownConverter()
doc = converter.convert(markdown_content, {"title": "My Document"})
doc.save("output.docx")
```

## VSCode Integration

Perfect for:
- **Cline/Q-Dev Workflow** - Generate markdown docs, convert to Word for clients
- **Report Generation** - Technical specs → Professional Word documents
- **Proposal Creation** - Markdown drafts → Formatted proposals
- **Documentation Pipeline** - README.md → Professional documentation

## Structure

- `src/mcp/markdown_converter/` - MCP server implementation
- `docker/` - Container configurations (coming soon)
- `doc/` - Documentation and guides