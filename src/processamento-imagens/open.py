from PIL import Image

image = Image.open("image/logo.png")

cordinate = (300,300)
print( image.getpixel(cordinate) )

image.show()
