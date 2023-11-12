from PIL import Image
import os

image = Image.open("thug.png")
print(image.getpixel((0,0)))

image.show()