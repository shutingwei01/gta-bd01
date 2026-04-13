
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
    
    # [修改点 1]：强制英文版也使用与中文版统一的 Sonny 章节标题样式
    'fncychap': r'\usepackage[Sonny]{fncychap}',
    
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
% Remove Chinese indent style, use standard English paragraph spacing
\setlength{\parindent}{0pt}             % No first-line indent
\setlength{\parskip}{0.6\baselineskip}  % Add space between paragraphs
\linespread{1.15}                       % Slightly increase line height for readability

% ==========================================
% Professional PDF Styling (Sphinx Setup)
% ==========================================
\sphinxsetup{
    hmargin={1in,1in},         % Standard 1-inch left/right margins
    vmargin={1in,1in},         % Standard 1-inch top/bottom margins
    TitleColor={rgb}{0,0,0},   % Keep titles clean black
    InnerLinkColor={rgb}{0.0,0.3,0.7}, % Professional blue for internal links (TOC, cross-refs)
    OuterLinkColor={rgb}{0.0,0.3,0.7}, % Professional blue for URLs
    verbatimwithframe=false,   % Remove ugly borders around code blocks
    verbatimwrapslines=true,   % Automatically wrap long code lines
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
% [修改点 2 & 3]：修复表格长字符串溢出与表头加粗
% ==========================================
% 重新定义下划线，让 LaTeX 遇到下划线时允许自动换行
\renewcommand{\_}{\textunderscore\allowbreak}

% 重写 Sphinx 的表头样式，加入 \bfseries (加粗) 指令
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
