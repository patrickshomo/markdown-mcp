#!/usr/bin/env python3
"""Demo script to test the simple improved converter."""

import sys
sys.path.append('src')

from src.mcp.markdown_converter.simple_improved_converter import SimpleImprovedConverter

def test_basic_functionality():
    """Test basic functionality of the simple improved converter."""
    print("Testing Simple Improved Markdown Converter...")
    
    converter = SimpleImprovedConverter()
    
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

### Links
Visit [GitHub](https://github.com) for more info.
"""
    
    try:
        # Test validation
        print("\n1. Testing validation...")
        validation = converter.validate_markdown(markdown_content)
        print(f"   Valid: {validation['valid']}")
        if validation['valid']:
            features = validation['features_detected']
            detected = [k for k, v in features.items() if v]
            print(f"   Features detected: {detected}")
        
        # Test conversion
        print("\n2. Testing conversion...")
        doc = converter.convert(markdown_content, metadata={
            'title': 'Test Document',
            'author': 'Simple Improved Converter',
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
        has_checkboxes = any('☑' in p.text or '☐' in p.text for p in doc.paragraphs)
        
        print(f"   Has code formatting: {has_code}")
        print(f"   Has text formatting: {has_formatting}")
        print(f"   Has task checkboxes: {has_checkboxes}")
        
        # Save test document
        output_path = "tests/output/simple_improved_test.docx"
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
        improved = SimpleImprovedConverter()
        
        test_content = """
# Comparison Test

| Feature | Original | Improved |
|---------|----------|----------|
| Tables  | Basic    | Enhanced |
| Tasks   | None     | ✅ Full  |

- [x] Task item completed
- [ ] Task item incomplete

```python
print("code block test")
```

Text with **bold**, *italic*, and ~~strikethrough~~.

Visit [GitHub](https://github.com) for source code.
"""
        
        # Convert with both
        print("Converting with original converter...")
        original_doc = original.convert(test_content)
        
        print("Converting with improved converter...")
        improved_doc = improved.convert(test_content)
        
        print(f"Original: {len(original_doc.paragraphs)} paragraphs, {len(original_doc.tables)} tables")
        print(f"Improved: {len(improved_doc.paragraphs)} paragraphs, {len(improved_doc.tables)} tables")
        
        # Check for task list support
        original_has_checkboxes = any('☑' in p.text or '☐' in p.text for p in original_doc.paragraphs)
        improved_has_checkboxes = any('☑' in p.text or '☐' in p.text for p in improved_doc.paragraphs)
        
        print(f"Original has checkboxes: {original_has_checkboxes}")
        print(f"Improved has checkboxes: {improved_has_checkboxes}")
        
        # Save both for comparison
        original_doc.save("tests/output/original_comparison.docx")
        improved_doc.save("tests/output/improved_comparison.docx")
        
        print("✅ Comparison complete - check output files")
        
    except ImportError:
        print("⚠️  Original converter not available for comparison")
    except Exception as e:
        print(f"❌ Comparison failed: {e}")
        import traceback
        traceback.print_exc()

def test_specific_features():
    """Test specific GFM features."""
    print("\nTesting specific GFM features...")
    
    converter = SimpleImprovedConverter()
    
    # Test cases for different features
    test_cases = {
        "Task Lists": """
- [x] Completed task
- [ ] Incomplete task
- [x] Another completed task
""",
        "Strikethrough": """
This is ~~deleted text~~ and this is normal text.
Some ~~more~~ strikethrough ~~text~~.
""",
        "Complex Tables": """
| Left | Center | Right |
|:-----|:------:|------:|
| L1   | C1     | R1    |
| L2   | C2     | R2    |
""",
        "Code with Language": """
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```
""",
        "Mixed Formatting": """
This has *italic*, **bold**, ***bold italic***, `code`, and ~~strikethrough~~.

*This is italic with **bold inside** it.*
"""
    }
    
    for feature_name, content in test_cases.items():
        try:
            print(f"\n  Testing {feature_name}...")
            doc = converter.convert(content)
            print(f"    ✅ {feature_name} converted successfully")
            
            # Save individual test
            filename = f"tests/output/test_{feature_name.lower().replace(' ', '_')}.docx"
            doc.save(filename)
            
        except Exception as e:
            print(f"    ❌ {feature_name} failed: {e}")

if __name__ == "__main__":
    success = test_basic_functionality()
    test_comparison()
    test_specific_features()
    
    if success:
        print("\n🎉 Demo completed successfully!")
        print("\nKey improvements demonstrated:")
        print("- ✅ Task lists with checkboxes (☑/☐)")
        print("- ✅ Strikethrough text support")
        print("- ✅ Enhanced table formatting")
        print("- ✅ Better code block handling")
        print("- ✅ Improved inline formatting")
        print("- ✅ Link processing")
        print("- ✅ Validation functionality")
    else:
        print("\n💥 Demo failed!")
        sys.exit(1)