"""

    Creating a Simple Website with Python 🐍
    Github :: PCabralSoftware - 2K18 - Twitter :: @pedrogcabral

"""

# Import DOM and HTML Tags from Browser
from browser import document
from browser import html

# Navigation Div
nav = html.DIV('Python 🐍', Class="nav")

# Content Div
cnt = html.DIV('You can do really awesome stuff using Python!', Class="content")

# Footer Div
ftr = html.DIV('Thank You', Class="footer")

# "Render" it!
document <= [nav, cnt, ftr]