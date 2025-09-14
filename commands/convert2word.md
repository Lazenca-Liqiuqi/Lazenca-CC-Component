# Convert2Word: Typst到Word文档转换完整工作流

## 概述

这是一个完整的Typst到Word文档转换工具，通过四个主要步骤将Typst格式文档转换为Microsoft Word格式。该工作流自动处理引用、文档结构、特殊元素（图、表、公式）和正文内容的转换。

## 前置条件

### 必需的MCP服务器
- `word-document-server`: 用于操作Word文档
- `serena`: 用于代码和文件系统操作

### 必需的工具文件

确保存在以下Python脚本（通常位于`citation_tools`文件夹中）：
- `generate_citation_mapping.py`
- `replace.py`
- `apply_citation_mapping.py`

## 完整工作流

### 第一步：处理引用

**目标**: 将Typst中的引用转换为Word兼容格式

```bash
# 1. 生成引用映射表
python generate_citation_mapping.py <bibtex_file> -o 引用映射表.md

# 2. 处理Typst文件中的引用
python replace.py <typst_file> -o 引用映射表.md -a

# 3. 应用引用映射
python apply_citation_mapping.py 引用映射表.md <typst_file> -o <processed_file>
```

**参数说明**:
- `bibtex_file`: BibTeX格式的参考文献文件路径
- `typst_file`: 需要转换的Typst源文件路径
- `processed_file`: 处理后的Typst文件（输出文件）

**关键点**:
- 所有中间文件保留在citation_tools文件夹内
- 最终转换结果放在Typst文件同目录
- 使用`-a`参数确保追加模式而非覆盖

### 第二步：创建文档结构

**目标**: 建立Word文档的标题和基本结构

**输入**:
- `processed_typst_content`: 第一步处理后的Typst文本
- `word_template_path`: Word模板文件路径（.docx格式）

**执行步骤**:

1. **创建模板副本**
   ```python
   # 复制模板文件，避免修改原模板
   import shutil
   shutil.copy(word_template_path, working_copy_path)
   ```

2. **清除模板内容**
   - 删除模板原有的全部占位内容

3. **插入基本信息**
   - 文章标题（使用MS Title样式）
   - 作者信息（使用Authors样式）
   - 机构信息（使用Affiliation样式）
   - 通讯信息（使用Correspondence样式）

4. **插入摘要**
   ```
   **Abstract** [摘要内容]
   ```

5. **建立标题结构**
   - `= Chapter` → `Heading 1`
   - `== Section` → `Heading 2`
   - `=== Subsection` → `Heading 3`
   - 以此类推...

**输出**: 包含完整标题结构的Word文档对象

### 第三步：迁移特殊元素

**目标**: 识别并迁移图、表、公式等特殊元素

**识别模式**:
- **Figure**: `#figure(...)`
- **Table**: `#table(...)`
- **Formula**: `#mi(...)`, `#mitex(...)`

**处理规则**:

1. **Figure处理**
   - 只提取`caption`的文本内容
   - 在Word文档中插入图注文本
   - **不插入实际图片**

2. **Table处理**
   - 提取`caption`文本内容并插入Word
   - 解析表格内容并在caption下方插入新表格

3. **Formula处理**
   - 提取原始LaTeX代码字符串
   - 将LaTeX代码原样插入Word文档对应位置

**定位原则**: 以Typst文本中的标题和元素caption作为定位锚点，确保元素被放置在正确的章节下

### 第四步：填充正文文本

**目标**: 完成文档最后的文本填充

**内容识别规则**:

需要识别并插入的"普通正文"是指不属于以下类别的文本：
- 标题 (`= ...`, `== ...`)
- 图块 (`#figure(...)`)
- 表块 (`#table(...)`)
- 公式块 (`#mi(...)`, `#mitex(...)`)
- 引用块 (`#bibliography(...)`)
- 代码块 (```...```)

**插入逻辑**:
- 遍历processed_typst_content
- 将识别出的普通正文段落作为新段落添加到Word文档
- 保持原始段落划分（Typst中的空行代表新段落）
- 确保文本出现在正确的标题章节下

## 使用示例

### 完整命令序列

```bash
# 假设输入文件: paper.typ, 模板: template.docx, 参考文献库: references.bib

# 步骤1: 处理引用
python generate_citation_mapping.py references.bib -o 引用映射表.md
python replace.py paper.typ -o 引用映射表.md -a
python apply_citation_mapping.py 引用映射表.md paper.typ -o paper_processed.typ

# 步骤2-4: 使用MCP服务器完成文档转换
# (通过word-document-server MCP服务器执行)
```

### 人工检查点

在每个主要步骤完成后，建议进行人工检查：

1. **步骤1后**: 检查引用处理结果，确保引用格式正确
2. **步骤2后**: 验证文档结构是否完整，标题级别是否正确
3. **步骤3后**: 确认特殊元素（图、表、公式）位置和格式
4. **步骤4后**: 最终文档完整性检查

## 故障排除

### 常见问题

1. **引用处理失败**
   - 检查BibTeX文件格式是否正确
   - 确认Python脚本路径和权限

2. **Word模板问题**
   - 确保模板文件包含所需的样式（MS Title, Authors等）
   - 验证模板文件可正常打开

3. **特殊元素识别失败**
   - 检查Typst语法是否正确
   - 确认元素标记格式符合预期

4. **文本插入位置错误**
   - 验证标题识别逻辑
   - 检查元素锚点定位是否准确

## 最佳实践

1. **文件管理**
   - 始终在副本上操作，保留原始文件
   - 使用有意义的文件命名规范

2. **质量控制**
   - 在每个步骤后进行验证
   - 保留中间文件用于调试

3. **模板准备**
   - 准备标准化的Word模板
   - 确保模板包含所有必要的样式

4. **引用管理**
   - 保持BibTeX文件的整洁和一致性
   - 定期更新引用数据库

## 扩展功能

该工作流设计为模块化结构，可以根据需要扩展：
- 支持更多文档元素类型
- 添加自动化测试步骤
- 集成版本控制系统
- 支持批量处理多个文件

---

*该工具集成了Typst到Word转换的完整流程，确保格式保真度和结构完整性。*