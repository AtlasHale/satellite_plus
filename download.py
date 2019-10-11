import numpy as np
import pandas as pd
import os
from satsearch import Search
import imageio as im
from PIL import Image
import re

# os.environ['SATUTILS_API_URL'] = "https://sat-api.developmentseed.org/"
# search = Search(bbox=[-121.671912, 39.789597, -121.566920, 39.720973],
#                datetime='2018-10-30/2018-11-07',
#                property=["eo:cloud_cover < 30"])
# print('bbox search: %s items' % search.found())
#
# items = search.items()
# items.save('camp-fire.json')
# items.download('B4')
# items.download('B3')
# items.download('B2')
#print(items.summary())
search = Search(bbox=[-110, 39.5, -105, 40.5])
print('bbox search: %s items' % search.found())
items = search.items()
print(type(items))
items.save('test.json')
items.download('B4')
items.download('B3')
items.download('B2')
files = os.listdir()
for file in files:
    if 'B2.TIF' in file:
        os.rename(file, 'B2.TIF')
    if 'B3.TIF' in file:
        os.rename(file, 'B3.TIF')
    if 'B4.TIF' in file:
        os.rename(file, 'B4.TIF')

print(files)

# Read all bands into numpy array and reduce to 8 bit
r = np.array([.5], dtype='float64')
print(r.nbytes)
r = np.interp(im.imread("B2.TIF"),
              (np.iinfo(np.uint16).min, np.iinfo(np.uint16).max),
              (np.iinfo(np.uint8).min, np.iinfo(np.uint8).max))
g = np.interp(im.imread("B3.TIF"),
              (np.iinfo(np.uint16).min, np.iinfo(np.uint16).max),
              (np.iinfo(np.uint8).min, np.iinfo(np.uint8).max))
b = np.interp(im.imread("B4.TIF"),
              (np.iinfo(np.uint16).min, np.iinfo(np.uint16).max),
              (np.iinfo(np.uint8).min, np.iinfo(np.uint8).max))

# dstack combines the 3 NxM arrays into 1 NxMx3 array
m = np.dstack((r,g,b))

# Generate and save the image from the array.
img = Image.fromarray(m.astype('uint8'))
img.save("sample_rgb.jpg")
