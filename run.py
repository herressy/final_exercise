#! /usr/bin/env python3

import os
import requests

HOME = os.path.expanduser('~')
URL = 'http://localhost/fruits/'

for description in os.listdir(home + '/supplier-data/descriptions'):
    if description.endswith(".txt"):
        with open(HOME + '/supplier-data/descriptions/' + description) as file:
            fruit_name = os.path.splitext(file)[0]
            data = file.read().split("\n")
            fruit_dic = {
                "name": data[0],
                "weight": int(data[1].strip(" lbs")),
                "description": data[2],
                "image_name": fruit_name + ".jpeg"
            }
            response = requests.post(URL, json=fruit_dic)
            response.raise_for_status()
