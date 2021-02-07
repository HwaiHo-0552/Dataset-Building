#!/usr/bin/python
# -*-coding:UTF-8 -*-
                        #由于标注人员将xml文件中folder和name随意乱写, 标签不正确。所以将其改成正确的标签格式

import os
import xml.etree.ElementTree as ET

path = 'V:\Coding\9-long\data-mammogram\datasets_4\label'
Att_1 = 'folder'
Att_2 = 'name'

class modify:
    def __init__(self, path, attribute_1, attribute_2):
        self.path = path
        self.attribute_1 = attribute_1
        self.attribute_2 = attribute_2
    
    def doing(self):
        for file_content in os.listdir(self.path):
            file_type = os.path.splitext(file_content)[-1]
            if(file_type == '.xml'):
                file_path = os.path.join(self.path, file_content)
                tree = ET.parse(file_path)
                root = tree.getroot()

                for son_folder in root.iter(self.attribute_1):
                    for son_name in root.iter(self.attribute_2):
                        son_name.text = son_folder.text
                tree.write(file_path)

def main():
    work_1 = modify(path, Att_1, Att_2)
    work_1.doing()

if __name__ == '__main__':
    main()