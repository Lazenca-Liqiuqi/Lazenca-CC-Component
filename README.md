# Lazenca CC Component
上次更新时间：2025-09-14 更新README为标准格式

## 1. 项目性质说明
> **本项目为开源分享项目**，提供Claude Code中文开发环境的完整配置方案。作为配置模板和参考方案，不设具体开发目标，欢迎社区使用、修改和改进。

## 2. 定期更新速查表
| 日期 | 更新内容 | 更新人 |
|------|----------|--------|
| 2025-09-14 | 更新README为标准格式，完善项目结构说明 | Moss |
| 2025-09-14 | 添加Context Hunter和Prompt Optimizer代理 | Moss |
| 2025-09-14 | 新增Python Coder和Cpp Coder专业化代理 | Moss |

## 3. 文献调研
- Claude Code 官方文档 - 代理系统架构
- MCP (Model Context Protocol) 规范文档
- Python语音合成最佳实践
- 中文开发环境配置指南

## 4. 项目基本信息
Lazenca CC Component 是一个专为Claude Code设计的中文开发环境配置包。该项目提供了一套完整的智能代理系统、语音交互功能和项目管理工具，旨在为中文用户提供更高效的开发体验。

**核心特点：**
- 基于多代理协作的智能任务处理系统
- 集成Windows语音合成交互功能
- 完整的中文开发规范和项目管理流程
- 可扩展的命令和钩子系统

## 5. 全面的项目工具列表
### 子代理系统
- **Codebase Analyzer**: 代码库结构分析专家
- **Code Explainer**: 代码注释和技术文档生成
- **Document Manager**: 项目文档管理和更新
- **Log Recorder**: 工作日志标准化记录
- **Memorizer**: 项目信息和目录结构维护
- **Context Hunter**: 上下文信息检索专家
- **Prompt Optimizer**: 提示词工程优化专家
- **Python Coder**: Python代码生成专家
- **Cpp Coder**: C++代码生成专家

### 自定义命令
- **init-project**: 项目初始化命令
- **go**: 快速导航命令
- **change-model**: AI模型切换命令
- **convert2word**: 文档转换命令套件
- **init-mcp**: MCP服务器初始化
- **init-existing-project**: 现有项目初始化
- **init-with-spec-kit**: 特定规范项目初始化

### 语音交互系统
- **notification.py**: 用户许可语音播报
- **task_complete_voice.py**: 任务完成语音提示
- **conversation_start_voice.py**: 会话开始欢迎语音

## 6. 变量表 (简写与符号)
- **MCP**: Model Context Protocol - 模型上下文协议
- **CC**: Claude Code - AI编程助手
- **TODO**: 待办事项列表
- **LOG**: 工作日志记录

## 7. 项目进展记录
当前项目已建立完整的基础架构，包括9个专业化AI子代理、8个自定义命令和3个语音交互钩子。项目采用标准化的文档格式和协作流程，支持复杂的开发任务处理。

### 成果展示 (由用户填写)
- [ ] 成功应用于实际项目开发
- [ ] 提升开发效率XX%
- [ ] 用户反馈评分X/5
- [ ] 减少重复工作量XX%