import numpy as np
import imageio as im
from PIL import Image


# Read all bands into numpy array and reduce to 8 bit

r = np.interp(im.imread(r"C:\Users\Main\Downloads\B2.TIF"),
              (np.iinfo(np.uint16).min, np.iinfo(np.uint16).max),
              (np.iinfo(np.uint8).min, np.iinfo(np.uint8).max))
g = np.interp(im.imread(r"C:\Users\Main\Downloads\B3.TIF"),
              (np.iinfo(np.uint16).min, np.iinfo(np.uint16).max),
              (np.iinfo(np.uint8).min, np.iinfo(np.uint8).max))
b = np.interp(im.imread(r"C:\Users\Main\Downloads\B4.TIF"),
              (np.iinfo(np.uint16).min, np.iinfo(np.uint16).max),
              (np.iinfo(np.uint8).min, np.iinfo(np.uint8).max))

# dstack combines the 3 NxM arrays into 1 NxMx3 array
m = np.dstack((r,g,b))

# Generate and save the image from the array.
img = Image.fromarray(m.astype('uint8'))
img.save(r"C:\Users\Main\Pictures\sample_rgb.jpg")
