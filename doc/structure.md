# Project Structure Guide

## Simple Projects
```
project/
├── src/
│   ├── main.py          # Main application
│   ├── models/          # Data models
│   ├── services/        # Business logic
│   └── utils/           # Utilities
├── docker/
│   ├── Dockerfile
│   └── requirements.txt
├── doc/
│   └── api.md
└── README.md
```

## Projects with MCP
```
project/
├── src/
│   ├── app/             # Main application
│   └── mcp/             # MCP servers
│       ├── weather/     # Example MCP tool
│       │   ├── server.py
│       │   ├── client.py
│       │   └── README.md
│       └── database/    # Another MCP tool
├── docker/
│   ├── app.Dockerfile
│   ├── mcp.Dockerfile
│   └── docker-compose.yml
└── README.md
```

## Key Principles
1. **Flat when possible** - Avoid deep nesting
2. **Purpose-driven** - Group by function, not file type
3. **Container-ready** - Docker configs separate but accessible
4. **Self-documenting** - Structure should be obvious