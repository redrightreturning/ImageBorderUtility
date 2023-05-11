#Works on every image present in the directory it's called
#Makes an image square based on it's longest size, adding a white border plus a border all around
#Color (white) and border(50) have defaults
#arg 1: the location of the files
#arg 2 (optional): the border to use
#arg 3 (optional): a string of the color ie "black" "blue" etc. Based on Pillow Imaging colors

from sys import argv
from PIL import Image
from os import listdir
from os.path import isfile, join

#Border in pixels
BORDER_DEFAULT = 50
#RGB color
COLOR_DEFAULT = (255, 255, 255)

if len(argv) == 3:
    border = int(float(argv[2]))
else:
    border = BORDER_DEFAULT

if len(argv) == 4:
    color = argv[3]
else:
    color = COLOR_DEFAULT

files = [f for f in listdir(argv[1]) if isfile(join(argv[1], f))]
images = [f for f in files if f.split('.')[1] in ("JPEG", "jpeg", "jpg", "JPG", "png", "PNG") ]

for image in images:
    original = Image.open(argv[1] + "/" + image)

    #Tallest size of image plus a border on each side
    newSize = max(original.width, original.height) + (border * 2)
    newImage = Image.new("RGB", (newSize, newSize), color)
    box = (abs((original.width - newSize) // 2), abs((original.height - newSize) // 2))
    newImage.paste(original, box)

    filenameParts = image.split('.')
    #newImage.show()
    newImage.save(f'{argv[1]}/{filenameParts[0]}_wBorder.{filenameParts[1]}')
