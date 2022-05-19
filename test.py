from cv2 import threshold
from skimage.morphology import skeletonize
from skimage import data
import cv2
from skimage.io import imread, imshow
import matplotlib.pyplot as plt
from skimage.util import invert

# Invert the horse image
# image = data.horse()
# image = cv2.imread('images/r.jpg')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = imread('images/h.jpg')
# ret,image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)
image = invert(image)

# ret,image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)



# perform skeletonization
skeleton = skeletonize(image)

# display results
# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
#                          sharex=True, sharey=True)

# ax = axes.ravel()

# ax[0].imshow(image, cmap=plt.cm.gray)
# ax[0].axis('off')
# ax[0].set_title('original', fontsize=20)

# ax[1].imshow(skeleton, cmap=plt.cm.gray)
# ax[1].axis('off')
# ax[1].set_title('skeleton', fontsize=20)

# fig.tight_layout()
# plt.show()
