"""FastMCP server for Pandoc markdown conversion."""

import os
from pathlib import Path
from typing import Dict, Any, Optional

from fastmcp import FastMCP
from .pandoc_converter import PandocConverter

# Initialize MCP server
mcp = FastMCP("Pandoc Markdown Converter")
converter = PandocConverter()


@mcp.tool()  # MCP_FUNCTION
def convert_markdown_to_docx(
    markdown_content: str,
    output_filename: str = "output.docx",
    title: Optional[str] = None,
    author: Optional[str] = None
) -> Dict[str, Any]:
    """Convert markdown to Word document using Pandoc.
    
    Args:
        markdown_content: The markdown text to convert
        output_filename: Name for the output file
        title: Document title (optional)
        author: Document author (optional)
    
    Returns:
        Dict with conversion results and file path
    """
    try:
        metadata = {}
        if title:
            metadata['title'] = title
        if author:
            metadata['author'] = author
        
        output_path = converter.convert(markdown_content, output_filename, metadata)
        
        return {
            'success': True,
            'output_file': output_path,
            'message': f'Successfully converted markdown to {output_filename}',
            'converter': 'pandoc'
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'message': 'Conversion failed'
        }


@mcp.tool()  # MCP_FUNCTION
def validate_markdown_compatibility(markdown_content: str) -> Dict[str, Any]:
    """Validate markdown and detect supported features.
    
    Args:
        markdown_content: The markdown text to validate
    
    Returns:
        Dict with validation results and detected features
    """
    return converter.validate_markdown(markdown_content)


@mcp.tool()  # MCP_FUNCTION
def batch_convert_directory(
    input_directory: str,
    output_directory: str = "converted_docs",
    file_pattern: str = "*.md"
) -> Dict[str, Any]:
    """Convert all markdown files in a directory.
    
    Args:
        input_directory: Directory containing markdown files
        output_directory: Directory for converted files
        file_pattern: File pattern to match (default: *.md)
    
    Returns:
        Dict with batch conversion results
    """
    try:
        input_path = Path(input_directory)
        output_path = Path(output_directory)
        output_path.mkdir(exist_ok=True)
        
        converted_files = []
        
        for md_file in input_path.glob(file_pattern):
            output_file = output_path / f"{md_file.stem}.docx"
            
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            converter.convert(content, str(output_file))
            converted_files.append(str(output_file))
        
        return {
            'success': True,
            'converted_files': converted_files,
            'count': len(converted_files),
            'message': f'Successfully converted {len(converted_files)} files'
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'message': 'Batch conversion failed'
        }


@mcp.tool()  # MCP_FUNCTION
def get_conversion_features() -> Dict[str, Any]:
    """Get supported conversion features and capabilities.
    
    Returns:
        Dict with supported features and converter info
    """
    return {
        'converter': 'pandoc',
        'supported_features': [
            'GitHub Flavored Markdown (GFM)',
            'Task lists (checkboxes)',
            'Tables with alignment',
            'Strikethrough text',
            'Fenced code blocks',
            'Syntax highlighting info',
            'Complex emphasis',
            'Links and images',
            'Blockquotes',
            'Lists (ordered/unordered)',
            'Headers (H1-H6)',
            'Horizontal rules'
        ],
        'input_format': 'gfm',
        'output_format': 'docx',
        'metadata_support': ['title', 'author'],
        'batch_processing': True
    }


if __name__ == "__main__":
    mcp.run()