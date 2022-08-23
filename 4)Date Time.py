# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:41:41 2022

@author: Pranav Varanasi
"""
#Date Time in a Specific format
from datetime import datetime as dt
cur=dt.now()
print(cur.strftime(' %a %m %H:%M:%S IST %Y'))