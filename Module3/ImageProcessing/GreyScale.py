from images.images import Image

def greyScale(pic):
    for y in range(pic.getWidth()):
        for x in range(pic.getHeight()):
            r, g, b = pic.getPixel(x, y)
            