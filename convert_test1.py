#!/usr/bin/env python3
"""Convert test1.md using the improved converter."""

import sys
sys.path.append('src')

from src.mcp.markdown_converter.simple_improved_converter import SimpleImprovedConverter

def main():
    # Read test1.md
    with open('tests/input/test1.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert
    converter = SimpleImprovedConverter()
    doc = converter.convert(content, metadata={
        'title': 'Markdown Test Document',
        'author': 'Test Suite'
    })
    
    # Save
    output_path = 'tests/output/test1_improved.docx'
    doc.save(output_path)
    print(f"Converted test1.md → {output_path}")
    
    # Show stats
    print(f"Paragraphs: {len(doc.paragraphs)}")
    print(f"Tables: {len(doc.tables)}")

if __name__ == "__main__":
    main()