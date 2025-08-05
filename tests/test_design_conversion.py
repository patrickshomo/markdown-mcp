"""Test converting the design-input.md file to Word."""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.mcp.markdown_converter.converter import MarkdownConverter


def test_design_conversion():
    """Convert design-input.md to Word document."""
    # Read the design input file
    design_file = Path("../design/design-input.md")
    
    if not design_file.exists():
        print(f"Design file not found: {design_file}")
        return
        
    with open(design_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Set up metadata
    metadata = {
        "title": "Markdown to Word MCP Server Goals",
        "author": "Development Team",
        "subject": "Technical Design Document"
    }
    
    # Convert to Word
    converter = MarkdownConverter()
    doc = converter.convert(markdown_content, metadata)
    
    # Save output
    output_path = "design-input.docx"
    doc.save(output_path)
    print(f"Design document converted and saved as: {output_path}")


if __name__ == "__main__":
    test_design_conversion()