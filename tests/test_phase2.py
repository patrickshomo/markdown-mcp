"""Test Phase 2 enhancements: tables, enhanced metadata, templates."""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.mcp.markdown_converter.converter import MarkdownConverter


def test_table_conversion():
    """Test markdown table to Word table conversion."""
    markdown_content = """# Table Test

Here's a sample table:

| Name | Age | City |
|------|-----|------|
| John | 25 | NYC |
| Jane | 30 | LA |
| Bob | 35 | Chicago |

End of table test."""

    converter = MarkdownConverter()
    doc = converter.convert(markdown_content)
    
    output_path = Path(__file__).parent / "output" / "table_test.docx"
    doc.save(str(output_path))
    print(f"Table test saved: {output_path}")


def test_enhanced_metadata():
    """Test enhanced metadata support."""
    markdown_content = """# Enhanced Metadata Test

This document tests enhanced metadata features."""

    metadata = {
        "title": "Enhanced Metadata Test",
        "author": "Test User",
        "subject": "Phase 2 Testing",
        "keywords": "markdown, docx, conversion",
        "comments": "Testing enhanced metadata in Phase 2"
    }

    converter = MarkdownConverter()
    doc = converter.convert(markdown_content, metadata)
    
    output_path = Path(__file__).parent / "output" / "metadata_test.docx"
    doc.save(str(output_path))
    print(f"Metadata test saved: {output_path}")


def test_template_usage():
    """Test template system."""
    markdown_content = """# Template Test Document

## Introduction
This document tests the template system.

## Features
- Template loading
- Style inheritance
- Professional formatting

## Code Example
```python
def test_function():
    return "Hello, templates!"
```

## Data Table
| Feature | Status |
|---------|--------|
| Templates | Working |
| Tables | Working |
| Code | Working |
"""

    # Test each template
    templates = ['simple', 'corporate', 'technical']
    
    for template in templates:
        template_path = Path(__file__).parent.parent / "src" / "mcp" / "markdown_converter" / "templates" / f"{template}.docx"
        
        if template_path.exists():
            converter = MarkdownConverter(str(template_path))
            doc = converter.convert(markdown_content, {"title": f"{template.title()} Template Test"})
            
            output_path = Path(__file__).parent / "output" / f"template_{template}_test.docx"
            doc.save(str(output_path))
            print(f"Template {template} test saved: {output_path}")
        else:
            print(f"Template {template} not found at {template_path}")


def test_complex_document():
    """Test complex document with all Phase 2 features."""
    markdown_content = """# Phase 2 Feature Test

## Overview
This document demonstrates all Phase 2 enhancements.

## Code Blocks
Here's some Python code:

```python
def convert_markdown(content):
    converter = MarkdownConverter()
    return converter.convert(content)
```

## Data Tables
Performance comparison:

| Feature | Phase 1 | Phase 2 |
|---------|---------|---------|
| Headers | ✓ | ✓ |
| Paragraphs | ✓ | ✓ |
| Code Blocks | Basic | Enhanced |
| Tables | ✗ | ✓ |
| Metadata | Basic | Enhanced |
| Templates | ✗ | ✓ |

## Additional Content
More paragraphs and content to test the complete conversion process.

### Subsection
Final testing content."""

    metadata = {
        "title": "Phase 2 Complete Test",
        "author": "Test Suite",
        "subject": "Comprehensive Phase 2 Testing",
        "keywords": "phase2, tables, templates, metadata"
    }

    converter = MarkdownConverter()
    doc = converter.convert(markdown_content, metadata)
    
    output_path = Path(__file__).parent / "output" / "phase2_complete_test.docx"
    doc.save(str(output_path))
    print(f"Complete Phase 2 test saved: {output_path}")


if __name__ == "__main__":
    # Ensure output directory exists
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    
    print("Running Phase 2 tests...")
    test_table_conversion()
    test_enhanced_metadata()
    test_template_usage()
    test_complex_document()
    print("Phase 2 tests completed!")