#!/usr/bin/python
#-*- coding: UTF-8 -*-
 
import os
import shutil

Type = 'xml'
Path = 'C:\Coding\Medical Dataset\source_data'
Dict = 'C:\Coding\Faster_RCNN(Project_1)\Annotation'
New_List = ['Root', 'Img2', 'Img3', 'Img4a', 'Img4b', 'Img4c', 'Img5']

class build_new_file:
    def __init__(self, dict, list_file):
        self.dict = dict
        self.list_file = list_file

    def building(self):
        for name in self.list_file:
            if os.path.exists(name):
                print('!ERROR!')
            else:
               os.makedirs(self.dict + '\\' + name) 

class Copy_file:
    i=0;
    def __init__(self, type, path, dict, list_name):
        self.type = type
        self.path = path
        self.dict = dict
        self.list_name = list_name

    def copying(self):
        for root, folder, file in os.walk(self.path):
            if Copy_file.i < len(self.list_name):
                for name in file:
                    source_path = root + '\\' + name
                    if name.endswith(self.type):
                        dict_path = self.dict + '\\' + self.list_name[Copy_file.i]
                        shutil.copy(source_path, dict_path)
                Copy_file.i += 1                  

def main():
    building_file = build_new_file(Dict, New_List)
    building_file.building()

    Copying = Copy_file(Type, Path, Dict, New_List)
    Copying.copying()
            
if __name__ == '__main__':
    main()