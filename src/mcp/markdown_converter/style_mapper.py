"""Style mapping between Markdown elements and MS Word styles."""

from typing import Dict, Optional, Any
from enum import Enum


class MarkdownElement(Enum):
    """Enumeration of supported Markdown elements."""
    # Headers
    H1 = "h1"
    H2 = "h2" 
    H3 = "h3"
    H4 = "h4"
    H5 = "h5"
    H6 = "h6"
    
    # Text formatting
    PARAGRAPH = "p"
    EMPHASIS = "em"
    STRONG = "strong"
    CODE_INLINE = "code"
    STRIKETHROUGH = "del"
    
    # Block elements
    BLOCKQUOTE = "blockquote"
    CODE_BLOCK = "pre"
    HORIZONTAL_RULE = "hr"
    
    # Lists
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"
    LIST_ITEM = "li"
    TASK_LIST_CHECKED = "task_checked"
    TASK_LIST_UNCHECKED = "task_unchecked"
    
    # Tables
    TABLE = "table"
    TABLE_HEADER = "th"
    TABLE_CELL = "td"
    
    # Links and images
    LINK = "a"
    IMAGE = "img"


class WordStyle:
    """Word style definition with properties."""
    
    def __init__(self, name: str, font_name: Optional[str] = None, 
                 font_size: Optional[int] = None, bold: Optional[bool] = None,
                 italic: Optional[bool] = None, underline: Optional[bool] = None,
                 color: Optional[str] = None, background_color: Optional[str] = None,
                 paragraph_style: Optional[str] = None):
        self.name = name
        self.font_name = font_name
        self.font_size = font_size
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.color = color
        self.background_color = background_color
        self.paragraph_style = paragraph_style


class StyleMapper:
    """Maps Markdown elements to MS Word styles."""
    
    def __init__(self):
        """Initialize the style mapper with default mappings."""
        self._style_map = self._create_default_mappings()
    
    def _create_default_mappings(self) -> Dict[MarkdownElement, WordStyle]:
        """Create default Markdown to Word style mappings."""
        return {
            # Headers - Map to Word's built-in heading styles
            MarkdownElement.H1: WordStyle("Heading 1", paragraph_style="Heading 1"),
            MarkdownElement.H2: WordStyle("Heading 2", paragraph_style="Heading 2"),
            MarkdownElement.H3: WordStyle("Heading 3", paragraph_style="Heading 3"),
            MarkdownElement.H4: WordStyle("Heading 4", paragraph_style="Heading 4"),
            MarkdownElement.H5: WordStyle("Heading 5", paragraph_style="Heading 5"),
            MarkdownElement.H6: WordStyle("Heading 6", paragraph_style="Heading 6"),
            
            # Text formatting
            MarkdownElement.PARAGRAPH: WordStyle("Normal", paragraph_style="Normal"),
            MarkdownElement.EMPHASIS: WordStyle("Emphasis", italic=True),
            MarkdownElement.STRONG: WordStyle("Strong", bold=True),
            MarkdownElement.CODE_INLINE: WordStyle("Code Inline", 
                                                 font_name="Courier New",
                                                 background_color="light_gray"),
            MarkdownElement.STRIKETHROUGH: WordStyle("Strikethrough", underline=True),
            
            # Block elements
            MarkdownElement.BLOCKQUOTE: WordStyle("Quote", paragraph_style="Quote"),
            MarkdownElement.CODE_BLOCK: WordStyle("Code Block", 
                                                font_name="Courier New",
                                                font_size=10,
                                                background_color="light_gray",
                                                paragraph_style="No Spacing"),
            MarkdownElement.HORIZONTAL_RULE: WordStyle("Horizontal Rule", 
                                                     paragraph_style="Normal"),
            
            # Lists
            MarkdownElement.UNORDERED_LIST: WordStyle("List Bullet", 
                                                    paragraph_style="List Bullet"),
            MarkdownElement.ORDERED_LIST: WordStyle("List Number", 
                                                  paragraph_style="List Number"),
            MarkdownElement.LIST_ITEM: WordStyle("List Item", 
                                               paragraph_style="List Paragraph"),
            MarkdownElement.TASK_LIST_CHECKED: WordStyle("Task List Checked", 
                                                       paragraph_style="List Bullet"),
            MarkdownElement.TASK_LIST_UNCHECKED: WordStyle("Task List Unchecked", 
                                                         paragraph_style="List Bullet"),
            
            # Tables
            MarkdownElement.TABLE: WordStyle("Table", paragraph_style="Table Grid"),
            MarkdownElement.TABLE_HEADER: WordStyle("Table Header", 
                                                  bold=True,
                                                  background_color="light_blue"),
            MarkdownElement.TABLE_CELL: WordStyle("Table Cell", 
                                                paragraph_style="Normal"),
            
            # Links and images
            MarkdownElement.LINK: WordStyle("Hyperlink", 
                                          color="blue",
                                          underline=True),
            MarkdownElement.IMAGE: WordStyle("Image", paragraph_style="Normal"),
        }
    
    def get_word_style(self, markdown_element: MarkdownElement) -> Optional[WordStyle]:
        """Get the Word style for a given Markdown element."""
        return self._style_map.get(markdown_element)
    
    def get_word_style_name(self, markdown_element: MarkdownElement) -> Optional[str]:
        """Get the Word style name for a given Markdown element."""
        style = self.get_word_style(markdown_element)
        return style.name if style else None
    
    def get_paragraph_style_name(self, markdown_element: MarkdownElement) -> Optional[str]:
        """Get the Word paragraph style name for a given Markdown element."""
        style = self.get_word_style(markdown_element)
        return style.paragraph_style if style else None
    
    def map_html_tag_to_element(self, html_tag: str) -> Optional[MarkdownElement]:
        """Map HTML tag to Markdown element."""
        tag_mapping = {
            'h1': MarkdownElement.H1,
            'h2': MarkdownElement.H2,
            'h3': MarkdownElement.H3,
            'h4': MarkdownElement.H4,
            'h5': MarkdownElement.H5,
            'h6': MarkdownElement.H6,
            'p': MarkdownElement.PARAGRAPH,
            'em': MarkdownElement.EMPHASIS,
            'i': MarkdownElement.EMPHASIS,
            'strong': MarkdownElement.STRONG,
            'b': MarkdownElement.STRONG,
            'code': MarkdownElement.CODE_INLINE,
            'del': MarkdownElement.STRIKETHROUGH,
            's': MarkdownElement.STRIKETHROUGH,
            'blockquote': MarkdownElement.BLOCKQUOTE,
            'pre': MarkdownElement.CODE_BLOCK,
            'hr': MarkdownElement.HORIZONTAL_RULE,
            'ul': MarkdownElement.UNORDERED_LIST,
            'ol': MarkdownElement.ORDERED_LIST,
            'li': MarkdownElement.LIST_ITEM,
            'table': MarkdownElement.TABLE,
            'th': MarkdownElement.TABLE_HEADER,
            'td': MarkdownElement.TABLE_CELL,
            'a': MarkdownElement.LINK,
            'img': MarkdownElement.IMAGE,
        }
        return tag_mapping.get(html_tag.lower())
    
    def get_style_for_html_tag(self, html_tag: str) -> Optional[WordStyle]:
        """Get Word style for HTML tag."""
        element = self.map_html_tag_to_element(html_tag)
        return self.get_word_style(element) if element else None
    
    def update_style_mapping(self, markdown_element: MarkdownElement, word_style: WordStyle):
        """Update or add a style mapping."""
        self._style_map[markdown_element] = word_style
    
    def get_all_mappings(self) -> Dict[MarkdownElement, WordStyle]:
        """Get all style mappings."""
        return self._style_map.copy()
    
    def apply_style_to_run(self, run, word_style: WordStyle):
        """Apply Word style properties to a document run."""
        if word_style.font_name:
            run.font.name = word_style.font_name
        if word_style.font_size:
            run.font.size = word_style.font_size
        if word_style.bold is not None:
            run.bold = word_style.bold
        if word_style.italic is not None:
            run.italic = word_style.italic
        if word_style.underline is not None:
            run.underline = word_style.underline
        if word_style.color:
            # Color mapping would need to be implemented based on docx color system
            pass
    
    def apply_style_to_paragraph(self, paragraph, word_style: WordStyle):
        """Apply Word style properties to a document paragraph."""
        if word_style.paragraph_style:
            try:
                paragraph.style = word_style.paragraph_style
            except KeyError:
                # Style doesn't exist in document, use Normal
                paragraph.style = 'Normal'


# Convenience function to get the default style mapper
def get_default_style_mapper() -> StyleMapper:
    """Get a StyleMapper instance with default mappings."""
    return StyleMapper()


# Example usage and testing
if __name__ == "__main__":
    # Create style mapper
    mapper = get_default_style_mapper()
    
    # Test mappings
    print("Markdown to Word Style Mappings:")
    print("=" * 40)
    
    for element, style in mapper.get_all_mappings().items():
        print(f"{element.value:15} -> {style.name}")
        if style.paragraph_style:
            print(f"{'':15}    Paragraph: {style.paragraph_style}")
        if style.font_name:
            print(f"{'':15}    Font: {style.font_name}")
        if style.bold:
            print(f"{'':15}    Bold: {style.bold}")
        if style.italic:
            print(f"{'':15}    Italic: {style.italic}")
        print()
    
    # Test HTML tag mapping
    print("\nHTML Tag to Markdown Element Mapping:")
    print("=" * 40)
    
    test_tags = ['h1', 'h2', 'p', 'strong', 'em', 'code', 'blockquote', 'ul', 'ol', 'table']
    for tag in test_tags:
        element = mapper.map_html_tag_to_element(tag)
        if element:
            style = mapper.get_word_style(element)
            print(f"{tag:10} -> {element.value:15} -> {style.name if style else 'None'}")