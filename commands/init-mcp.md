# InitMCP: Claude Code MCP服务器初始化工具

## 概述

这是一个用于初始化和管理Claude Code的MCP（Model Context Protocol）服务器的工具。MCP服务器扩展了Claude Code的功能，提供文档处理、代码分析、网页浏览等额外能力。

## 可用的MCP服务器

以下是所有可用的MCP服务器配置：

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
    "serena": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "D:\\Repository\\serena",
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
    "sequential-thinking": {
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ],
      "command": "npx"
    },
    "context7": {
        "type": "http",
        "url": "https://mcp.context7.com/mcp",
        "headers": {
        "CONTEXT7_API_KEY": "ctx7sk-a06a3bd3-9890-4d94-8579-f63ecbed86ac"
        }
    }
  }
}
```

### 服务器详细介绍

**📄 文档处理类**
- **word-document-server**:
  - **功能**: Word文档的创建、编辑、格式化和内容提取
  - **能力**: 文档结构解析、样式应用、内容搜索和替换
  - **适用**: 报告生成、文档批量处理、模板填充

**💻 代码分析类**
- **serena**:
  - **功能**: 智能代码语义搜索、跨文件分析和精准编辑
  - **能力**: 符号级代码理解、引用关系追踪、重构建议
  - **适用**: 大型代码库维护、架构分析、代码质量优化

**🌐 网络交互类**
- **playwright**:
  - **功能**: 现代网页自动化测试和数据抓取
  - **能力**: 浏览器操作、表单填写、截图录制、性能测试
  - **适用**: E2E测试、爬虫开发、UI自动化

- **deepwiki**:
  - **功能**: GitHub仓库智能文档检索和分析
  - **能力**: README解析、代码示例提取、API文档生成
  - **适用**: 开源项目研究、技术栈分析、最佳实践学习

**📚 知识检索类**
- **microsoft_docs_mcp**:
  - **功能**: Microsoft官方技术文档智能检索
  - **能力**: Azure、.NET、Office 365等产品文档查询
  - **适用**: 微软技术栈开发、API参考查阅

- **context7**:
  - **功能**: 编程库和框架文档的智能获取
  - **能力**: 多语言库支持、代码示例生成、版本感知
  - **适用**: 第三方库集成、API使用指导、技术选型

- **hf-mcp-server**:
  - **功能**: Hugging Face模型和数据集生态访问
  - **能力**: 模型信息查询、数据集浏览、使用示例获取
  - **适用**: AI/ML项目开发、模型选择、数据集调研

**🤖 AI服务类**
- **aihubmix-api**:
  - **功能**: 多AI模型统一调用接口
  - **能力**: 模型切换、负载均衡、成本优化
  - **适用**: 多模型对比、AI能力验证、生产环境部署

**🧠 思维增强类**
- **sequential-thinking**:
  - **功能**: 结构化思维训练和复杂问题分解
  - **能力**: 逻辑推理、步骤规划、决策树分析
  - **适用**: 复杂项目规划、技术方案设计、问题排查

## 工作流

### 步骤1：检查现有配置
检查当前目录是否已存在`.mcp.json`配置文件：
- **无配置文件**: 展示所有可用的MCP服务器
- **有配置文件**: 过滤已配置的服务器，仅展示未配置的

### 步骤2：用户选择
根据项目需求，用户选择需要启用的MCP服务器：
- 建议默认选择：`sequential-thinking`、`serena`
- 根据具体需求选择其他服务器

### 步骤3：配置生成
根据用户选择生成或更新`.mcp.json`配置文件

## 使用场景

### 初始化情景
为新项目创建完整的MCP配置：
1. 用户选择所需的MCP服务器序号
2. 在项目目录创建`.mcp.json`文件
3. 包含所选服务器的完整配置

### 增量情景
为现有项目添加新的MCP服务器：
1. 读取现有`.mcp.json`配置
2. 展示未配置的服务器选项
3. 用户选择需要添加的服务器
4. 更新配置文件，保留原有设置

## 最佳实践

### 推荐配置

**🎯 基础开发环境** (通用项目):
- `sequential-thinking`: 复杂问题分解和技术决策
- `serena`: 代码质量和架构维护

**📄 文档密集型项目** (技术文档、报告生成):
- 基础配置 + `word-document-server`: 文档自动化处理
- `context7`: 第三方库文档快速查询

**🌐 Web应用开发** (前端、全栈项目):
- 基础配置 + `playwright`: E2E测试和UI自动化
- `deepwiki`: 技术栈研究和最佳实践学习

**🤖 AI/机器学习项目**:
- 基础配置 + `hf-mcp-server`: 模型和数据集调研
- `context7`: ML框架文档和API参考
- `aihubmix-api`: 多模型能力验证和对比

**🏢 企业级应用** (.NET/Azure生态):
- 基础配置 + `microsoft_docs_mcp`: 官方文档查询
- `word-document-server`: 规范文档生成

**🔬 研究和开源项目**:
- 基础配置 + `deepwiki`: 相关项目技术栈分析
- `hf-mcp-server`: SOTA模型和方案调研

### 配置管理
1. **按需启用**: 只启用项目实际需要的MCP服务器
2. **安全考虑**: 妥善保管API密钥，不要提交到版本控制
3. **性能优化**: 避免同时启用过多服务器，可能影响性能

### 故障排除
- **连接失败**: 检查网络连接和API密钥
- **依赖缺失**: 确保所需的运行时环境（Python、Node.js、uv）
- **权限问题**: 检查脚本执行权限
- **配置错误**: 验证JSON格式和路径配置

---

*该工具简化了MCP服务器的配置过程，使Claude Code能够快速获得各种扩展能力。*

