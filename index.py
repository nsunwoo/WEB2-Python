#!C:\Users\SW\anaconda3\envs\py3\python.exe
# -*- coding: utf-8 -*-
print("Content-Type: text/html")
print()

import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open(f'data/{pageId}', 'r', encoding='utf-8').read()
    description = description.replace('<', '&lt;')
    description = description.replace('>', '&gt;')
    update_link = f'<a href="update.py?id={pageId}">update</a>'
    delete_action = f'''<form action="process_delete.py" method="post">
        <input type="hidden" name="pageId" value="{pageId}">
        <input type="submit" value="delete">
    </form>'''
else:
    pageId = 'Welcome'
    description = '웹이에요.'
    update_link = ''
    delete_action = ''

print(f'''<!DOCTYPE html>
<html>
<head>
    <title>WEB1 - Welcome</title>
    <meta charset="euc-kr">
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
        {view.getList()}
    </ol>
    <a href="create.py">create</a>
    {update_link}
    {delete_action}
    <h2>{pageId}</h2>
    <p>{description}</p>
</body>
</html>''')