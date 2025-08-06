"""Test the StyleMapper functionality."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from mcp.markdown_converter.style_mapper import StyleMapper, MarkdownElement, WordStyle


def test_style_mapper():
    """Test the StyleMapper class."""
    print("Testing StyleMapper...")
    
    # Create mapper
    mapper = StyleMapper()
    
    # Test basic mappings
    print("\n1. Testing basic style mappings:")
    test_elements = [
        MarkdownElement.H1,
        MarkdownElement.H2,
        MarkdownElement.PARAGRAPH,
        MarkdownElement.STRONG,
        MarkdownElement.EMPHASIS,
        MarkdownElement.CODE_INLINE,
        MarkdownElement.BLOCKQUOTE,
        MarkdownElement.CODE_BLOCK
    ]
    
    for element in test_elements:
        style = mapper.get_word_style(element)
        print(f"  {element.value:15} -> {style.name if style else 'None'}")
        if style and style.paragraph_style:
            print(f"  {'':15}    Paragraph Style: {style.paragraph_style}")
    
    # Test HTML tag mapping
    print("\n2. Testing HTML tag to Markdown element mapping:")
    test_tags = ['h1', 'h2', 'p', 'strong', 'em', 'code', 'blockquote', 'pre', 'ul', 'ol']
    
    for tag in test_tags:
        element = mapper.map_html_tag_to_element(tag)
        style = mapper.get_style_for_html_tag(tag)
        print(f"  {tag:10} -> {element.value if element else 'None':15} -> {style.name if style else 'None'}")
    
    # Test style name retrieval
    print("\n3. Testing style name retrieval:")
    print(f"  H1 style name: {mapper.get_word_style_name(MarkdownElement.H1)}")
    print(f"  H1 paragraph style: {mapper.get_paragraph_style_name(MarkdownElement.H1)}")
    print(f"  Strong style name: {mapper.get_word_style_name(MarkdownElement.STRONG)}")
    
    # Test custom style mapping
    print("\n4. Testing custom style mapping:")
    custom_style = WordStyle("Custom Header", font_name="Arial", font_size=14, bold=True)
    mapper.update_style_mapping(MarkdownElement.H1, custom_style)
    
    updated_style = mapper.get_word_style(MarkdownElement.H1)
    print(f"  Updated H1 style: {updated_style.name}")
    print(f"  Font: {updated_style.font_name}, Size: {updated_style.font_size}, Bold: {updated_style.bold}")
    
    print("\nStyleMapper tests completed successfully!")


def test_markdown_to_word_mapping():
    """Test the complete mapping from Markdown syntax to Word styles."""
    print("\n" + "="*50)
    print("MARKDOWN TO WORD STYLE MAPPING REFERENCE")
    print("="*50)
    
    mapper = StyleMapper()
    
    markdown_examples = [
        ("# Heading 1", "h1", "Creates a top-level heading"),
        ("## Heading 2", "h2", "Creates a second-level heading"),
        ("### Heading 3", "h3", "Creates a third-level heading"),
        ("Regular paragraph", "p", "Normal paragraph text"),
        ("**Bold text**", "strong", "Bold formatting"),
        ("*Italic text*", "em", "Italic formatting"),
        ("`inline code`", "code", "Monospace inline code"),
        ("~~strikethrough~~", "del", "Strikethrough text"),
        ("> Blockquote", "blockquote", "Quoted text block"),
        ("```\ncode block\n```", "pre", "Monospace code block"),
        ("- List item", "ul", "Bullet list"),
        ("1. Numbered item", "ol", "Numbered list"),
        ("[Link](url)", "a", "Hyperlink"),
        ("![Image](url)", "img", "Embedded image"),
    ]
    
    print(f"{'Markdown Syntax':<20} {'HTML Tag':<10} {'Word Style':<20} {'Description'}")
    print("-" * 80)
    
    for markdown, html_tag, description in markdown_examples:
        element = mapper.map_html_tag_to_element(html_tag)
        style = mapper.get_word_style(element) if element else None
        word_style_name = style.name if style else "Default"
        
        print(f"{markdown:<20} {html_tag:<10} {word_style_name:<20} {description}")
    
    print("\nParagraph Styles Used:")
    print("-" * 30)
    
    for element, style in mapper.get_all_mappings().items():
        if style.paragraph_style:
            print(f"  {element.value:<15} -> {style.paragraph_style}")


if __name__ == "__main__":
    test_style_mapper()
    test_markdown_to_word_mapping()