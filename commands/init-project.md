# 项目初始化

## 1 工作流

1. 先调用`Codebase Analyzer`递归读取各级目录并生成项目信息。
2. 调用``Memorizer`将信息写入各级`CLAUDE.md`。
3. 调用`Code Explainer`为各处代码文件添加详细注释，并向`CLAUDE.md`中追加技术文档。
4. 调用`Log Recorder`记录初始化日志。