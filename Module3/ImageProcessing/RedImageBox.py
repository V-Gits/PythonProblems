from images.images import Image

width = 200
height = 100
R = 255
G = 127
B = 0
Window = Image(width, height)
for x in range(Window.getWidth()):
    for y in range(Window.getHeight()):
        Window.setPixel(x, y, (R,G,B))
    R-=1
    B+=1
Window.draw()

