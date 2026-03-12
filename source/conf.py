project = 'GTA1000 Series Documentation'
copyright = '2026, Giantec'
author = 'Hardware Team'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'myst_parser',
]

source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown'}
templates_path = ['_templates']
exclude_patterns = []
language = 'zh_CN'

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
}
html_static_path = ['_static']
html_css_files = ['custom.css']

todo_include_todos = True
autosectionlabel_prefix_document = True

numfig = True
numfig_secnum_depth = 1
numfig_format = {
    'figure': '图 %s',
    'table': '表 %s',
    'code-block': '代码 %s'
}

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '12pt',
    'preamble': r'''
\usepackage{xeCJK} % 启用 xeCJK 来支持 CJK 字体
\setmainfont{DejaVu Sans} % 设置主字体（你可以替换为系统中的任何中文字体，如 Songti SC, KaiTi, Microsoft YaHei 等）
\setCJKmainfont{SimSun} % 设置中文字体，例如：思源宋体 Source Han Serif CN, 或 Windows 上的 SimSun (宋体)
\xeCJKsetup{CJKmath=true} % 确保数学公式中的中文也正常
\usepackage{indentfirst} % 首行缩进
\setlength{\parindent}{2em} % 设置段落首行缩进两个汉字
\usepackage{ragged2e} % 左对齐环境
\RaggedRight % 全局左对齐，不使用两端对齐
''',
    'figure_align': 'htbp',
}

latex_documents = [
    ('index', 'GTA1000_MicBoard_UserGuide.tex', 'GTA1000 Series 麦克风板用户指南',
     'Giantec Hardware Team', 'manual'),
]