"""Test script for the markdown converter."""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.mcp.markdown_converter.converter import MarkdownConverter


def test_basic_conversion():
    """Test basic markdown to docx conversion."""
    markdown_content = """# Test Document

This is a test paragraph.

## Section 1

Some content here.

```python
def hello():
    print("Hello, World!")
```

Another paragraph."""

    converter = MarkdownConverter()
    doc = converter.convert(markdown_content, {"title": "Test Doc", "author": "Test User"})
    
    # Save test output
    doc.save("test_output.docx")
    print("Test document saved as test_output.docx")


if __name__ == "__main__":
    test_basic_conversion()