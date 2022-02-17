#! /usr/bin/env python3

import os
import requests

home = os.path.expanduser('~')
url = 'http://localhost/upload/'

for image in os.listdir(home + '/supplier-data/images'):
    if image.endswith(".jpeg"):
        with open(home + '/supplier-data/images/' + image, 'rb') as opened:
            r = requests.post(url, files = {'file': opened})