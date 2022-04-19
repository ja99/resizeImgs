import glob
from PIL import Image

NEW_WIDTH = 500

for file in glob.iglob(f'images/**/*.png', recursive=True):
    image = Image.open(file)
    aspect_ratio = image.size[1] / image.size[0]
    new_height = int(NEW_WIDTH * aspect_ratio)

    new_image = image.resize((NEW_WIDTH, new_height))
    new_image.save(file)
