"""Test markdown formatting conversion."""

import pytest
from pathlib import Path
import tempfile
import os

from src.mcp.markdown_converter.converter import MarkdownConverter


def test_inline_formatting():
    """Test inline markdown formatting conversion."""
    converter = MarkdownConverter()
    
    markdown = """# Test Formatting

**This is bold text**

*This is italic text*

~~This is strikethrough~~

`This is inline code`

Regular text with **bold** and *italic* mixed.
"""
    
    doc = converter.convert(markdown)
    assert doc is not None
    
    # Save to temp file to verify
    with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as tmp:
        doc.save(tmp.name)
        assert Path(tmp.name).exists()
        
        # Clean up
        os.unlink(tmp.name)


def test_convert_test1_with_formatting():
    """Test conversion of test1.md with proper formatting."""
    converter = MarkdownConverter()
    
    # Read the test1.md file
    test_file = Path("tests/input/test1.md")
    if test_file.exists():
        content = test_file.read_text(encoding='utf-8')
        
        doc = converter.convert(content)
        assert doc is not None
        
        # Save with formatting
        output_file = Path("tests/output/test1_formatted.docx")
        doc.save(str(output_file))
        
        print(f"Formatted document saved to: {output_file}")
        assert output_file.exists()


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])