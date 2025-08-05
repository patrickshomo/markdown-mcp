"""Phase 4 tests for advanced features."""

import pytest
from pathlib import Path
import tempfile
import os

from src.mcp.markdown_converter.converter import MarkdownConverter
from src.mcp.markdown_converter.image_handler import ImageHandler
from src.mcp.markdown_converter.mermaid_handler import MermaidHandler
from src.mcp.markdown_converter.batch_processor import BatchProcessor


def test_image_handler():
    """Test image handling functionality."""
    handler = ImageHandler()
    
    # Test image pattern detection
    content = "# Test\n\n![Alt text](test.png)\n\nMore content."
    from docx import Document
    doc = Document()
    
    processed = handler.process_images(doc, content)
    assert "[Image: Alt text]" in processed
    assert "![Alt text](test.png)" not in processed


def test_mermaid_handler():
    """Test Mermaid diagram handling."""
    handler = MermaidHandler()
    
    # Test mermaid pattern detection
    content = "# Test\n\n```mermaid\ngraph TD\nA --> B\n```\n\nMore content."
    from docx import Document
    doc = Document()
    
    processed = handler.process_mermaid(doc, content)
    # Should replace mermaid block regardless of CLI availability
    assert "```mermaid" not in processed
    assert "[Mermaid Diagram" in processed


def test_converter_with_images():
    """Test converter with image processing."""
    converter = MarkdownConverter()
    markdown = "# Test\n\n![Test Image](nonexistent.png)\n\nContent."
    
    doc = converter.convert(markdown)
    assert doc is not None


def test_batch_processor_setup():
    """Test batch processor initialization."""
    processor = BatchProcessor()
    assert processor.converter is not None


def test_batch_process_nonexistent_directory():
    """Test batch processing with nonexistent directory."""
    processor = BatchProcessor()
    
    result = processor.process_directory("/nonexistent", "/tmp/output")
    assert "error" in result
    assert "not found" in result["error"]


def test_batch_process_files():
    """Test batch processing specific files."""
    processor = BatchProcessor()
    
    # Create temp markdown file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as tmp:
        tmp.write("# Test Document\n\nThis is a test.")
        temp_md = tmp.name
    
    with tempfile.TemporaryDirectory() as output_dir:
        result = processor.process_files([temp_md], output_dir)
        
        assert result["processed"] == 1
        assert result["successful"] == 1
        assert result["failed"] == 0
        
        # Check output file exists
        output_file = Path(output_dir) / f"{Path(temp_md).stem}.docx"
        assert output_file.exists()
    
    os.unlink(temp_md)


def test_enhanced_validation():
    """Test enhanced validation with Phase 4 features."""
    converter = MarkdownConverter()
    
    markdown_with_features = """
# Test Document

![Image](test.png)

```mermaid
graph TD
A --> B
```

Regular content.
"""
    
    # Should handle conversion without errors
    doc = converter.convert(markdown_with_features)
    assert doc is not None


if __name__ == "__main__":
    pytest.main([__file__])