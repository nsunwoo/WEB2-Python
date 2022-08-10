import os, html_sanitizer

def getList():
    sanitizer = html_sanitizer.Sanitizer()
    files = os.listdir('data')
    listStr = ''
    for item in files:
        item = sanitizer.sanitize(item)
        listStr = listStr + f'<li><a href="index.py?id={item}">{item}</a></li>\n\t\t'
    return listStr