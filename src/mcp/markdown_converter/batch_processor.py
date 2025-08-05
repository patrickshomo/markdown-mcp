"""Batch processing for multiple markdown files."""

from typing import List, Dict, Any, Optional
from pathlib import Path
from .simple_improved_converter import SimpleImprovedConverter as MarkdownConverter
import os


class BatchProcessor:
    """Handles batch conversion of multiple markdown files."""
    
    def __init__(self, template_dirs: Optional[List[str]] = None):
        self.converter = MarkdownConverter(template_dirs=template_dirs)
        
    def process_directory(
        self, 
        input_dir: str, 
        output_dir: str,
        template_name: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Process all markdown files in a directory."""
        input_path = Path(input_dir)
        output_path = Path(output_dir)
        
        if not input_path.exists():
            return {"error": f"Input directory not found: {input_dir}"}
            
        # Create output directory
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Find markdown files
        md_files = list(input_path.glob("*.md"))
        if not md_files:
            return {"error": "No markdown files found in directory"}
            
        results = []
        for md_file in md_files:
            try:
                # Read markdown content
                content = md_file.read_text(encoding='utf-8')
                
                # Convert to Word
                doc = self.converter.convert(content, metadata, template_name)
                
                # Save output
                output_file = output_path / f"{md_file.stem}.docx"
                doc.save(str(output_file))
                
                results.append({
                    "input": str(md_file),
                    "output": str(output_file),
                    "status": "success"
                })
                
            except Exception as e:
                results.append({
                    "input": str(md_file),
                    "output": None,
                    "status": "error",
                    "error": str(e)
                })
                
        return {
            "processed": len(results),
            "successful": len([r for r in results if r["status"] == "success"]),
            "failed": len([r for r in results if r["status"] == "error"]),
            "results": results
        }
    
    def process_files(
        self,
        file_paths: List[str],
        output_dir: str,
        template_name: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Process specific markdown files."""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        results = []
        for file_path in file_paths:
            try:
                md_file = Path(file_path)
                if not md_file.exists():
                    results.append({
                        "input": file_path,
                        "output": None,
                        "status": "error",
                        "error": "File not found"
                    })
                    continue
                    
                # Read and convert
                content = md_file.read_text(encoding='utf-8')
                doc = self.converter.convert(content, metadata, template_name)
                
                # Save output
                output_file = output_path / f"{md_file.stem}.docx"
                doc.save(str(output_file))
                
                results.append({
                    "input": file_path,
                    "output": str(output_file),
                    "status": "success"
                })
                
            except Exception as e:
                results.append({
                    "input": file_path,
                    "output": None,
                    "status": "error",
                    "error": str(e)
                })
                
        return {
            "processed": len(results),
            "successful": len([r for r in results if r["status"] == "success"]),
            "failed": len([r for r in results if r["status"] == "error"]),
            "results": results
        }