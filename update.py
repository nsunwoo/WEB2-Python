#!C:\Users\SW\anaconda3\envs\py3\python.exe
# -*- coding: utf-8 -*-
print("Content-Type: text/html")
print()

import cgi, os

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open(f'data/{pageId}', 'r', encoding='utf-8').read()
else:
    pageId = 'Welcome'
    description = '웹이에요.'

def getList():
    files = os.listdir('data')
    listStr = ''
    for item in files:
        listStr = listStr + f'<li><a href="index.py?id={item}">{item}</a></li>\n\t\t'
    return listStr

print(f'''<!DOCTYPE html>
<html>
<head>
    <title>WEB1 - Welcome</title>
    <meta charset="euc-kr">
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
        {getList()}
    </ol>
    <a href="create.py">create</a>
    <form action="process_update.py" method="post">
        <input type="hidden" name="pageId" value="{pageId}">
        <p><input type="text" name="title" placeholder="제목" value="{pageId}"></p>
        <p><textarea rows="4" name="descr" placeholder="설명">{description}</textarea></p>
        <p><input type="submit"></p>
    </form>
</body>
</html>''')