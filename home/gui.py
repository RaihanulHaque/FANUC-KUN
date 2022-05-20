from skeleton import coordinates
from tkinter import *
import time
from sortCoordinates import sortedArray


def createCircle(x, y, r, canvasName):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill="#000")


window = Tk()   # Create Window object
WIDTH = 600
HEIGHT = 600
canvas = Canvas(window, width=WIDTH, height=HEIGHT)  # Creating Canvas
canvas.pack()

for coordinate in sortedArray:
    createCircle(coordinate[0], coordinate[1], 1, canvas)
    window.update()
    time.sleep(0.006)

window.mainloop()
