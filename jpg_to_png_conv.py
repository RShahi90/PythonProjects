import sys
import os
from PIL import Image

args = sys.argv

files = os.listdir(args[1])
if not os.path.exists(args[2]):
    os.mkdir(args[2])
path_image = args[1]
for i in files:
    img = Image.open(path_image+i)
    clean_name_file = os.path.splitext(i)
    new_file = args[2] + clean_name_file[0] + '.png'
    img.save(new_file, "png")
