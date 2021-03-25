import numpy as np
from skimage.io import imread, imsave
import matplotlib.pyplot as plt
from skimage import transform
from skimage.transform import rotate, AffineTransform
from skimage.util import random_noise
from skimage.filters import gaussian
from scipy import ndimage
# load Image
img = imread('./butterfly.jpg') / 255
# plot original Image
plt.imshow(img)

rotate30 = rotate(img, angle=30)
rotate45 = rotate(img, angle=45)
rotate60 = rotate(img, angle=60)
rotate90 = rotate(img, angle=90)
fig = plt.figure(tight_layout='auto', figsize=(10, 7))
fig.add_subplot(221)
plt.title('Rotate 30')
plt.imshow(rotate30)
fig.add_subplot(222)
plt.title('Rotate 45')
plt.imshow(rotate45)
fig.add_subplot(223)
plt.title('Rotate 60')
plt.imshow(rotate60)
fig.add_subplot(224)
plt.title('Rotate 90') 
plt.imshow(rotate90)
	
# image shearing using sklearn.transform.AffineTransform
# try out with differnt values of shear 
tf = AffineTransform(shear=-0.5)
sheared = transform.warp(img, tf, order=1, preserve_range=True, mode='wrap')
sheared_fig = plot_side_by_side(img, sheared, 'Original', 'Sheared')
plot.show()
 
# Image rescaling with sklearn.transform.rescale
rescaled = transform.rescale(img, 1.1)
rescaled_fig = plot_side_by_side(img, rescaled, 'Original', 'Rescaled')
plt.show()
print('Original Shape: ',img.shape)
print('Rescaled Shape: ',rescaled.shape)


