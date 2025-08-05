"""Test the improved markdown converter against GFM specification."""

import pytest
from src.mcp.markdown_converter.improved_converter import ImprovedMarkdownConverter
from src.mcp.markdown_converter.converter import MarkdownConverter


class TestImprovedConverter:
    """Test improved converter features."""
    
    def setup_method(self):
        self.improved_converter = ImprovedMarkdownConverter()
        self.original_converter = MarkdownConverter()
    
    def test_gfm_tables(self):
        """Test GitHub Flavored Markdown table support."""
        markdown_content = """
| Feature | Original | Improved |
|---------|----------|----------|
| Tables  | Basic    | Full GFM |
| Code    | Simple   | Highlighted |
| Tasks   | None     | ✓ Supported |
"""
        
        # Test improved converter
        doc = self.improved_converter.convert(markdown_content)
        assert len(doc.tables) > 0
        
        # Validate table content
        table = doc.tables[0]
        assert table.rows[0].cells[0].text == "Feature"
        assert table.rows[1].cells[2].text == "Full GFM"
    
    def test_task_lists(self):
        """Test task list support."""
        markdown_content = """
## Todo List

- [x] Implement basic converter
- [ ] Add GFM support  
- [x] Create tests
- [ ] Write documentation
"""
        
        doc = self.improved_converter.convert(markdown_content)
        
        # Check that checkboxes are rendered
        paragraphs = [p.text for p in doc.paragraphs]
        checkbox_paragraphs = [p for p in paragraphs if '☑' in p or '☐' in p]
        assert len(checkbox_paragraphs) >= 2
    
    def test_strikethrough(self):
        """Test strikethrough text support."""
        markdown_content = "This is ~~deleted~~ text and this is normal text."
        
        doc = self.improved_converter.convert(markdown_content)
        
        # Check for strikethrough formatting
        found_strike = False
        for para in doc.paragraphs:
            for run in para.runs:
                if run.font.strike:
                    found_strike = True
                    break
        assert found_strike
    
    def test_fenced_code_blocks(self):
        """Test fenced code blocks with language specification."""
        markdown_content = """
```python
def hello_world():
    print("Hello, World!")
    return True
```
"""
        
        doc = self.improved_converter.convert(markdown_content)
        
        # Check for code block
        code_paragraphs = [p for p in doc.paragraphs if any(run.font.name == 'Courier New' for run in p.runs)]
        assert len(code_paragraphs) > 0
    
    def test_emphasis_and_strong(self):
        """Test proper emphasis and strong emphasis handling."""
        markdown_content = """
This is *italic* text and this is **bold** text.
This is ***bold italic*** text.
This has *nested **bold** in italic* text.
"""
        
        doc = self.improved_converter.convert(markdown_content)
        
        # Check for formatting
        found_italic = False
        found_bold = False
        
        for para in doc.paragraphs:
            for run in para.runs:
                if run.italic:
                    found_italic = True
                if run.bold:
                    found_bold = True
                    
        assert found_italic and found_bold
    
    def test_headers_hierarchy(self):
        """Test proper header hierarchy."""
        markdown_content = """
# Main Title
## Section
### Subsection
#### Sub-subsection
##### Deep section
###### Deepest section
"""
        
        doc = self.improved_converter.convert(markdown_content)
        
        # Check for different heading levels
        heading_levels = []
        for para in doc.paragraphs:
            if para.style.name.startswith('Heading'):
                level = para.style.name.split()[-1]
                heading_levels.append(level)
        
        assert len(set(heading_levels)) >= 3  # At least 3 different heading levels
    
    def test_validation_function(self):
        """Test markdown validation functionality."""
        markdown_content = """
# Test Document

This has **bold** and *italic* text.

- [x] Task item
- [ ] Incomplete task

| Col1 | Col2 |
|------|------|
| A    | B    |

```python
print("code")
```
"""
        
        validation = self.improved_converter.validate_markdown(markdown_content)
        
        assert validation['valid'] is True
        features = validation['features_detected']
        
        assert features['tables'] is True
        assert features['code_blocks'] is True
        assert features['headers'] is True
        assert features['lists'] is True
        assert features['emphasis'] is True
        assert features['task_lists'] is True
    
    def test_complex_nested_formatting(self):
        """Test complex nested markdown formatting."""
        markdown_content = """
This paragraph contains *italic text with **bold inside** and more italic*.

Here's a list with formatting:
- *Italic item*
- **Bold item** 
- Item with `inline code`
- ~~Strikethrough item~~

And a table with formatting:

| **Bold Header** | *Italic Header* | `Code Header` |
|-----------------|-----------------|---------------|
| Normal text     | *Italic cell*   | `code cell`   |
| **Bold cell**   | ~~Strike cell~~ | Normal        |
"""
        
        doc = self.improved_converter.convert(markdown_content)
        
        # Should not crash and should produce a document
        assert len(doc.paragraphs) > 0
        assert len(doc.tables) > 0
    
    def test_autolinks_and_links(self):
        """Test autolink and regular link support."""
        markdown_content = """
Visit https://github.com for code.

Or check out [GitHub](https://github.com) manually.

Email me at test@example.com for questions.
"""
        
        doc = self.improved_converter.convert(markdown_content)
        
        # Check that links are processed (even if not as hyperlinks)
        text_content = ' '.join(p.text for p in doc.paragraphs)
        assert 'GitHub' in text_content
        assert 'github.com' in text_content
    
    def test_comparison_with_original(self):
        """Compare improved converter with original."""
        markdown_content = """
# Comparison Test

## Features

- [x] Basic formatting
- [ ] Advanced features

| Feature | Support |
|---------|---------|
| Tables  | Yes     |
| Tasks   | Yes     |

```python
def test():
    return "improved"
```

This has ~~strikethrough~~ and **bold** text.
"""
        
        # Both should work without errors
        improved_doc = self.improved_converter.convert(markdown_content)
        original_doc = self.original_converter.convert(markdown_content)
        
        # Improved should have more features
        assert len(improved_doc.paragraphs) >= len(original_doc.paragraphs)
        
        # Improved should handle tables better
        if len(improved_doc.tables) > 0 and len(original_doc.tables) > 0:
            improved_table = improved_doc.tables[0]
            original_table = original_doc.tables[0]
            
            # Both should have same structure but improved might have better formatting
            assert len(improved_table.rows) == len(original_table.rows)


if __name__ == "__main__":
    pytest.main([__file__])