
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

# -- MyST-Parser 配置 --------------------------------------------------------
# 【新增关键配置】开启 Markdown 中的数学公式支持
myst_enable_extensions = [
    "dollarmath",   # 允许使用 $公式$ 和 $$公式$$ 语法（解决 $\geq$ 不渲染的核心）
    "amsmath",      # 支持高级数学公式环境（如 align, equation 等）
]

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

# 必须指定 xelatex 引擎，这是支持现代中西文字体的前提
latex_engine = 'xelatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': r'''
\usepackage{xeCJK}

% --- 全局字体风格设置 ---
% 现代科技文档通常通篇使用无衬线体 (Sans-serif)。
% 这行代码将 LaTeX 默认的衬线体 (Serif) 切换为无衬线体。
\renewcommand{\familydefault}{\sfdefault}

% --- 1. 设置西文字体 (英文字母、数字、符号) ---
% 备用衬线体 (一般不用，但为了严谨配置上)
\setmainfont{Noto Serif}       
% 核心：正文和标题的西文无衬线体 (整洁、现代)
\setsansfont{Noto Sans}        
% 核心：代码块、终端命令使用的等宽西文字体
\setmonofont{Noto Sans Mono}   

% --- 2. 设置中文字体 (与上述西文字体逐一完美对应) ---
% 备用中文衬线体 (思源宋体)
\setCJKmainfont{Noto Serif CJK SC} 
% 核心：正文和标题的中文无衬线体 (思源黑体，与 Noto Sans 完美融合)
\setCJKsansfont{Noto Sans CJK SC}  
% 核心：代码块中如果出现中文，也保持黑体风格
\setCJKmonofont{Noto Sans CJK SC}  

% --- 3. 中文排版细节优化 ---
\xeCJKsetup{CJKmath=true} % 数学公式中的中文支持
\usepackage{indentfirst}  % 允许首行缩进
\setlength{\parindent}{2em} % 段落首行缩进2个中文字符宽度
\XeTeXlinebreaklocale "zh"  % 中文换行规则
\XeTeXlinebreakskip = 0pt plus 1pt % 允许换行处有微小的字距弹性，使排版更整齐

% --- 4.【新增】Unicode 特殊符号 → LaTeX 数学符号映射 ---
% 双保险：即使您在 .md 文件中直接输入 ≥ ≤ 等 Unicode 字符（不用 $ $ 包裹），
% PDF 也不会再出现方块或空白，LaTeX 会自动将它们转为标准数学符号渲染。
\usepackage{newunicodechar}
\newunicodechar{≥}{\ensuremath{\geq}}
\newunicodechar{≤}{\ensuremath{\leq}}
\newunicodechar{±}{\ensuremath{\pm}}
\newunicodechar{×}{\ensuremath{\times}}
\newunicodechar{÷}{\ensuremath{\div}}
\newunicodechar{≈}{\ensuremath{\approx}}
\newunicodechar{≠}{\ensuremath{\neq}}
\newunicodechar{µ}{\ensuremath{\mu}}
\newunicodechar{Ω}{\ensuremath{\Omega}}
''',
    # 避免单面打印时章与章之间出现多余的空白页
    'extraclassoptions': 'openany,oneside', 
    'figure_align': 'H',
}

latex_documents = [
    ('index', f'GTA1000_MicBoard_UserGuide_V{release}.tex', 'GTA1000 Series 麦克风板用户指南',
     'Giantec Hardware Team', 'manual'),
]
# -----------------------------------------------------------------------------


# -- Options for simplepdf output --------------------------------------------
# (以下配置将保留，当您在本地电脑上运行 sphinx-build -b simplepdf 时会生效，但在 RTD 云端 formats: pdf 构建中不会生效)

simplepdf_title = project + ' 麦克风板用户指南'
simplepdf_use_toc = True
simplepdf_stylesheets = ['_static/simplepdf.css']
