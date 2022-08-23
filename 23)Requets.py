# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 14:27:51 2022

@author: Pranav Varanasi
"""
import requests as req
from bs4 import BeautifulSoup
r=req.get('https://www.google.co.in/?hl=te')
print(r.content)
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())