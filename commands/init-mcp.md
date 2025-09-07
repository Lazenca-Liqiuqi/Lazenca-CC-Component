# Claude Code MCP初始化

## 1 工作流

###  1.1 先展示所有mcp服务器

这是所有mcp服务器的信息，请给用户展示所有mcp的名字，然后让他挑出需要的。

```json
{
  "mcpServers": {
    "word-document-server": {
      "command": "python",
      "args": [
        "D:/Others(English)/MCP/Office-Word-MCP-Server/word_mcp_server.py"
      ],
      "env": {
        "MCP_TRANSPORT": "stdio"
      }
    },
    "github": {
    "type": "http",
    "url": "https://api.githubcopilot.com/mcp",
    "headers": {
    "Authorization": "GITHUB_PERSONAL_ACCESS_TOKEN=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"
    }
    },
    "playwright": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ],
      "env": {}
    },
    "microsoft_docs_mcp": {
      "type": "http",
      "url": "https://learn.microsoft.com/api/mcp"
    },
    "deepwiki": {
      "type": "http",
      "url": "https://mcp.deepwiki.com/mcp"
    },
    "hf-mcp-server": {
      "type": "http",
      "url": "https://huggingface.co/mcp",
      "headers": {
        "Authorization": "Bearer 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"
      }
    },
    "typst-mcp": {
      "type": "stdio",
      "command": "python",
      "args": [
        "D:\\Others(English)\\MCP\\typst-mcp\\server.py"
      ],
      "env": {}
    },
    "serena": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "D:\\Others(English)\\MCP\\serena",
        "serena-mcp-server"
      ]
    },
    "aihubmix-api": {
      "type": "http",
      "url": "https://aihubmix.com/mcp/",
      "headers": {
        "Authorization": "Bearer sk-x5mwr3r4PtDKudpmEaC4F73bFfC64f5391AcD3E923440e8c"
      }
    },
    "gitmcp": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://gitmcp.io/{owner}/{repo}"
      ]
    },
    "sequential-thinking": {
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ],
      "command": "npx"
    }
  }
}
  
```

### 1.2 询问用户需要哪些

用户会回答他所需要的mcp的序号。

默认情况下，sequential thinking、serena是需要添加的。

### 1.3 第三步：添加MCP

在本项目目录创建文件 `.mcp.json`，里面是选择了的mcp服务器，格式和上面的代码一致。
