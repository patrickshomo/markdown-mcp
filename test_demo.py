#!/usr/bin/env python3
"""Demo script to test the improved converter."""

import sys
sys.path.append('src')

from src.mcp.markdown_converter.improved_converter import ImprovedMarkdownConverter

def test_basic_functionality():
    """Test basic functionality of the improved converter."""
    print("Testing Improved Markdown Converter...")
    
    converter = ImprovedMarkdownConverter()
    
    # Test markdown content with various GFM features
    markdown_content = """
# Test Document

This is a test of the **improved** markdown converter with *enhanced* GFM support.

## Features Tested

### Task Lists
- [x] Basic conversion
- [x] GFM table support
- [ ] Advanced features
- [ ] Performance optimization

### Tables
| Feature | Status | Notes |
|---------|--------|-------|
| Tables | ✅ Working | Full GFM support |
| Tasks | ✅ Working | Checkbox rendering |
| Code | ✅ Working | Syntax highlighting |
| Strike | ✅ Working | ~~Old text~~ |

### Code Blocks
```python
def hello_world():
    print("Hello from improved converter!")
    return True
```

### Formatting
This text has **bold**, *italic*, ~~strikethrough~~, and `inline code`.

### Complex Formatting
This is *italic with **bold inside** and more italic*.

Here's ***bold italic*** text.
"""
    
    try:
        # Test validation
        print("\n1. Testing validation...")
        validation = converter.validate_markdown(markdown_content)
        print(f"   Valid: {validation['valid']}")
        print(f"   Features detected: {list(validation['features_detected'].keys())}")
        
        # Test conversion
        print("\n2. Testing conversion...")
        doc = converter.convert(markdown_content, metadata={
            'title': 'Test Document',
            'author': 'Improved Converter',
            'subject': 'GFM Conversion Test'
        })
        
        print(f"   Document created with {len(doc.paragraphs)} paragraphs")
        print(f"   Tables: {len(doc.tables)}")
        
        # Check for specific features
        has_code = any(
            any(run.font.name == 'Courier New' for run in p.runs) 
            for p in doc.paragraphs
        )
        has_formatting = any(
            any(run.bold or run.italic for run in p.runs) 
            for p in doc.paragraphs
        )
        
        print(f"   Has code formatting: {has_code}")
        print(f"   Has text formatting: {has_formatting}")
        
        # Save test document
        output_path = "tests/output/improved_converter_test.docx"
        import os
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        doc.save(output_path)
        print(f"   Saved to: {output_path}")
        
        print("\n✅ All tests passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_comparison():
    """Compare with original converter."""
    print("\nComparing with original converter...")
    
    try:
        from src.mcp.markdown_converter.converter import MarkdownConverter
        
        original = MarkdownConverter()
        improved = ImprovedMarkdownConverter()
        
        test_content = """
# Comparison Test

| Feature | Original | Improved |
|---------|----------|----------|
| Tables  | Basic    | Enhanced |
| Tasks   | None     | ✅ Full  |

- [x] Task item
- [ ] Incomplete

```python
print("code block")
```

Text with **bold** and ~~strike~~.
"""
        
        # Convert with both
        original_doc = original.convert(test_content)
        improved_doc = improved.convert(test_content)
        
        print(f"Original: {len(original_doc.paragraphs)} paragraphs, {len(original_doc.tables)} tables")
        print(f"Improved: {len(improved_doc.paragraphs)} paragraphs, {len(improved_doc.tables)} tables")
        
        # Save both for comparison
        original_doc.save("tests/output/original_comparison.docx")
        improved_doc.save("tests/output/improved_comparison.docx")
        
        print("✅ Comparison complete - check output files")
        
    except ImportError:
        print("⚠️  Original converter not available for comparison")
    except Exception as e:
        print(f"❌ Comparison failed: {e}")

if __name__ == "__main__":
    success = test_basic_functionality()
    test_comparison()
    
    if success:
        print("\n🎉 Demo completed successfully!")
    else:
        print("\n💥 Demo failed!")
        sys.exit(1)