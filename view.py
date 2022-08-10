import os

def getList():
    files = os.listdir('data')
    listStr = ''
    for item in files:
        listStr = listStr + f'<li><a href="index.py?id={item}">{item}</a></li>\n\t\t'
    return listStr