# conf.py

# ... (文件顶部保持不变，如 Python 路径设置等，此处省略) ...

# -- Project information -----------------------------------------------------

project = 'GTA1000 Series Documentation'
copyright = '2026, Giantec'
author = 'Hardware Team'
release = '1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'myst_parser',
    'sphinx_simplepdf',  # !!! 添加这一行，启用 Sphinx-SimplePDF 扩展 !!!
]

source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown'}
templates_path = ['_templates']
exclude_patterns = []
language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
}
html_static_path = ['_static']
html_css_files = ['custom.css'] # 请确保您的 _static/custom.css 文件存在

todo_include_todos = True
autosectionlabel_prefix_document = True

numfig = True
numfig_secnum_depth = 1
numfig_format = {
    'figure': '图 %s',
    'table': '表 %s',
    'code-block': '代码 %s'
}

# --- 注释掉原有的 LaTeX 输出配置，因为我们将使用 Sphinx-SimplePDF 生成 PDF ---
# # -- Options for LaTeX output --------------------------------------------------

# latex_elements = {
#     'papersize': 'a4paper',
#     'pointsize': '12pt',
#     'preamble': r'''
# \usepackage{xeCJK} % 启用 xeCJK 来支持 CJK 字体
# \setmainfont{DejaVu Sans} % 设置主字体（你可以替换为系统中的任何中文字体，如 Songti SC, KaiTi, Microsoft YaHei 等）
# \setCJKmainfont{SimSun} % 设置中文字体，例如：思源宋体 Source Han Serif CN, 或 Windows 上的 SimSun (宋体)
# \xeCJKsetup{CJKmath=true} % 确保数学公式中的中文也正常
# \usepackage{indentfirst} % 首行缩进
# \setlength{\parindent}{2em} % 设置段落首行缩进两个汉字
# \usepackage{ragged2 ελληνική}} % 左对齐环境
# \RaggedRight % 全局左对齐，不使用两端对齐
# ''',
#     'figure_align': 'htbp',
# }

# latex_documents = [
#     ('index', 'GTA1000_MicBoard_UserGuide.tex', 'GTA1000 Series 麦克风板用户指南',
#      'Giantec Hardware Team', 'manual'),
# ]
# -----------------------------------------------------------------------------


# -- Options for simplepdf output --------------------------------------------
# !!! 这是 SimplePDF 的关键配置 !!!

# PDF 文档的标题
# 沿用您项目信息的 title，并添加适当的后缀
simplepdf_title = project + ' 麦克风板用户指南' # 根据您的 latex_documents 标题调整

# 是否在 PDF 首页显示目录
simplepdf_use_toc = True

# 用于设置 PDF 样式的 CSS 文件列表。
# 路径是相对于 conf.py 文件的目录。
# 这里的 '_static/simplepdf.css' 指的是 docs/_static/simplepdf.css
simplepdf_stylesheets = ['_static/simplepdf.css']

# 您还可以添加其他 simplepdf_ 配置，例如：
# simplepdf_fit_width = False # 是否让内容自动适应页面宽度
# simplepdf_break_level = 1 # 在哪个标题级别之后分页
# simplepdf_debug = False # 启用调试模式，可以查看渲染细节