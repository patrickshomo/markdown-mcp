# Bedrock Samples

Container-ready projects for Amazon Bedrock with optional MCP server support.

## Structure

- `src/` - All source code (app logic and MCP servers)
- `docker/` - Container configurations (created when needed)
- `doc/` - Documentation and guides

## Quick Start

1. Add your code to `src/`
2. Mark MCP functions with `# MCP_FUNCTION` comment
3. Use `docker/` for containerization when ready

See [doc/structure.md](doc/structure.md) for detailed guidance.