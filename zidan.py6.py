# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 10:26:52 2024

@author: ASUS
"""

n = int(input ("berapa banyak = ") )
for baris in range (n,0,-1):
    for kolom in range (baris):
        print (baris,end='')
    print ()
    