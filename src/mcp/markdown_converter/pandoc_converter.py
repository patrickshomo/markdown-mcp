"""Pandoc-powered markdown to Word converter."""

import subprocess
import os
from pathlib import Path
from typing import Dict, Any, Optional
import pypandoc


class PandocConverter:
    """Clean Pandoc-based markdown to Word converter."""
    
    def __init__(self):
        self._ensure_pandoc()
    
    def _ensure_pandoc(self):
        """Ensure Pandoc is available."""
        try:
            subprocess.run(['pandoc', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            raise RuntimeError("Pandoc not found. Install with: brew install pandoc")
    
    def convert(self, markdown_content: str, output_path: str, 
                metadata: Optional[Dict[str, Any]] = None) -> str:
        """Convert markdown to Word document."""
        extra_args = ['--from=gfm', '--to=docx']
        
        if metadata:
            if 'title' in metadata:
                extra_args.extend(['-M', f'title={metadata["title"]}'])
            if 'author' in metadata:
                extra_args.extend(['-M', f'author={metadata["author"]}'])
        
        pypandoc.convert_text(
            markdown_content,
            'docx',
            format='gfm',
            outputfile=output_path,
            extra_args=extra_args
        )
        
        return output_path
    
    def validate_markdown(self, markdown_content: str) -> Dict[str, Any]:
        """Validate markdown and detect features."""
        features = []
        
        if '- [' in markdown_content:
            features.append('task_lists')
        if '|' in markdown_content and '---' in markdown_content:
            features.append('tables')
        if '~~' in markdown_content:
            features.append('strikethrough')
        if '```' in markdown_content:
            features.append('code_blocks')
        
        return {
            'valid': True,
            'features_detected': features,
            'converter': 'pandoc'
        }