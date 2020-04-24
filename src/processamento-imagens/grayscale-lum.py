from PIL import Image

img_color = Image.open("image/logo.png")

def grayscale_lum(colored):
    w, h = colored.size
    img = Image.new("P", (w, h))

    for x in range(w):
        for y in range(h):
            pixel = colored.getpixel((x,y))
            lum = int(0.3*pixel[0] + 0.59*pixel[1] + 0.11*pixel[2])
            img.putpixel((x,y), (lum, lum, lum))
    return img

image = grayscale(img_color)
image.show()