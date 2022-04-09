import cv2
import numpy as np
from matplotlib import pyplot,image

coordinates = []
image = cv2.imread('images/r.jpg')
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,binimage = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# xy_coords = np.flip(np.column_stack(np.where(grayscale >= 0)), axis=1)
# yx_coords = np.column_stack(np.where(grayscale >= 0))
# print(yx_coords)
for y in range(0,binimage.shape[0]):
    for x in range(0,binimage.shape[1]):
        if binimage[y,x][0] == 0:
            coordinates.append([x,y])
for i in range(0,len(coordinates)):
    print(coordinates[i])

plottedCoord = np.array(coordinates)
# print(plottedCoord[:,1])
# x,y = plottedCoord.T
x = plottedCoord[:,0]
y = plottedCoord[:,1]
pyplot.scatter(x, y,color='black')
# pyplot.imshow(binimage)
pyplot.show()