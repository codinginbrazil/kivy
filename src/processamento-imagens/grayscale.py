import os
from PIL import Image

img_color = Image.open("image/logo.png")

def grayscale(colored):
    w, h = colored.size
    img = Image.new("P", (w, h))

    for x in range(w):
        for y in range(h):
            pixel = colored.getpixel((x,y))
            lum = (pixel[0] + pixel[1] + pixel[2])//3
            img.putpixel((x,y), (lum, lum, lum))
    return img

image = grayscale(img_color)
image.show()
image.save(os.path.join("image", "logo-mono.png"))