from cv2 import threshold, imread, imshow, resize, THRESH_BINARY_INV, waitKey
from skimage.morphology import skeletonize
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
# from skimage import data
# from skimage.io import imread, imshow
# from skimage.util import invert

image = imread('images/name.png')
image = resize(image, (500, 500))
# grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayimage = rgb2gray(image)
ret, invertedBinimage = threshold(image, 127, 255, THRESH_BINARY_INV)
# invimage = invert(binimage)

# perform skeletonization
skeleton = skeletonize(invertedBinimage)

# Coordinate Store in list
coordinates = []
for y in range(0, skeleton.shape[0]):
    for x in range(0, skeleton.shape[1]):
        if skeleton[y][x][1] == 255:
            coordinates.append([x, y])

# display results
# plt.imshow(skeleton)
# plt.show()
# imshow('original',image)
# imshow('Gray',grayimage)
# imshow('Binary',invertedBinimage)
# imshow('Skeleton',skeleton)
# waitKey(0)
