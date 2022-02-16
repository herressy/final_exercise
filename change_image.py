#! /usr/bin/env python3

import os
from PIL import Image

home = os.path.expanduser('~')

for image in os.listdir(home + '/supplier-data/images/'):
    if image.endswith(".tiff"):
        im = Image.open(home + '/supplier-data/images/' + image)
        im.convert('RGB').resize((600, 400)).save(home + '/supplier-data/images/' + image.strip('.tiff') + '.jpeg', 'JPEG')
