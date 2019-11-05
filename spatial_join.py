# -*- coding: utf-8 -*-
"""

This is a temporary script file.
"""
# Import the necessary modules
from  osgeo import ogr, osr
import pandas as pd
import numpy as np
import json

p = pd.read_csv(r'C:\Users\Main\Desktop\locs\perim.csv')
o = pd.read_csv(r'C:\Users\Main\Desktop\locs\origin.csv')
p = p[(p['YEAR_'] > 2014) & (p['CAUSE'] == 14)]
o = o[o['YEAR_'] > 2014]
o['ALARM_DATE'] = pd.to_datetime(o.ALARM_DATE, format='%Y%m%d')
o.ALARM_DATE.value_counts()

driver = ogr.GetDriverByName('ESRI Shapefile')
shp = driver.Open(r'C:\Users\Main\Desktop\locs\here\firep18_1.shp')

# Get Projection from layer
layer = shp.GetLayer()
spatialRef = layer.GetSpatialRef()
print (spatialRef)

# Get Shapefile Fields and Types
layerDefinition = layer.GetLayerDefn()
print(layerDefinition)
inFeature = layer.GetNextFeature()
counter = 0
incidents = []

point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(-121.4347, 39.8134)

ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(-122, 40)
ring.AddPoint(-120,40)
ring.AddPoint(-120,39)
ring.AddPoint(-122,39)
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(ring)

print(type(poly))
print(poly.IsEmpty())
print(poly.Contains(point))
while inFeature:
    shape = inFeature.GetGeometryRef()
    """ get the date attribute for the input feature """
    date = inFeature.GetField('ALARM_DATE')
    date = pd.to_datetime(date)    

    if date:
        if int(inFeature.GetField('CAUSE')) == 14:
            incidents.append(inFeature.GetField('INC_NUM'))
            temp = o[o['ALARM_DATE'] == date] 
            
            lat, long = list(temp.LAT83), list(temp.LON83)
            for i in range(len(lat)):
                x = lat[i]
                y = long[i]
                point = ogr.Geometry(ogr.wkbPoint)
                point.AddPoint(x,y)
                print(x, y, point, sep='\t')
                if shape.Contains(point):
                    print(x, y)
                    print(inFeature.GetField('OBJECTID'))
                    break

    # destroy the input feature and get a new one
    inFeature = None
    inFeature = layer.GetNextFeature()


print ('{:<15}{:<10}{:<10}{:<5}'.format('Name', 'Type', 'Width', 'Precision'))
# Get Feature Count and iterate through the features, showing information.
# The features are the same features which make up the gdb table
# Including ALARM_DATE, the important feature.
for i in range(layerDefinition.GetFieldCount()):
    fieldName =  layerDefinition.GetFieldDefn(i).GetName()
    fieldTypeCode = layerDefinition.GetFieldDefn(i).GetType()
    fieldType = layerDefinition.GetFieldDefn(i).GetFieldTypeName(fieldTypeCode)
    fieldWidth = layerDefinition.GetFieldDefn(i).GetWidth()
    GetPrecision = layerDefinition.GetFieldDefn(i).GetPrecision()
    print ('{:<15}{:<10}{:<10}{:<5}'.format(fieldName, fieldType, str(fieldWidth), str(GetPrecision)))

