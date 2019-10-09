# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:28:54 2019

@author: Main
"""

from satstac import Catalog, Collection, Item

cat = Catalog.open('https://landsat-stac.s3.amazonaws.com/catalog.json')
print(cat, cat.filename)

col = Collection.open('https://landsat-stac.s3.amazonaws.com/landsat-8-l1/catalog.json')
print(col, col.filename)

item = Item.open('https://landsat-stac.s3.amazonaws.com/landsat-8-l1/111/111/2018-11-30/LC81111112018334LGN00.json')
print(item, item.filename, sep='\n')