
from PIL import Image


img = Image.open("test.jpg")

pix = img.load()
print img.size
pixel_values = list(img.getdata())
print pixel_values
file = open("test.txt", "w")
file.write(str(pixel_values))
file.close()
