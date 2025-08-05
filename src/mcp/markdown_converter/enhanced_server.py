"""Enhanced MCP server with improved GFM-compliant markdown conversion."""

from fastmcp import FastMCP
from typing import Optional, Dict, Any, List
from pathlib import Path
import tempfile
import os

from .simple_improved_converter import SimpleImprovedConverter as ImprovedMarkdownConverter
from .template_manager import TemplateManager
from .batch_processor import BatchProcessor

# Initialize MCP server
mcp = FastMCP("Enhanced Markdown Converter")

# Global converter instance
converter = None
template_manager = None
batch_processor = None

def get_converter():
    """Get or create converter instance."""
    global converter
    if converter is None:
        converter = ImprovedMarkdownConverter()
    return converter

def get_template_manager():
    """Get or create template manager instance."""
    global template_manager
    if template_manager is None:
        template_manager = TemplateManager()
    return template_manager

def get_batch_processor():
    """Get or create batch processor instance."""
    global batch_processor
    if batch_processor is None:
        batch_processor = BatchProcessor()
    return batch_processor


@mcp.tool()  # MCP_FUNCTION
def convert_markdown_to_docx(
    markdown_content: str,
    output_path: Optional[str] = None,
    template_name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Convert markdown content to Word document with enhanced GFM support.
    
    This enhanced version provides full GitHub Flavored Markdown support including:
    - Tables with proper formatting
    - Task lists with checkboxes
    - Strikethrough text
    - Fenced code blocks with language detection
    - Proper emphasis and strong emphasis
    - Autolinks and reference links
    - Enhanced inline formatting
    
    Args:
        markdown_content: The markdown text to convert
        output_path: Optional path to save the document
        template_name: Optional template to use (simple, corporate, technical)
        metadata: Optional document metadata (title, author, subject, etc.)
    
    Returns:
        Dictionary with conversion results and document info
    """
    try:
        conv = get_converter()
        
        # Convert markdown to document
        doc = conv.convert(
            markdown_content=markdown_content,
            metadata=metadata or {},
            template_name=template_name
        )
        
        # Save document
        if output_path:
            save_path = Path(output_path)
        else:
            # Create temporary file
            temp_dir = Path(tempfile.gettempdir()) / "markdown_converter"
            temp_dir.mkdir(exist_ok=True)
            save_path = temp_dir / "converted_document.docx"
        
        # Ensure parent directory exists
        save_path.parent.mkdir(parents=True, exist_ok=True)
        doc.save(str(save_path))
        
        # Get document statistics
        stats = {
            'paragraphs': len(doc.paragraphs),
            'tables': len(doc.tables),
            'sections': len(doc.sections),
            'has_headers': any('Heading' in p.style.name for p in doc.paragraphs),
            'has_code_blocks': any(
                any(run.font.name == 'Courier New' for run in p.runs) 
                for p in doc.paragraphs
            ),
            'has_formatting': any(
                any(run.bold or run.italic for run in p.runs) 
                for p in doc.paragraphs
            )
        }
        
        return {
            "success": True,
            "output_path": str(save_path),
            "file_size": save_path.stat().st_size,
            "template_used": template_name or "default",
            "document_stats": stats,
            "message": f"Successfully converted markdown to Word document with enhanced GFM support"
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to convert markdown to Word document"
        }


@mcp.tool()  # MCP_FUNCTION
def validate_markdown_compatibility(markdown_content: str) -> Dict[str, Any]:
    """
    Validate markdown content for conversion compatibility and feature detection.
    
    This function analyzes the markdown content and reports:
    - Whether the content can be successfully parsed
    - Which GFM features are detected
    - Potential conversion issues
    - HTML preview of parsed content
    
    Args:
        markdown_content: The markdown text to validate
    
    Returns:
        Dictionary with validation results and feature analysis
    """
    try:
        conv = get_converter()
        validation_result = conv.validate_markdown(markdown_content)
        
        # Add additional analysis
        lines = markdown_content.split('\n')
        analysis = {
            'line_count': len(lines),
            'character_count': len(markdown_content),
            'word_count': len(markdown_content.split()),
            'has_metadata': markdown_content.strip().startswith('---'),
            'complexity_score': _calculate_complexity_score(markdown_content)
        }
        
        validation_result['content_analysis'] = analysis
        
        return validation_result
        
    except Exception as e:
        return {
            "valid": False,
            "error": str(e),
            "features_detected": {},
            "content_analysis": {},
            "html_preview": ""
        }


@mcp.tool()  # MCP_FUNCTION
def list_available_templates() -> Dict[str, Any]:
    """
    List all available Word document templates.
    
    Returns information about available templates including:
    - Template names and descriptions
    - Template file paths
    - Template validation status
    
    Returns:
        Dictionary with template information
    """
    try:
        tm = get_template_manager()
        templates = tm.list_templates()
        
        template_info = {}
        for name, path in templates.items():
            template_info[name] = {
                'path': str(path),
                'exists': path.exists() if path else False,
                'valid': tm.validate_template(str(path)) if path and path.exists() else False,
                'size': path.stat().st_size if path and path.exists() else 0
            }
        
        return {
            "success": True,
            "templates": template_info,
            "template_count": len(templates),
            "message": f"Found {len(templates)} available templates"
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "templates": {},
            "message": "Failed to list templates"
        }


@mcp.tool()  # MCP_FUNCTION
def batch_convert_directory(
    input_directory: str,
    output_directory: Optional[str] = None,
    template_name: Optional[str] = None,
    file_pattern: str = "*.md"
) -> Dict[str, Any]:
    """
    Convert all markdown files in a directory to Word documents.
    
    Args:
        input_directory: Directory containing markdown files
        output_directory: Directory to save converted documents (optional)
        template_name: Template to use for all conversions (optional)
        file_pattern: File pattern to match (default: "*.md")
    
    Returns:
        Dictionary with batch conversion results
    """
    try:
        bp = get_batch_processor()
        conv = get_converter()
        
        input_path = Path(input_directory)
        if not input_path.exists():
            return {
                "success": False,
                "error": f"Input directory does not exist: {input_directory}",
                "results": []
            }
        
        # Set output directory
        if output_directory:
            output_path = Path(output_directory)
        else:
            output_path = input_path / "converted"
        
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Find markdown files
        markdown_files = list(input_path.glob(file_pattern))
        
        if not markdown_files:
            return {
                "success": True,
                "message": f"No files found matching pattern '{file_pattern}'",
                "results": [],
                "files_processed": 0
            }
        
        # Process files
        results = []
        successful_conversions = 0
        
        for md_file in markdown_files:
            try:
                # Read markdown content
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Convert to Word
                doc = conv.convert(
                    markdown_content=content,
                    template_name=template_name
                )
                
                # Save document
                output_file = output_path / f"{md_file.stem}.docx"
                doc.save(str(output_file))
                
                results.append({
                    "input_file": str(md_file),
                    "output_file": str(output_file),
                    "success": True,
                    "file_size": output_file.stat().st_size
                })
                successful_conversions += 1
                
            except Exception as e:
                results.append({
                    "input_file": str(md_file),
                    "output_file": None,
                    "success": False,
                    "error": str(e)
                })
        
        return {
            "success": True,
            "files_processed": len(markdown_files),
            "successful_conversions": successful_conversions,
            "failed_conversions": len(markdown_files) - successful_conversions,
            "output_directory": str(output_path),
            "results": results,
            "message": f"Processed {len(markdown_files)} files, {successful_conversions} successful"
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "results": [],
            "message": "Batch conversion failed"
        }


@mcp.tool()  # MCP_FUNCTION
def get_conversion_features() -> Dict[str, Any]:
    """
    Get information about supported markdown features and conversion capabilities.
    
    Returns:
        Dictionary with feature information and examples
    """
    return {
        "gfm_features": {
            "tables": {
                "supported": True,
                "description": "GitHub Flavored Markdown tables with alignment",
                "example": "| Header 1 | Header 2 |\\n|----------|----------|\\n| Cell 1   | Cell 2   |"
            },
            "task_lists": {
                "supported": True,
                "description": "Task lists with checkboxes",
                "example": "- [x] Completed task\\n- [ ] Incomplete task"
            },
            "strikethrough": {
                "supported": True,
                "description": "Strikethrough text formatting",
                "example": "~~deleted text~~"
            },
            "fenced_code_blocks": {
                "supported": True,
                "description": "Code blocks with language specification",
                "example": "```python\\nprint('Hello World')\\n```"
            },
            "autolinks": {
                "supported": True,
                "description": "Automatic link detection",
                "example": "https://github.com or <https://github.com>"
            },
            "emphasis": {
                "supported": True,
                "description": "Proper emphasis and strong emphasis",
                "example": "*italic* **bold** ***bold italic***"
            }
        },
        "word_features": {
            "templates": {
                "supported": True,
                "description": "Custom Word document templates",
                "available": ["simple", "corporate", "technical"]
            },
            "metadata": {
                "supported": True,
                "description": "Document properties and metadata",
                "fields": ["title", "author", "subject", "keywords", "comments"]
            },
            "formatting": {
                "supported": True,
                "description": "Rich text formatting preservation",
                "features": ["bold", "italic", "strikethrough", "code", "headers", "lists"]
            },
            "images": {
                "supported": True,
                "description": "Image embedding and processing",
                "formats": ["png", "jpg", "jpeg", "gif"]
            },
            "diagrams": {
                "supported": True,
                "description": "Mermaid diagram conversion",
                "types": ["flowchart", "sequence", "gantt", "pie"]
            }
        },
        "conversion_options": {
            "batch_processing": True,
            "validation": True,
            "error_handling": True,
            "progress_tracking": True
        }
    }


def _calculate_complexity_score(markdown_content: str) -> int:
    """Calculate a complexity score for markdown content."""
    score = 0
    
    # Basic content
    score += len(markdown_content.split()) // 100  # Word count factor
    
    # Features
    if '|' in markdown_content:  # Tables
        score += 2
    if '```' in markdown_content:  # Code blocks
        score += 2
    if '- [' in markdown_content or '* [' in markdown_content:  # Task lists
        score += 1
    if '~~' in markdown_content:  # Strikethrough
        score += 1
    if '![' in markdown_content:  # Images
        score += 2
    if 'mermaid' in markdown_content.lower():  # Diagrams
        score += 3
    
    # Headers
    score += markdown_content.count('#') // 2
    
    # Links
    score += markdown_content.count('[') // 3
    
    return min(score, 10)  # Cap at 10


if __name__ == "__main__":
    mcp.run()