#!C:\Users\SW\anaconda3\envs\py3\python.exe
# -*- coding: utf-8 -*-

import cgi, os

form = cgi.FieldStorage()
pageId = form['pageId'].value
title = form['title'].value
description = form['descr'].value

opened_file = open(f'data/{pageId}', 'w')
opened_file.write(description)
opened_file.close()

os.rename(f'data/{pageId}', f'data/{title}')

# Redirection
print(f"Location: index.py?id={title}")
print()