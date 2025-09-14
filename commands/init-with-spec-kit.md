# Spec Kit 项目初始化

## 概述

此command用于使用GitHub官方的spec-kit模板来初始化新的项目。Spec Kit是一个实现**规范驱动开发（Spec-Driven Development, SDD）**的开发框架，通过将规范作为可执行的主要工件来直接生成实现，而不是传统的代码优先方法。

**🎯 核心理念**: 规范成为真实的源头，代码服务于规范，而不是相反。

### Spec Kit的核心优势
- **规范优先**: 规范是主要工件，代码只是规范的表达形式
- **可执行规范**: 规范足够精确和明确，能够直接生成工作系统
- **持续细化**: 通过多步骤细化过程而非一次性代码生成
- **意图驱动**: 先定义"做什么"和"为什么"，再考虑"如何做"
- **AI代理集成**: 支持Claude、Gemini、Copilot、Cursor等多种AI代理

### 宪政框架
spec-kit包含强大的宪政框架（`memory/constitution.md`），定义了不可变的架构原则和质量标准，确保AI代理在实现过程中遵循这些原则。

## 1 工作流

### 📋 前置条件检查清单
在开始之前，请确认：

#### 系统要求
- [ ] **uv包管理器**: 已安装并可用（用于运行specify CLI）
- [ ] **网络连接**: 可访问GitHub以下载模板
- [ ] **文件权限**: 有足够权限在目标目录创建文件和文件夹
- [ ] **Git支持**: 已安装git（可选，用于版本控制初始化）

#### 知识准备
- [ ] **理解SDD**: 了解规范驱动开发的基本理念
- [ ] **AI代理**: 熟悉将要使用的AI代理（推荐Claude）
- [ ] **项目规划**: 明确项目类型和基本需求

### 🔧 详细执行步骤

#### 步骤 1: 环境准备和验证
```bash
# 检查uv是否可用
uv --version

# 如果未安装，请先安装uv
# 在Windows上:
#   powershell -c "irm https://astral.sh/uv/install.sh | iex"
# 在Linux/macOS上:
#   curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### 步骤 2: 执行Spec Kit初始化命令
**🎯 关键决策点**: 选择合适的AI代理和脚本类型

```bash
# 基础命令格式
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>

# 推荐：Windows + Claude
uvx --from git+https://github.com/github/spec-kit.git specify init my-project --ai claude --script ps

# 推荐：Linux/macOS + Claude
uvx --from git+https://github.com/github/spec-kit.git specify init my-project --ai claude --script sh

# 在当前目录初始化（适用于已有项目目录）
uvx --from git+https://github.com/github/spec-kit.git specify init --ai claude --script ps --here
```

**📝 AI代理选择指南**:
- **Claude**: 推荐，优秀的代码生成和推理能力
- **Gemini**: 快速响应，适合简单项目
- **Copilot**: 与GitHub生态系统深度集成
- **Cursor**: 专为代码优化设计

#### 步骤 3: 交互式配置
spec-kit会引导您完成以下配置：

```
🤖 Spec Kit Project Initialization
===========================================

? Select AI assistant: [Use arrow keys]
> claude    (推荐：平衡的性能和代码质量)
  gemini    (快速：适合原型开发)
  copilot   (集成：GitHub生态友好)
  cursor    (专注：代码优化导向)

? Select script type: [Use arrow keys]
> ps        (PowerShell - Windows系统推荐)
  sh        (Bash/Zsh - Linux/macOS推荐)

✅ Downloading template package...
✅ Extracting to project directory...
✅ Setting up file permissions...
✅ Initializing git repository...
```

#### 步骤 4: 验证初始项目结构
初始化完成后，验证以下结构：

```
project-name/
├── .specify/
│   └── scripts/              # 自动化脚本
├── memory/
│   ├── constitution.md       # 📜 架构宪章（重要！）
│   └── constitution_update_checklist.md
├── scripts/
│   └── create-new-feature.sh # 功能创建脚本
├── specs/
│   └── 001-feature/
│       └── spec.md          # 示例规格说明
├── templates/
│   └── spec-template.md     # 规格模板
├── .gitignore
├── .git/                    # Git仓库
└── README.md
```

**⚠️ 重要**: 请花时间阅读 `memory/constitution.md`，这是项目的架构基础！

#### 步骤 5: Claude Code环境集成
```bash
# 进入项目目录
cd project-name

# 初始化MCP服务器
/init-mcp

# 选择推荐的MCP服务器：
# - sequential-thinking (必需)
# - serena (代码分析)
# - context7 (技术文档)
```

#### 步骤 6: 项目上下文建立
```bash
# 分析项目结构并建立CLAUDE.md
# 调用 Codebase Analyzer → Memorizer 工具链
```

#### 步骤 7: 文档系统同步
```bash
# 创建项目文档和LOG.md
# 调用 Document Manager → Log Recorder 工具链
```

## 2 🚀 快速开始：您的第一个SDD项目

### 2.1 理解SDD工作流程

spec-kit使用三阶段工作流程：

```
📝 /specify → 📋 /plan → ✅ /tasks
    ↓            ↓           ↓
 定义需求     制定计划     执行任务
 (做什么)     (怎么做)     (具体做)
```

#### 阶段 1: `/specify` - 规范定义
**🎯 目标**: 将想法转化为结构化规范
```bash
# 在AI代理中执行
/specify 我想要一个用户认证系统，支持邮箱和密码登录
```

**💡 关键要点**:
- 专注于"**做什么**"和"**为什么**"
- **避免**技术实现细节
- 描述用户需求和业务价值

#### 阶段 2: `/plan` - 技术规划
**🎯 目标**: 将规范转化为技术实现方案
```bash
# 在AI代理中执行
/plan
```

**📋 输出内容**:
- `plan.md` - 实施计划
- `research.md` - 技术调研
- `data-model.md` - 数据模型
- `contracts/` - API契约
- `quickstart.md` - 验证指南

#### 阶段 3: `/tasks` - 任务分解
**🎯 目标**: 将计划分解为可执行的任务
```bash
# 在AI代理中执行
/tasks
```

**✅ 输出特点**:
- 按依赖关系排序的任务列表
- 标记可并行执行的任务 `[P]`
- 与Claude Code子代理系统无缝集成

### 2.2 实际示例：创建待办事项应用

#### 步骤 1: 定义功能规范
```bash
/specify 我想要一个简单的待办事项管理应用，用户可以：
1. 添加新的待办事项
2. 标记事项为已完成
3. 删除待办事项
4. 查看所有待办事项列表

这个应用应该是命令行工具，数据存储在本地文件中。
```

#### 步骤 2: 生成实现计划
```bash
/plan
```
spec-kit会询问技术栈选择，推荐选择Python + argparse + JSON文件存储。

#### 步骤 3: 执行任务
```bash
/tasks
```
生成的任务列表将包含：
1. `[P] 创建数据模型`
2. `[P] 设计文件存储格式`
3. 创建CLI接口
4. 实现添加功能
5. 实现列表功能
6. 实现标记完成功能
7. 实现删除功能
8. 添加测试用例

## 3 🎯 用户最佳实践指南

### 3.1 新手常见误区

#### ❌ 错误1: 在规范阶段包含技术细节
```bash
# 错误示例
/specify 我想要一个用Python Flask和SQLite实现的用户系统

# 正确示例
/specify 我想要一个用户管理系统，支持用户注册、登录和个人资料管理
```

#### ❌ 错误2: 跳过验证步骤
```bash
# 错误：直接接受AI的第一次输出
/specify 用户登录系统
# （然后就直接跳到/plan）

# 正确：验证和完善规范
/specify 用户登录系统
# → 检查生成的spec.md
# → 询问AI："请检查[NEEDS CLARIFICATION]项目"
# → 确认所有需求都被正确理解
```

#### ❌ 错误3: 忽视宪政框架
```bash
# 错误：不阅读memory/constitution.md
# 直接开始开发

# 正确：先理解架构原则
# 仔细阅读memory/constitution.md的九条开发条款
# 特别关注：
# - 图书优先原则
# - 测试优先原则
# - 简洁性原则
```

### 3.2 成功的关键原则

#### ✅ 原则1: 意图驱动开发
**关注点**: 用户的"what"和"why"
```bash
# 好的规范描述
"用户应该能够通过邮箱注册账户，收到验证邮件后激活账户"

# 避免的描述
"使用JWT token实现用户认证，发送验证邮件"
```

#### ✅ 原则2: 迭代式细化
**方法**: 多轮对话澄清需求
```bash
# 第一轮
/specify 我想要一个照片组织应用

# 第二轮（基于AI反馈）
"照片应该按日期自动分组，支持添加标签和搜索功能"

# 第三轮（进一步细化）
"界面应该显示缩略图网格，支持拖拽重新排列"
```

#### ✅ 原则3: 拥抱测试优先
**要求**: 先写测试，后写实现
```bash
# 在/plan阶段，AI会生成测试任务
# 确保这些任务优先执行：
# 1. 编写失败的单元测试
# 2. 实现功能让测试通过
# 3. 重构代码
```

### 3.3 团队协作指南

#### 团队成员角色
- **产品负责人**: 负责`/specify`阶段，定义业务需求
- **技术负责人**: 负责`/plan`阶段，选择技术栈
- **开发者**: 负责`/tasks`阶段，实现具体功能

#### 协作流程
1. **需求讨论**: 团队共同参与`/specify`阶段
2. **技术评审**: 技术团队评审`/plan`输出
3. **任务分配**: 基于`/tasks`输出分配开发任务
4. **代码审查**: 确保实现符合宪政框架

## 4 🛠️ 高级配置和定制

### 4.1 自定义宪政框架
编辑 `memory/constitution.md` 来定制项目的架构原则：

```markdown
# 示例：添加新的架构原则
## Article X: 云原生优先
所有组件必须设计为容器化部署，支持水平扩展。
```

### 4.2 模板定制
修改 `templates/` 目录下的模板文件：

- `spec-template.md`: 功能规格模板
- `plan-template.md`: 实施计划模板
- `task-template.md`: 任务分解模板

### 4.3 集成外部工具
在 `.specify/scripts/` 目录添加自定义脚本：

```bash
#!/bin/bash
# 示例：自定义部署脚本
echo "部署到生产环境..."
./deploy.sh
```

## 5 🔍 故障排除

### 5.1 常见问题

#### 问题: uv包管理器不可用
**症状**: `command not found: uv`
**解决方案**:
```bash
# Windows
powershell -c "irm https://astral.sh/uv/install.sh | iex"

# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### 问题: 网络连接失败
**症状**: 无法下载模板
**解决方案**:
```bash
# 使用代理
uvx --from git+https://github.com/github/spec-kit.git specify init my-project --skip-tls

# 或手动下载模板
```

#### 问题: AI代理不响应
**症状**: `/specify` 命令无反应
**解决方案**:
```bash
# 检查AI代理配置
specify check --ignore-agent-tools

# 重新初始化AI代理设置
```

### 5.2 性能优化

#### 大型项目处理
- 使用 `--no-git` 跳过Git初始化（后续手动设置）
- 分模块初始化，避免一次性创建过多文件
- 使用 `.gitignore` 排除不必要的文件

#### 缓存管理
```bash
# 清理uv缓存
uv cache clean

# 重新下载最新模板
uvx --from git+https://github.com/github/spec-kit.git specify init my-project --debug
```

## 6 📚 进阶学习资源

### 6.1 官方文档
- **Spec Kit Wiki**: https://deepwiki.com/github/spec-kit
- **GitHub仓库**: https://github.com/github/spec-kit
- **SDD方法论**: 详见wiki的"Spec-Driven Development Methodology"章节

### 6.2 示例项目
- **待办事项应用**: 简单的CLI工具示例
- **Web API**: RESTful API开发示例
- **数据分析工具**: 复杂数据处理示例

### 6.3 社区资源
- **讨论区**: GitHub Discussions
- **问题报告**: GitHub Issues
- **功能请求**: GitHub Features

---

## 🎉 恭喜！

您现在已经掌握了spec-kit的使用方法。记住：

**🔄 核心循环**: `/specify` → `/plan` → `/tasks` → 开发 → 验证 → 迭代

**📈 成功要素**:
- 清晰的意图表达
- 严格遵循宪政框架
- 持续验证和改进
- 与Claude Code的无缝集成

开始您的SDD之旅吧！遇到问题时，记得查阅故障排除部分或寻求社区帮助。

**最后提醒**: spec-kit是一个强大的工具，但真正的价值来自于您对SDD理念的理解和实践。保持学习和探索的心态！