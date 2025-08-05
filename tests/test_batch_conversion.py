#!/usr/bin/env python3
"""Test batch conversion of input files to output directory."""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.mcp.markdown_converter.batch_processor import BatchProcessor


def test_batch_conversion():
    """Test batch processing of all markdown files in input directory."""
    processor = BatchProcessor()
    
    input_dir = "tests/input"
    output_dir = "tests/output"
    
    result = processor.process_directory(input_dir, output_dir)
    
    print(f"Batch conversion results: {result}")
    
    if "error" in result:
        print(f"Error: {result['error']}")
        return
    
    print(f"Processed: {result['processed']}, Successful: {result['successful']}, Failed: {result['failed']}")
    
    # List generated files
    output_path = Path(output_dir)
    docx_files = list(output_path.glob("*.docx"))
    print(f"Generated files: {[f.name for f in docx_files]}")


def test_batch_with_template():
    """Test batch processing with template."""
    processor = BatchProcessor()
    
    input_dir = "tests/input"
    output_dir = "tests/output"
    
    result = processor.process_directory(
        input_dir, 
        output_dir, 
        template_name="simple",
        metadata={"author": "Batch Test"}
    )
    
    print(f"Batch with template results: {result}")
    
    if "error" not in result:
        # Rename files to indicate template usage
        output_path = Path(output_dir)
        for docx_file in output_path.glob("*.docx"):
            if not docx_file.name.endswith("_template.docx"):
                new_name = docx_file.stem + "_template.docx"
                docx_file.rename(output_path / new_name)
                print(f"  → {new_name}")


if __name__ == "__main__":
    test_batch_conversion()
    test_batch_with_template()