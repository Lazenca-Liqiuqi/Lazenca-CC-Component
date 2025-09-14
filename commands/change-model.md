# ChangeModel: Claude Code模型切换工具

## 概述

这是一个用于快速切换Claude Code使用的AI模型的命令行工具。支持多种AI服务提供商，包括Claude、GLM、Deepseek和Kimi等。

## 支持的模型

### 1. Claude (通过Wentuo代理)
- **特点**: 原生Claude模型，质量稳定
- **适用场景**: 代码生成、文档编写、复杂推理

### 2. GLM-4.5 (智谱AI)
- **特点**: 中文理解能力强，性价比高
- **适用场景**: 中文内容创作、日常对话

### 3. Deepseek Chat
- **特点**: 代码能力强，响应速度快
- **适用场景**: 编程辅助、技术文档

### 4. Kimi K2 Turbo
- **特点**: 长文本处理能力强，上下文理解好
- **适用场景**: 长文档分析、复杂任务

## 使用方法

### 方式一：环境变量设置（推荐）

```powershell
# Claude
setx ANTHROPIC_BASE_URL "https://api.wentuo.ai"
setx ANTHROPIC_AUTH_TOKEN "sk-hiEi8inFbUOKsjoAxRV7Zdy8hFXF201PsMAcLIFCW1F100z1"
setx ANTHROPIC_MODEL ""
setx ANTHROPIC_DEFAULT_HAIKU_MODEL ""

# GLM-4.5
setx ANTHROPIC_BASE_URL "https://open.bigmodel.cn/api/anthropic"
setx ANTHROPIC_AUTH_TOKEN "43632cc392ed478783266f5c0e4cb330.RebbA38cPxJLSVTr"
setx ANTHROPIC_MODEL "glm-4.5"
setx ANTHROPIC_DEFAULT_HAIKU_MODEL "glm-4.5"

# Deepseek
setx ANTHROPIC_BASE_URL "https://api.deepseek.com/anthropic"
setx ANTHROPIC_AUTH_TOKEN "sk-8c6697412ccd45b289912efe2ff909d5"
setx ANTHROPIC_MODEL "deepseek-chat"
setx ANTHROPIC_DEFAULT_HAIKU_MODEL "deepseek-chat"

# Kimi K2
setx ANTHROPIC_BASE_URL "https://api.moonshot.cn/anthropic/"
setx ANTHROPIC_AUTH_TOKEN "sk-eJ2bFotPeaSjJ6qhx7CtMCJ2hof1xFpv3rNoqhrBqSRkgCY2"
setx ANTHROPIC_MODEL "kimi-k2-turbo-preview"
setx ANTHROPIC_DEFAULT_HAIKU_MODEL "kimi-k2-turbo-preview"
```

### 方式二：配置文件设置

编辑Claude Code的settings.json文件：

```json
{
  // Kimi K2
  "ANTHROPIC_BASE_URL": "https://api.moonshot.cn/anthropic/",
  "ANTHROPIC_AUTH_TOKEN": "sk-eJ2bFotPeaSjJ6qhx7CtMCJ2hof1xFpv3rNoqhrBqSRkgCY2",
  "ANTHROPIC_MODEL": "kimi-k2-turbo-preview",
  "ANTHROPIC_DEFAULT_HAIKU_MODEL": "kimi-k2-turbo-preview"

  // 或选择其他模型
  // "ANTHROPIC_BASE_URL": "https://api.wentuo.ai",
  // "ANTHROPIC_AUTH_TOKEN": "sk-hiEi8inFbUOKsjoAxRV7Zdy8hFXF201PsMAcLIFCW1F100z1"

  // "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic",
  // "ANTHROPIC_AUTH_TOKEN": "43632cc392ed478783266f5c0e4cb330.RebbA38cPxJLSVTr",
  // "ANTHROPIC_MODEL": "glm-4.5",
  // "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-4.5"

  // "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
  // "ANTHROPIC_AUTH_TOKEN": "sk-8c6697412ccd45b289912efe2ff909d5",
  // "ANTHROPIC_MODEL": "deepseek-chat",
  // "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-chat"
}
```

## 工作流

### 步骤1：展示模型选项
向用户展示所有可用的模型选项，包括：
- 模型名称和提供商
- 主要特点和适用场景
- 性能和成本信息

### 步骤2：用户选择
用户根据需求选择合适的模型

### 步骤3：执行切换
根据用户选择的方式（环境变量或配置文件）执行切换操作

### 步骤4：验证设置
验证设置是否生效，可能需要重启Claude Code

## 最佳实践

### 选择建议
- **代码开发**: 优先选择Claude或Deepseek
- **中文内容**: GLM-4.5或Kimi K2
- **长文档处理**: Kimi K2
- **成本敏感**: GLM-4.5

### 注意事项
1. 环境变量设置后需要重启终端或Claude Code
2. API密钥请妥善保管，不要泄露
3. 不同服务商的调用限制和费用不同
4. 建议根据具体任务选择最适合的模型

### 故障排除
- 如果设置后无法使用，检查API密钥是否正确
- 确认网络连接正常
- 验证服务商的服务状态
- 查看Claude Code的错误日志

---

*该工具提供了灵活的模型切换能力，确保用户可以根据不同需求选择最适合的AI模型。*