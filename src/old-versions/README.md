# Old Versions Directory

This directory contains outdated source and test files that are no longer used in the current version of the project.

## Moved Files

### Outdated Source Files
- `converter.py` - Original basic markdown converter (replaced by `simple_improved_converter.py`)
- `improved_converter.py` - First attempt at improved converter with pymdownx dependencies (replaced by `simple_improved_converter.py`)
- `server.py` - Original MCP server (replaced by `enhanced_server.py`)

### Outdated Test Files
- `test_converter.py` - Tests for original converter
- `test_improved_converter.py` - Tests for first improved converter

### Outdated Demo Scripts
- `convert_test1.py` - Basic test conversion script
- `convert_test1_debug.py` - Debug version of test script
- `convert_test1_final.py` - Final version using original converter
- `test_demo.py` - Demo script for improved_converter.py
- `test_simple_demo.py` - Demo script for simple_improved_converter.py

## Current Implementation

The current active implementation uses:
- **Main Converter**: `simple_improved_converter.py` - GFM-compliant converter using standard markdown library
- **MCP Server**: `enhanced_server.py` - Full-featured MCP server with all functions
- **Tests**: Phase-based tests in `tests/test_phase*.py` files

## Why These Files Were Moved

1. **Architecture Evolution**: The project evolved from manual regex parsing to proper markdown library usage
2. **Dependency Management**: Moved away from pymdownx extensions to standard markdown library for better compatibility
3. **Feature Completeness**: The current implementation provides full GFM support without external dependencies
4. **Code Quality**: Better error handling, validation, and maintainability in current version

## Historical Context

These files represent the development journey:
1. **Phase 1**: Basic converter with manual parsing (`converter.py`)
2. **Phase 2**: Improved converter with pymdownx extensions (`improved_converter.py`)
3. **Phase 3**: Final simplified converter with standard libraries (`simple_improved_converter.py`)

The current implementation combines the best aspects of all previous versions while maintaining simplicity and reliability.