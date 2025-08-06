# Bin Directory

Executable utilities for the markdown-mcp project.

## extract-word-styles

Reads a Word document and outputs all style definitions including font properties, paragraph formatting, and other style attributes.

### Usage

```bash
./bin/extract-word-styles document.docx
```

### Output

The script displays:
- Style name and type
- Font properties (name, size, bold, italic, underline, color)
- Paragraph formatting (alignment, indentation, spacing)
- Whether the style is built-in to Word

### Example

```bash
./bin/extract-word-styles tests/sample.docx
```

This will output all style definitions found in the document, useful for understanding how Word documents are formatted and for reverse-engineering style mappings.