#!C:\Users\SW\anaconda3\envs\py3\python.exe
# -*- coding: utf-8 -*-

import cgi, os

form = cgi.FieldStorage()
pageId = form['pageId'].value

os.remove(f'data/{pageId}')

# Redirection
print(f"Location: index.py")
print()