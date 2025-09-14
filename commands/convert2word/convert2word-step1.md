# Word转换Prompt 1: 处理引用



找到citation_tools文件夹，内含三个py程序和bib文件：

这是用来转换一个typst文件引用格式的方法，注意把中间文件留在文件夹内，但最终的转换结果放在typst文件同目录，依次运行：

1. ` python generate_citation_mapping.py <bibtex_file> [选项]`
    参数:
    bibtex_file          BibTeX文件路径
    选项:
    -h, --help           显示此帮助信息
    -o, --output         输出Markdown文件路径（默认: 引用映射表.md）
    -v, --verbose        显示详细信息
    -a, --append         追加到输出文件而不是覆盖

2. `python replace.py <input_file> [选项]`
    参数:
    input_file           typst文件路径
    选项:
	-h, --help           显示此帮助信息
    -o, --output         输出Markdown文件路径（默认: 引用映射表.md）
    -v, --verbose        显示详细信息
    -a, --append         追加到输出文件而不是覆盖（需要使用）

3. `python apply_citation_mapping.py <mapping_file> <input_file> [选项]`
    参数:
    mapping_file          引用映射表文件路径（Markdown或JSON格式）
    input_file           要处理的输入文件路径
    选项:
    -h, --help           显示此帮助信息
    -o, --output         输出文件路径（可选，默认输出到控制台）
    --json FILE          将映射表保存为JSON格式到指定文件
    --preview            仅预览更改，不实际处理文件
    --max-preview NUM    预览的最大更改数量（默认: 10）
    -v, --verbose        显示详细信息
