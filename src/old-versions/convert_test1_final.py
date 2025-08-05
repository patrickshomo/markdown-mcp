#!/usr/bin/env python3
"""Convert test1.md with robust handling."""

import sys
sys.path.append('src')

from src.mcp.markdown_converter.converter import MarkdownConverter

def main():
    with open('tests/input/test1.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use original converter for comparison
    converter = MarkdownConverter()
    doc = converter.convert(content, metadata={
        'title': 'Test1 Document',
        'author': 'Converter Test'
    })
    
    doc.save('tests/output/test1_converted.docx')
    print(f"✅ Converted test1.md successfully")
    print(f"📄 Paragraphs: {len(doc.paragraphs)}")
    print(f"📊 Tables: {len(doc.tables)}")
    print(f"💾 Saved to: tests/output/test1_converted.docx")

if __name__ == "__main__":
    main()