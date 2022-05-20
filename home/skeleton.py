from cv2 import threshold, imread, imshow, resize, THRESH_BINARY_INV, cvtColor, COLOR_BGR2GRAY, waitKey
from skimage.morphology import skeletonize
from skimage.color import rgb2gray

# import and resize image
image = imread('images/anya.jpg')
resizedImage = resize(image, (600, 600))
# grayimage = cvtColor(image, COLOR_BGR2GRAY)    # Convert the image into grayscale
# grayimage = rgb2gray(image)

ret, invertedBinimage = threshold(
    resizedImage, 127, 255, THRESH_BINARY_INV)  # Invert the binary image

skeleton = skeletonize(invertedBinimage)   # perform skeletonization

# Coordinate Store in list
coordinates = []
for y in range(0, skeleton.shape[0]):
    for x in range(0, skeleton.shape[1]):
        if skeleton[y][x][0] == 0 and skeleton[y][x][1] == 255 and skeleton[y][x][2] == 0:
            coordinates.append([x, y])
