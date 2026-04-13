
# conf.py

# ... (文件顶部保持不变，如 Python 路径设置等) ...

# -- Project information -----------------------------------------------------

project = 'GTA1000 Series Documentation'
copyright = '2026, Giantec'
author = ''
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'myst_parser',
    'sphinx_simplepdf',  # Keep this extension for local build
]

source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown'}
templates_path = ['_templates']
exclude_patterns = []
language = 'en'

# -- MyST-Parser Configuration -----------------------------------------------
myst_enable_extensions = [
    "dollarmath",   
    "amsmath",      
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
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Listing %s'
}

# -- Options for LaTeX output --------------------------------------------------

latex_engine = 'xelatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    
    # 彻底禁用自带的旧版双横线章节排版
    'fncychap': '',
    
    'preamble': r'''
% --- Font settings ---
\usepackage{xeCJK}

\renewcommand{\familydefault}{\sfdefault}
\setmainfont{Noto Serif}       
\setsansfont{Noto Sans}        
\setmonofont{Noto Sans Mono}   
\setCJKmainfont{Noto Serif CJK SC} 
\setCJKsansfont{Noto Sans CJK SC}  
\setCJKmonofont{Noto Sans CJK SC}  
\xeCJKsetup{CJKmath=true} 

% ==========================================
% English Typography Standard Settings
% ==========================================
% 取消首行缩进，采用段落间距，增加行距
\setlength{\parindent}{0pt}             
\setlength{\parskip}{0.6\baselineskip}  
\linespread{1.15}                       

% ==========================================
% NXP / 欧美经典硬件手册一级标题样式 (Classic Tech Manual)
% ==========================================
\usepackage{titlesec}
\titleformat{\chapter}[display]
  {\normalfont\sffamily\Huge\bfseries\raggedright}  % 全局巨大、加粗、无衬线字体、左对齐
  {Chapter \thechapter}                             % "Chapter X" 使用相同的巨大字体，保持视觉统一
  {0.5ex}                                           % 极小的间距，让章节号和标题文字紧密相连
  {}                                                % 紧接具体的标题内容
  [\vspace{1ex}\titlerule]                          % 在标题正下方加一条贯穿页面的粗实线，稳住排版重心
\titlespacing*{\chapter}{0pt}{-30pt}{30pt}          % 压缩顶部留白，预留底部空间

% ==========================================
% Professional PDF Styling (Sphinx Setup)
% ==========================================
\sphinxsetup{
    hmargin={1in,1in},         % 国际标准的 1 英寸页边距
    vmargin={1in,1in},         
    TitleColor={rgb}{0,0,0},   % 标题纯黑
    InnerLinkColor={rgb}{0.0,0.3,0.7}, % 目录、交叉引用使用专业蓝色
    OuterLinkColor={rgb}{0.0,0.3,0.7}, % URL 使用专业蓝色
    verbatimwithframe=false,   % 移除代码块多余边框
    verbatimwrapslines=true,   % 代码自动换行
}

% --- Special character handling ---
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

% ==========================================
% 表格深度优化：修复溢出与表头加粗
% ==========================================
% 重新定义下划线，让 LaTeX 遇到长下划线字符串（如寄存器名/料号）时允许自动换行
\renewcommand{\_}{\textunderscore\allowbreak}
% 强制 Sphinx 生成的表格表头使用加粗的无衬线字体
\renewcommand{\sphinxstyletheadfamily}{\bfseries\sffamily}

% ==========================================
% Force hide author and date on the cover page
% ==========================================
\makeatletter
\renewcommand{\author}[1]{\gdef\@author{}}
\renewcommand{\date}[1]{\gdef\@date{}}
\makeatother
% ==========================================
''',
    'extraclassoptions': 'openany,oneside', 
    'figure_align': 'H',
}

# We replaced the original author with an empty string ''
latex_documents = [
    ('index', f'GTA1000_MicBoard_UserGuide_V{release}.tex', 'GTA1000 Mic Board User Guide',
     '', 'manual'),
]

# -- Options for simplepdf output --------------------------------------------
simplepdf_title = project + ' Mic Board User Guide'
simplepdf_use_toc = True
simplepdf_stylesheets = ['_static/simplepdf.css']
today = ''
