#!/usr/bin/python
#-*- coding:UTF-8 -*-

path = 'V:\\Coding\\9-long\\data-mammogram\\datasets_4'

import os
from PIL import Image

for root, folders, files in os.walk(path):
    for folder in folders:
        file_path = os.path.join(root, folder)

        for content in os.listdir(file_path):
            file_name = os.path.splitext(content)[0]
            file_type = os.path.splitext(content)[1]
            
            if file_type == '.bmp':
                files = os.path.join(file_path, content)
                img = Image.open(files)
                new_name = file_name + '.jpg'
                new = os.path.join(file_path, new_name)
                img.save(new)
                os.remove(files)

'''            if file_type == '.JPG':
                old = os.path.join(file_path, content)
                new_name = file_name + '.jpg'
                new = os.path.join(file_path, new_name)
                os.rename(old, new)'''


            