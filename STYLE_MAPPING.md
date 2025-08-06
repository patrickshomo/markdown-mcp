# Markdown to Word Style Mapping

This document explains how the Markdown to Word converter maps Markdown elements to Microsoft Word styles.

## Overview

The `StyleMapper` class provides a systematic way to map Markdown elements to MS Word styles, ensuring consistent formatting throughout the conversion process. This mapping system allows for:

- **Consistent Styling**: All Markdown elements are mapped to appropriate Word styles
- **Customization**: Style mappings can be modified or extended
- **Template Compatibility**: Works with Word templates and built-in styles

## Core Mapping Table

| Markdown Syntax | HTML Tag | Word Style | Word Paragraph Style | Description |
|----------------|----------|------------|---------------------|-------------|
| `# Heading 1` | `h1` | Heading 1 | Heading 1 | Top-level heading |
| `## Heading 2` | `h2` | Heading 2 | Heading 2 | Second-level heading |
| `### Heading 3` | `h3` | Heading 3 | Heading 3 | Third-level heading |
| `#### Heading 4` | `h4` | Heading 4 | Heading 4 | Fourth-level heading |
| `##### Heading 5` | `h5` | Heading 5 | Heading 5 | Fifth-level heading |
| `###### Heading 6` | `h6` | Heading 6 | Heading 6 | Sixth-level heading |
| Regular text | `p` | Normal | Normal | Standard paragraph |
| `**bold text**` | `strong` | Strong | - | Bold formatting |
| `*italic text*` | `em` | Emphasis | - | Italic formatting |
| `` `inline code` `` | `code` | Code Inline | - | Monospace inline code |
| `~~strikethrough~~` | `del` | Strikethrough | - | Strikethrough text |
| `> blockquote` | `blockquote` | Quote | Quote | Quoted text block |
| ``` code block ``` | `pre` | Code Block | No Spacing | Monospace code block |
| `---` | `hr` | Horizontal Rule | Normal | Horizontal separator |
| `- list item` | `ul` | List Bullet | List Bullet | Bullet list |
| `1. list item` | `ol` | List Number | List Number | Numbered list |
| List item content | `li` | List Item | List Paragraph | Individual list item |
| `- [x] task` | `task_checked` | Task List Checked | List Bullet | Completed task |
| `- [ ] task` | `task_unchecked` | Task List Unchecked | List Bullet | Incomplete task |
| Table | `table` | Table | Table Grid | Table structure |
| Table header | `th` | Table Header | Normal | Table header cell |
| Table cell | `td` | Table Cell | Normal | Table data cell |
| `[link](url)` | `a` | Hyperlink | - | Clickable link |
| `![image](url)` | `img` | Image | Normal | Embedded image |

## Usage Examples

### Basic Usage

```python
from mcp.markdown_converter.style_mapper import StyleMapper, MarkdownElement

# Create style mapper
mapper = StyleMapper()

# Get Word style for a Markdown element
h1_style = mapper.get_word_style(MarkdownElement.H1)
print(f"H1 maps to: {h1_style.name}")  # Output: "Heading 1"

# Get paragraph style name
para_style = mapper.get_paragraph_style_name(MarkdownElement.H1)
print(f"H1 paragraph style: {para_style}")  # Output: "Heading 1"
```

### HTML Tag Mapping

```python
# Map HTML tag to Markdown element
element = mapper.map_html_tag_to_element('h1')
print(f"h1 tag maps to: {element.value}")  # Output: "h1"

# Get style directly from HTML tag
style = mapper.get_style_for_html_tag('strong')
print(f"strong tag style: {style.name}")  # Output: "Strong"
```

### Custom Style Mapping

```python
from mcp.markdown_converter.style_mapper import WordStyle

# Create custom style
custom_style = WordStyle(
    name="Custom Header",
    font_name="Arial",
    font_size=14,
    bold=True,
    paragraph_style="Heading 1"
)

# Update mapping
mapper.update_style_mapping(MarkdownElement.H1, custom_style)
```

## Style Properties

Each `WordStyle` object can have the following properties:

- **name**: Display name of the style
- **font_name**: Font family (e.g., "Arial", "Courier New")
- **font_size**: Font size in points
- **bold**: Boolean for bold formatting
- **italic**: Boolean for italic formatting
- **underline**: Boolean for underline formatting
- **color**: Text color (implementation dependent)
- **background_color**: Background color (implementation dependent)
- **paragraph_style**: Word paragraph style name

## Integration with Converter

The `SimpleImprovedConverter` automatically uses the `StyleMapper` to apply consistent formatting:

```python
from mcp.markdown_converter.simple_improved_converter import SimpleImprovedConverter

# Converter automatically uses StyleMapper
converter = SimpleImprovedConverter()
doc = converter.convert("# My Heading\n\nThis is **bold** text.")
```

## Template Compatibility

The style mapper is designed to work with Word templates:

1. **Built-in Styles**: Uses standard Word styles like "Heading 1", "Normal", "Quote"
2. **Template Styles**: When using templates, styles are applied if they exist in the template
3. **Fallback**: If a style doesn't exist, falls back to "Normal" or appropriate default

## Customization

### Adding New Mappings

```python
# Define new Markdown element (extend MarkdownElement enum)
# Create corresponding WordStyle
new_style = WordStyle("Custom Style", bold=True, italic=True)

# Add to mapper
mapper.update_style_mapping(MarkdownElement.CUSTOM, new_style)
```

### Modifying Existing Mappings

```python
# Get existing style
existing_style = mapper.get_word_style(MarkdownElement.STRONG)

# Create modified version
modified_style = WordStyle(
    name="Enhanced Strong",
    font_name="Arial Black",
    bold=True,
    color="red"
)

# Update mapping
mapper.update_style_mapping(MarkdownElement.STRONG, modified_style)
```

## Best Practices

1. **Use Standard Styles**: Prefer built-in Word styles for maximum compatibility
2. **Test with Templates**: Verify style mappings work with your Word templates
3. **Consistent Naming**: Use descriptive names for custom styles
4. **Fallback Handling**: Always provide fallback options for missing styles
5. **Documentation**: Document any custom style mappings for team use

This style mapping system provides a robust foundation for consistent Markdown to Word conversion while maintaining flexibility for customization and extension.