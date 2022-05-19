from skeleton import coordinates
from tkinter import *
import time


window = Tk()   # Create Window object

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)  # Creating Canvas

canvas.pack()


def create_circle(x, y, r, canvasName):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill="#000")


# coordinates = abrar.generateCoordinates()
for coordinate in coordinates:
    create_circle(coordinate[0], coordinate[1], 1, canvas)
    window.update()
    time.sleep(0.01)

window.mainloop()
