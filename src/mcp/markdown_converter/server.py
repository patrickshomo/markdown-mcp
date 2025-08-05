"""FastMCP server for markdown to Word conversion."""

from typing import Optional, Dict, Any, List
from pathlib import Path
import tempfile
import os

from fastmcp import FastMCP
from .converter import MarkdownConverter
from .template_manager import TemplateManager
from .batch_processor import BatchProcessor


# Initialize MCP server
mcp = FastMCP("Markdown to Word Converter")

# Initialize components
template_manager = TemplateManager()
batch_processor = BatchProcessor()


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
        # Initialize converter
        converter = MarkdownConverter()
        
        # Convert markdown to document
        doc = converter.convert(markdown_content, metadata, template_name)
        
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
def list_available_templates() -> List[Dict[str, str]]:
    """
    List all available Word templates.
    
    Returns:
        List of template dictionaries with name, path, and type
    """
    return template_manager.list_templates()


@mcp.tool()  # MCP_FUNCTION
def batch_convert_directory(
    input_dir: str,
    output_dir: str,
    template_name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Convert all markdown files in a directory to Word documents.
    
    Args:
        input_dir: Directory containing markdown files
        output_dir: Directory to save Word documents
        template_name: Optional template name
        metadata: Optional document metadata
        
    Returns:
        Batch processing results
    """
    return batch_processor.process_directory(input_dir, output_dir, template_name, metadata)


@mcp.tool()  # MCP_FUNCTION
def batch_convert_files(
    file_paths: List[str],
    output_dir: str,
    template_name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Convert specific markdown files to Word documents.
    
    Args:
        file_paths: List of markdown file paths
        output_dir: Directory to save Word documents
        template_name: Optional template name
        metadata: Optional document metadata
        
    Returns:
        Batch processing results
    """
    return batch_processor.process_files(file_paths, output_dir, template_name, metadata)


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