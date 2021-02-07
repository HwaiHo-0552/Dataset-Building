#!/usr/bin/python
#-*- coding:UTF-8 -*-

path = 'V:\Coding\9-long\data-mammogram\datasets_4'
source = '已标注700张'
file_1 = 'image'
file_2 = 'label'

import os
import shutil

source_path = os.path.join(path, source)
images = os.path.join(path, file_1)
labels = os.path.join(path, file_2)

'''for content in os.listdir(source_path):
    file_type = os.path.splitext(content)[-1]
    if (file_type =='.jpg'):
        img = os.path.join(source_path,content)
        shutil.move(img, images)'''

for content in os.listdir(images):
    img_name = os.path.splitext(content)[0]
    for con in os.listdir(labels):
        file_name = os.path.splitext(con)[0]

        if(img_name == file_name):
            m_p = os.path.join(images, content)
            shutil.move(m_p, source_path)