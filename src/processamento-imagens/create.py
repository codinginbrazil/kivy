import os
from PIL import Image

def create(size):
    image = Image.new("RGB", (size, size), (255, 255, 255) )
    for x in range(size):
        for y in range(size):
            if x < y:
                image.putpixel((x,y), (0, 0, 0))
    return image

image = create(500)
image.show()
image.save(os.path.join("image", "black-white.jpg"))
