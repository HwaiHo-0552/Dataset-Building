#!/usr/bin/python
#-*- coding:UTF-8 -*-

import cv2
import os
import shutil

path = 'V:\Coding\Thyroid_9long\JPG'
new_path = 'V:\Coding\Thyroid_9long\JPEGImages'
list_1 = []

class save_image:
    def __init__(self, path, new, list1):
        self.path = path
        self.new = new
        self.list1 = list1

    def resave(self):
        for img in os.listdir(self.path):
            img_path = os.path.join(self.path, img) 
            im = cv2.imread(img_path)
            if im.shape:
                self.list1.append(img)

'''
                Old = os.path.join(self.path, img)
                New = os.path.join(self.new, img)
                shutil.move(Old, New)'''
                
def main():
    work = save_image(path, new_path, list_1)
    work.resave()

    print(len(list_1))

if __name__ == '__main__':
    main()
