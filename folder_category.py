#!/usr/bin/python
#-*- coding:UTF-8 -*-

        #此代码功能, 首先打开目录下的xml文件，查看其所属类别，然后按其类别建立文件夹，移动至所属类别文件夹内
        #2021.1.14

import os
import xml.etree.ElementTree as ET
import shutil

Path = 'V:\\Coding\\Thyroid_9long\\2ndTraining\\source_dataset\\1'
Type = 'xml'
Attrib = 'name'

class classify_folder:
    counts = 0;
    def __init__(self, path, type, attribute):
        self.path = path
        self.type = type
        self.attribute = attribute
    
    def classifying(self):
        for file in os.listdir(self.path):
            if file.endswith(self.type):
                tree = ET.parse(self.path + '\\' + file)
                root = tree.getroot()
                for son in root.iter(self.attribute):
                    source_path = self.path + '\\' + file
                    move_path = self.path + '\\' + son.text
                    if not os.path.exists(move_path):
                        os.mkdir(move_path)
                shutil.copy(source_path, move_path)
                classify_folder.counts += 1;

def main():
    work = classify_folder(Path, Type, Attrib)
    work.classifying()

if __name__ == '__main__':
    main()
    print(classify_folder.counts)