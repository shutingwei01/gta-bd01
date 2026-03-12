project = 'GTA1000 Series Board User Guide'
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

numfig = True               # 开启图片、表格自动编号功能
numfig_secnum_depth = 1     # 编号关联到几级标题？1 表示关联到一级标题 (如 1.1, 1.2)
numfig_format = {
    'figure': '图 %s',      # %s 会被自动替换为 1.1, 1.2 等数字
    'table': '表 %s',
    'code-block': '代码 %s'
}