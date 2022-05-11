from tkinter import *
import textCoordinate
root = Tk()
myCanvas = Canvas(root)
myCanvas.config(width=500, height=500)
myCanvas.pack()


def create_circle(x, y, r, canvasName):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill="#000")


coordinates = textCoordinate.generateCoordinates()
for coordinate in coordinates:
    create_circle(coordinate[0], coordinate[1], 1, myCanvas)

root.mainloop()
