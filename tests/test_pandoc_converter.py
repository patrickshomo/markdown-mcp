"""Test Pandoc converter."""

import pytest
import tempfile
import os
from pathlib import Path

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.mcp.markdown_converter.pandoc_converter import PandocConverter


def test_basic_conversion():
    """Test basic markdown conversion."""
    converter = PandocConverter()
    
    markdown = """# Test Document

This is a **bold** test with *italic* text.

- [x] Completed task
- [ ] Pending task

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |

```python
print("Hello World")
```
"""
    
    with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as tmp:
        output_path = converter.convert(markdown, tmp.name, {'title': 'Test'})
        
        assert os.path.exists(output_path)
        assert Path(output_path).stat().st_size > 0
        
        # Cleanup
        os.unlink(output_path)


def test_validation():
    """Test markdown validation."""
    converter = PandocConverter()
    
    markdown = """# Test
- [x] Task
| Table | Header |
|-------|--------|
~~strikethrough~~
```code```
"""
    
    result = converter.validate_markdown(markdown)
    
    assert result['valid'] is True
    assert 'task_lists' in result['features_detected']
    assert 'tables' in result['features_detected']
    assert 'strikethrough' in result['features_detected']
    assert 'code_blocks' in result['features_detected']