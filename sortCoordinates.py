from skeleton import coordinates
import numpy as np

# Find the closest ccordinate to the origin


def findInitialPoint(unsortedArray):
    origin = np.array((0, 0))
    distances = np.linalg.norm(unsortedArray-origin, axis=1)
    min_index = np.argmin(distances)
    initialPoint = unsortedArray[min_index]
    unsortedArray = np.delete(unsortedArray, min_index, 0)
    return (initialPoint, unsortedArray)

# Generate the sorted array


def generateSortedArray(initialPoint, unsortedArray):
    sorted_array = [initialPoint]
    for element in unsortedArray:
        origin = initialPoint
        distances = np.linalg.norm(unsortedArray-origin, axis=1)
        min_index = np.argmin(distances)
        initialPoint = unsortedArray[min_index]
        sorted_array.append(initialPoint)
        unsortedArray = np.delete(unsortedArray, min_index, 0)
    return sorted_array


unsortedArray = np.array(coordinates)  # Conevrt the list into numpy array

initialPoint, unsortedArray = findInitialPoint(unsortedArray)
sortedArray = generateSortedArray(initialPoint, unsortedArray)
