"""Mermaid diagram handling for markdown conversion."""

from typing import Optional
from pathlib import Path
from docx import Document
from docx.shared import Inches
import re
import subprocess
import tempfile
import os


class MermaidHandler:
    """Handles Mermaid diagram conversion to images."""
    
    def __init__(self):
        self.mermaid_available = self._check_mermaid_cli()
        
    def process_mermaid(self, doc: Document, content: str) -> str:
        """Process and convert Mermaid diagrams to images."""
        # Find mermaid code blocks
        mermaid_pattern = r'```mermaid\n(.*?)\n```'
        matches = re.findall(mermaid_pattern, content, re.DOTALL)
        
        if not matches:
            return content
            
        processed_content = content
        
        if not self.mermaid_available:
            # Replace with placeholder when CLI not available
            for mermaid_code in matches:
                mermaid_block = f'```mermaid\n{mermaid_code}\n```'
                processed_content = processed_content.replace(mermaid_block, '[Mermaid Diagram - CLI not available]')
            return processed_content
        
        for i, mermaid_code in enumerate(matches):
            try:
                # Convert mermaid to image
                image_path = self._render_mermaid(mermaid_code, f"diagram_{i}")
                if image_path:
                    doc.add_picture(image_path, width=Inches(5))
                    os.unlink(image_path)
                    
                # Remove mermaid block from content
                mermaid_block = f'```mermaid\n{mermaid_code}\n```'
                processed_content = processed_content.replace(mermaid_block, '[Mermaid Diagram]')
            except Exception:
                # Replace with error message
                mermaid_block = f'```mermaid\n{mermaid_code}\n```'
                processed_content = processed_content.replace(mermaid_block, '[Mermaid Diagram - Render Error]')
                
        return processed_content
    
    def _check_mermaid_cli(self) -> bool:
        """Check if Mermaid CLI is available."""
        try:
            subprocess.run(['mmdc', '--version'], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def _render_mermaid(self, mermaid_code: str, filename: str) -> Optional[str]:
        """Render Mermaid diagram to PNG image."""
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.mmd', delete=False) as mmd_file:
                mmd_file.write(mermaid_code)
                mmd_path = mmd_file.name
                
            png_path = mmd_path.replace('.mmd', '.png')
            
            subprocess.run([
                'mmdc', '-i', mmd_path, '-o', png_path,
                '--backgroundColor', 'white'
            ], check=True, capture_output=True)
            
            os.unlink(mmd_path)
            return png_path if Path(png_path).exists() else None
            
        except Exception:
            return None