from images.images import Image

def blackAndWhite(pic):
    blackPixel = (0,0,0)
    whitePixel = (255, 255, 255)
    for y in range(pic.getHeight()):
        for x in range(pic.getWidth()):
            r,g,b = pic.get