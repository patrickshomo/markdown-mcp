#!/usr/bin/env python3
"""Convert test1.md with debug info."""

import sys
sys.path.append('src')

from src.mcp.markdown_converter.simple_improved_converter import SimpleImprovedConverter

def main():
    with open('tests/input/test1.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    converter = SimpleImprovedConverter()
    
    # Validate first
    validation = converter.validate_markdown(content)
    print(f"Valid: {validation['valid']}")
    if validation['valid']:
        features = [k for k, v in validation['features_detected'].items() if v]
        print(f"Features: {features}")
    
    # Convert with better error handling
    try:
        doc = converter.convert(content)
        doc.save('tests/output/test1_improved_debug.docx')
        print(f"Success: {len(doc.paragraphs)} paragraphs, {len(doc.tables)} tables")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()