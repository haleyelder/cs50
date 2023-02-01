# NOTE: image references are found on the pset page, all cases passed -- https://cs50.harvard.edu/python/2022/psets/6/shirt/

import sys
from os import path
import os
from PIL import Image, ImageOps

firstArg = os.path.splitext(sys.argv[1])

if firstArg[1] != ".jpg" and firstArg[1] != ".jpeg" and firstArg[1] != ".png":
    sys.exit("Invalid output")

if (len(sys.argv) < 2):
    sys.exit("Too few command-line arguments")
elif (len(sys.argv) > 3):
    sys.exit("Too many command-line arguments")
elif not path.exists(sys.argv[1]):
    sys.exit("File does not exist")

elif (len(sys.argv) == 3):
    secondArg = os.path.splitext(sys.argv[2])

    if firstArg[1] != secondArg[1]:
        sys.exit("Input and output have different extensions")
    else:
        # open both pics
        shirt = Image.open("shirt.png")
        muppetPic = Image.open(sys.argv[1])

        # crop and resize before/muppet pic
        muppetCropped = ImageOps.fit(muppetPic, shirt.size, Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

        # paste shirt over muppet croppped image
        muppetCropped.paste(shirt, box=None, mask=shirt)

        # save new pic as 2nd CLI arg name
        muppetCropped.save(sys.argv[2])