# Markdown to Word MCP Server

FastMCP server that converts Markdown documents to Microsoft Word format.

## Features

- Convert markdown to DOCX with proper formatting
- Support for headers, paragraphs, and code blocks
- Template system for consistent styling
- Document metadata injection
- Validation for conversion compatibility

## MCP Functions

- `convert_markdown_to_docx()` - Convert markdown content to Word document
- `list_available_templates()` - List available Word templates
- `validate_markdown()` - Validate markdown for conversion compatibility

## Usage

```bash
python server.py
```

## Templates

Place Word template files (.docx) in the `templates/` directory:
- `simple.docx` - Basic formatting
- `corporate.docx` - Corporate styling
- `technical.docx` - Technical documentation format