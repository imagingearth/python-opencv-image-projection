# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 23:33:17 2015

@author: Adam Steer

shows an image with entropy calculated over some radius
"""

import matplotlib.pyplot as plt

from skimage import data
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.util import img_as_ubyte

#import an image
img = io.imread('test_2_0126_subset.jpg')

#get a band, make it unsigned bytes
redband = img[:,:,0]
image = img_as_ubyte(redband)

#start a figure
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(10, 4))

#plot the image
img0 = ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title('Image')
ax0.axis('off')
fig.colorbar(img0, ax=ax0)

#compute its entropy and plot it
img1 = ax1.imshow(entropy(image, disk(5)), cmap=plt.cm.jet)
ax1.set_title('Entropy')
ax1.axis('off')
fig.colorbar(img1, ax=ax1)

plt.show()
