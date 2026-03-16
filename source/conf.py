
# conf.py

# ... (文件顶部保持不变，如 Python 路径设置等) ...

# -- Project information -----------------------------------------------------

project = 'GTA1000 Series Documentation'
copyright = '2026, Giantec'
author = 'Hardware Team'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'myst_parser',
    'sphinx_simplepdf',  # 保留此扩展，供本地构建使用
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

# --- 关键修改：恢复并修正 LaTeX 配置以支持 Read the Docs 云端 PDF 构建 ---
# -- Options for LaTeX output --------------------------------------------------

# 必须指定 xelatex 引擎，这是支持现代中文字体的前提
latex_engine = 'xelatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': r'''
\usepackage{xeCJK}
% 指定使用我们在 .readthedocs.yaml 中通过 apt 安装的 Noto CJK 字体
\setCJKmainfont{Noto Sans CJK SC}
\setCJKsansfont{Noto Sans CJK SC}
\setCJKmonofont{Noto Sans CJK SC}
\xeCJKsetup{CJKmath=true}
\usepackage{indentfirst}
\setlength{\parindent}{2em}
% 优化中文换行
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt
''',
    # 避免单面打印时章与章之间出现多余的空白页
    'extraclassoptions': 'openany,oneside', 
    'figure_align': 'H',
}

latex_documents = [
    ('index', 'GTA1000_MicBoard_UserGuide.tex', 'GTA1000 Series 麦克风板用户指南',
     'Giantec Hardware Team', 'manual'),
]
# -----------------------------------------------------------------------------


# -- Options for simplepdf output --------------------------------------------
# (以下配置将保留，当您在本地电脑上运行 sphinx-build -b simplepdf 时会生效，但在 RTD 云端 formats: pdf 构建中不会生效)

simplepdf_title = project + ' 麦克风板用户指南'
simplepdf_use_toc = True
simplepdf_stylesheets = ['_static/simplepdf.css']
