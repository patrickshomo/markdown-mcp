"""Image handling for markdown conversion."""

from typing import Optional
from pathlib import Path
from docx import Document
from docx.shared import Inches
import re
import requests
import tempfile
import os


class ImageHandler:
    """Handles image embedding in Word documents."""
    
    def __init__(self, base_path: Optional[str] = None):
        self.base_path = Path(base_path) if base_path else Path.cwd()
        
    def process_images(self, doc: Document, content: str) -> str:
        """Process and embed images from markdown content."""
        # Find all image references
        image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        matches = re.findall(image_pattern, content)
        
        processed_content = content
        for alt_text, image_path in matches:
            try:
                # Add image to document
                self._add_image_to_doc(doc, image_path, alt_text)
                # Remove image markdown from content
                image_markdown = f'![{alt_text}]({image_path})'
                processed_content = processed_content.replace(image_markdown, f'[Image: {alt_text}]')
            except Exception as e:
                # Replace with error message
                image_markdown = f'![{alt_text}]({image_path})'
                processed_content = processed_content.replace(image_markdown, f'[Image Error: {alt_text}]')
                
        return processed_content
    
    def _add_image_to_doc(self, doc: Document, image_path: str, alt_text: str):
        """Add image to Word document."""
        if image_path.startswith(('http://', 'https://')):
            # Download remote image
            temp_path = self._download_image(image_path)
            if temp_path:
                doc.add_picture(temp_path, width=Inches(4))
                os.unlink(temp_path)
        else:
            # Local image
            full_path = self.base_path / image_path
            if full_path.exists():
                doc.add_picture(str(full_path), width=Inches(4))
    
    def _download_image(self, url: str) -> Optional[str]:
        """Download image from URL to temp file."""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp:
                tmp.write(response.content)
                return tmp.name
        except Exception:
            return None