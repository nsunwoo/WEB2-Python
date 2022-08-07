#!C:\Users\SW\anaconda3\envs\py3\python.exe
# -*- coding: utf-8 -*-

import cgi

form = cgi.FieldStorage()
title = form['title'].value
description = form['descr'].value

opened_file = open(f'data/{title}', 'w')
opened_file.write(description)
opened_file.close()

# Redirection
print(f"Location: index.py?id={title}")
print()