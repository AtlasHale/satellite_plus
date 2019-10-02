    import pandas as pd
    import numpy as np
    import imageio as im
    import matplotlib.pyplot as plt
    from PIL import Image
    
    
    # Read all bands into numpy array and reduce to 8 bit
    
    r = im.imread(r"C:\Users\Main\Downloads\B2.TIF").astype(dtype=np.uint8)
    g = im.imread(r"C:\Users\Main\Downloads\B3.TIF").astype(dtype=np.uint8)
    b = im.imread(r"C:\Users\Main\Downloads\B4.TIF").astype(dtype=np.uint8)
    
    # Store the output shape to create output ndarray
    width = r.shape[0]
    height = r.shape[1]
    
    # Create ndarray to hold the pixel values
    output_array = np.ndarray(shape=(width, height, 3), dtype=np.uint8)
            
    fr = r.flatten()
    fg = g.flatten()
    fb = b.flatten()
    
    merged = np.asarray(list(zip(fr, fg, fb)))
    m = merged.reshape((width, height, 3))
    m.shape
    print(merged)
    img = Image.fromarray(m)
    img.save(r"C:\Users\Main\Pictures\sample_rgb.jpg")
