#!/usr/bin/env python3
"""Test runner for markdown-mcp project."""

import subprocess
import sys
import shutil
from pathlib import Path

def run_tests():
    """Run all tests in proper order."""
    test_order = [
        "test_converter.py",
        "test_batch_conversion.py"
    ]
    
    tests_dir = Path(__file__).parent
    project_root = tests_dir.parent
    
    # Clean output directory before running tests
    output_dir = tests_dir / "output"
    if output_dir.exists():
        shutil.rmtree(output_dir)
        print(f"🧹 Cleaned output directory: {output_dir}")
    output_dir.mkdir(exist_ok=True)
    
    failed = []
    
    for test_file in test_order:
        test_path = tests_dir / test_file
        if not test_path.exists():
            print(f"⚠️  {test_file} not found, skipping")
            continue
            
        print(f"🧪 Running {test_file}...")
        result = subprocess.run([
            sys.executable, str(test_path)
        ], cwd=project_root)
        
        if result.returncode != 0:
            failed.append(test_file)
            print(f"❌ {test_file} failed")
        else:
            print(f"✅ {test_file} passed")
    
    if failed:
        print(f"\n❌ {len(failed)} test file(s) failed: {', '.join(failed)}")
        sys.exit(1)
    else:
        print("\n✅ All tests passed!")

if __name__ == "__main__":
    run_tests()