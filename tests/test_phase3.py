"""Phase 3 tests for template system."""

import pytest
from pathlib import Path
import tempfile
import os

from src.mcp.markdown_converter.converter import MarkdownConverter
from src.mcp.markdown_converter.template_manager import TemplateManager


def test_template_manager():
    """Test template manager functionality."""
    manager = TemplateManager()
    templates = manager.list_templates()
    
    # Should have built-in templates
    assert len(templates) >= 3
    template_names = [t["name"] for t in templates]
    assert "simple" in template_names
    assert "corporate" in template_names
    assert "technical" in template_names


def test_dotx_template_loading():
    """Test DOTX template loading."""
    manager = TemplateManager()
    simple_path = manager.get_template_path("simple")
    
    assert simple_path is not None
    assert simple_path.endswith(".dotx")
    assert manager.validate_template(simple_path)


def test_converter_with_template():
    """Test converter with template selection."""
    converter = MarkdownConverter()
    markdown = "# Test Document\n\nThis is a test."
    
    doc = converter.convert(markdown, template_name="simple")
    assert doc is not None
    
    # Save to temp file to verify
    with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as tmp:
        doc.save(tmp.name)
        assert Path(tmp.name).exists()
        os.unlink(tmp.name)


def test_mcp_list_templates():
    """Test MCP list templates function."""
    manager = TemplateManager()
    templates = manager.list_templates()
    assert isinstance(templates, list)
    assert len(templates) >= 3
    
    for template in templates:
        assert "name" in template
        assert "path" in template
        assert "type" in template


def test_mcp_convert_with_template():
    """Test MCP conversion with template."""
    markdown = "# Test\n\n| Col1 | Col2 |\n|------|------|\n| A | B |"
    
    converter = MarkdownConverter()
    doc = converter.convert(
        markdown,
        metadata={"title": "Test Doc"},
        template_name="corporate"
    )
    
    assert doc is not None
    
    # Save to temp file to verify
    with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as tmp:
        doc.save(tmp.name)
        assert Path(tmp.name).exists()
        os.unlink(tmp.name)


if __name__ == "__main__":
    pytest.main([__file__])