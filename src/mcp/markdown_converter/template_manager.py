"""Template management for DOTX templates."""

from typing import List, Dict, Optional
from pathlib import Path
from docx import Document
import os


class TemplateManager:
    """Manages DOTX template discovery and loading."""
    
    def __init__(self, template_dirs: Optional[List[str]] = None):
        self.template_dirs = template_dirs or []
        self.builtin_dir = Path(__file__).parent / "templates"
        
    def list_templates(self) -> List[Dict[str, str]]:
        """List all available templates."""
        templates = []
        
        # Built-in templates
        for template_path in self.builtin_dir.glob("*.dotx"):
            templates.append({
                "name": template_path.stem,
                "path": str(template_path),
                "type": "builtin"
            })
            
        # External templates
        for template_dir in self.template_dirs:
            if Path(template_dir).exists():
                for template_path in Path(template_dir).glob("*.dotx"):
                    templates.append({
                        "name": template_path.stem,
                        "path": str(template_path),
                        "type": "external"
                    })
                    
        return templates
    
    def get_template_path(self, template_name: str) -> Optional[str]:
        """Get path for named template."""
        templates = self.list_templates()
        for template in templates:
            if template["name"] == template_name:
                return template["path"]
        return None
    
    def validate_template(self, template_path: str) -> bool:
        """Validate template file exists and is readable."""
        try:
            path = Path(template_path)
            return path.exists() and path.suffix == ".dotx"
        except Exception:
            return False