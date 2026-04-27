
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
\setlength{\parindent}{0pt}             
\setlength{\parskip}{0.6\baselineskip}  
\linespread{1.15}                       

% ==========================================
% NXP / 欧美经典硬件手册一级标题样式 (Classic Tech Manual)
% ==========================================
\usepackage{titlesec}
\titleformat{\chapter}[display]
  {\normalfont\sffamily\Huge\bfseries\raggedright}
  {Chapter \thechapter}
  {0.5ex}
  {}
  [\vspace{1ex}\titlerule]
\titlespacing*{\chapter}{0pt}{-30pt}{30pt}

% ==========================================
% 修复表格列宽分配不均导致表头文字截断
% ==========================================
\setlength{\tymin}{45pt}

% ==========================================
% 统一页脚样式：仅显示页码（右下角）
% ==========================================
\usepackage{fancyhdr}
\pagestyle{fancy}

% 清空所有默认的页眉页脚内容（移除左边的章节标题等）
\fancyhf{}

% 仅在右下角显示页码
\fancyfoot[R]{\thepage}

% 移除页眉和页脚的分隔线
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% 【关键】让章节首页（plain 样式）也使用相同的简洁页脚
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[R]{\thepage}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}

% ==========================================
% Professional PDF Styling (Sphinx Setup)
% ==========================================
\sphinxsetup{
    hmargin={1in,1in},         
    vmargin={1in,1in},         
    TitleColor={rgb}{0,0,0},   
    InnerLinkColor={rgb}{0.0,0.3,0.7}, 
    OuterLinkColor={rgb}{0.0,0.3,0.7}, 
    verbatimwithframe=false,   
    verbatimwrapslines=true,   
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
\renewcommand{\_}{\textunderscore\allowbreak}
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
