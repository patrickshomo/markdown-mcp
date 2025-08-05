"""Test batch conversion of input files to output directory."""

import pytest
from pathlib import Path
from src.mcp.markdown_converter.batch_processor import BatchProcessor


def test_convert_input_to_output():
    """Convert all markdown files in tests/input to tests/output."""
    processor = BatchProcessor()
    
    input_dir = "tests/input"
    output_dir = "tests/output"
    
    result = processor.process_directory(input_dir, output_dir)
    
    print(f"Batch conversion results: {result}")
    
    assert result["processed"] > 0
    assert result["successful"] > 0
    
    # Verify output files exist
    output_path = Path(output_dir)
    docx_files = list(output_path.glob("*.docx"))
    
    print(f"Generated DOCX files: {[f.name for f in docx_files]}")
    
    assert len(docx_files) >= result["successful"]


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])