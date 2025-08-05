#!/usr/bin/env python3
"""Test individual file conversion."""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.mcp.markdown_converter.simple_improved_converter import SimpleImprovedConverter


def test_individual_conversion():
    """Test converting individual markdown files."""
    converter = SimpleImprovedConverter()
    input_dir = Path("tests/input")
    output_dir = Path("tests/output")
    
    for md_file in input_dir.glob("*.md"):
        print(f"Converting {md_file.name}...")
        
        content = md_file.read_text(encoding='utf-8')
        doc = converter.convert(content)
        
        output_file = output_dir / f"{md_file.stem}.docx"
        doc.save(str(output_file))
        print(f"  → {output_file}")


def test_individual_with_metadata():
    """Test converting with metadata."""
    converter = SimpleImprovedConverter()
    input_dir = Path("tests/input")
    output_dir = Path("tests/output")
    
    for md_file in input_dir.glob("*.md"):
        print(f"Converting {md_file.name} with metadata...")
        
        content = md_file.read_text(encoding='utf-8')
        metadata = {
            "title": f"{md_file.stem.title()} Document",
            "author": "Test Suite",
            "subject": "Markdown Conversion Test"
        }
        
        doc = converter.convert(content, metadata)
        
        output_file = output_dir / f"{md_file.stem}_with_metadata.docx"
        doc.save(str(output_file))
        print(f"  → {output_file}")


if __name__ == "__main__":
    test_individual_conversion()
    test_individual_with_metadata()