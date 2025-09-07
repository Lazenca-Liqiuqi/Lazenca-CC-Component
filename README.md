# Lazenca CC Component

Claude Code 的中文开发环境配置包，包含完整的智能代理系统、语音交互功能和项目管理工具。

## 📁 结构说明

- **agents/** - 6个专业化AI子代理配置
  - Codebase Analyzer：代码库分析
  - Coder：代码生成专家  
  - Code Explainer：代码注释专家
  - Document Manager：文档管理
  - Log Recorder：日志记录
  - Memorizer：记忆管理

- **commands/** - 自定义命令
  - init-project：项目初始化
  - go：快速导航
  - change-model：模型切换
  - convert2word：文档转换

- **hooks/** - 钩子函数
  - notification.py：用户许可语音播报
  - task_complete_voice.py：任务完成提示
  - conversation_start_voice.py：会话开始欢迎

- **settings.json** - Claude Code 配置文件
- **CLAUDE.md** - 核心行为准则和项目配置

## 🚀 主要功能

- **智能代理系统**：多代理协作完成复杂任务
- **语音交互**：Windows语音合成，实时反馈
- **项目管理**：自动分析、文档生成、工作流程
- **中文环境**：完整的中文开发规范和提示词

## 💡 使用方法

1. 将配置文件复制到对应目录
2. 重启 Claude Code
3. 使用 `init-project` 命令初始化新项目
