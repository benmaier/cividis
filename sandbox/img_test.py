import numpy as np
from scipy.ndimage import imread
from bfmplot import pl

def rgb2grey(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    grey = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return grey

A = imread('column.png')
A = rgb2grey(A)

pl.imshow(A)
pl.gcf().savefig('column_cividis.png')
pl.show()
