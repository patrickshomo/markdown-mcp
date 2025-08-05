"""FastMCP server for markdown to Word conversion."""

from typing import Optional, Dict, Any
from pathlib import Path
import tempfile
import os

from fastmcp import FastMCP
from converter import MarkdownConverter


# Initialize MCP server
mcp = FastMCP("Markdown to Word Converter")

# Template directory
TEMPLATE_DIR = Path(__file__).parent / "templates"


@mcp.tool()  # MCP_FUNCTION
def convert_markdown_to_docx(
    markdown_content: str,
    template_name: Optional[str] = None,
    output_path: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> str:
    """
    Convert markdown content to a Word document.
    
    Args:
        markdown_content: The markdown text to convert
        template_name: Optional template name (simple, corporate, technical)
        output_path: Optional output file path, defaults to temp file
        metadata: Optional document metadata (title, author, subject, keywords, comments)
    
    Returns:
        Path to the generated Word document
    """
    try:
        # Get template path if specified
        template_path = None
        if template_name:
            template_path = str(TEMPLATE_DIR / f"{template_name}.docx")
            
        # Initialize converter
        converter = MarkdownConverter(template_path)
        
        # Convert markdown to document
        doc = converter.convert(markdown_content, metadata)
        
        # Determine output path
        if not output_path:
            temp_file = tempfile.NamedTemporaryFile(suffix='.docx', delete=False)
            output_path = temp_file.name
            temp_file.close()
            
        # Save document
        doc.save(output_path)
        
        return f"Document saved to: {output_path}"
        
    except Exception as e:
        return f"Error converting markdown: {str(e)}"


@mcp.tool()  # MCP_FUNCTION
def list_available_templates() -> str:
    """
    List all available Word templates.
    
    Returns:
        List of available template names
    """
    try:
        if not TEMPLATE_DIR.exists():
            return "No templates directory found"
            
        templates = [f.stem for f in TEMPLATE_DIR.glob("*.docx")]
        
        if not templates:
            return "No templates available"
            
        return f"Available templates: {', '.join(templates)}"
        
    except Exception as e:
        return f"Error listing templates: {str(e)}"


@mcp.tool()  # MCP_FUNCTION
def validate_markdown(markdown_content: str) -> str:
    """
    Validate markdown content for conversion compatibility.
    
    Args:
        markdown_content: The markdown text to validate
        
    Returns:
        Validation results and warnings
    """
    try:
        issues = []
        lines = markdown_content.split('\n')
        
        # Check for unsupported features
        for i, line in enumerate(lines, 1):
            if line.strip().startswith('![') and '](' in line:
                issues.append(f"Line {i}: Image embedding not yet supported")
            if '```mermaid' in line:
                issues.append(f"Line {i}: Mermaid diagrams not yet supported")
                
        if not issues:
            return "Markdown content is valid for conversion"
        else:
            return f"Validation warnings:\n" + "\n".join(issues)
            
    except Exception as e:
        return f"Error validating markdown: {str(e)}"


if __name__ == "__main__":
    mcp.run()