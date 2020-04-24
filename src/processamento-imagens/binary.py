import os
from PIL import Image

mono = Image.open("image/logo-mono.png")

def binary(grayscale, threshold):
    w, h = grayscale.size
    img = Image.new("L", (w, h), (255) )

    for x in range(w):
        for y in range(h):
            pixel = grayscale.getpixel((x,y))
            if (pixel[0] < threshold):
                img.putpixel((x,y), (0))
    return img

image = binary(mono,127)
image.show()
image.save(os.path.join("image", "binary.jpg"))