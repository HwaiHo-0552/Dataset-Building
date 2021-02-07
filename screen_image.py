#!/usr/bin/python
#-*- coding:UTF-8 -*-

#由于数据集中一些图片未被标注, 造成图像数量和标注数量不一致, 所以将标签对应的图像筛选出来

import os
import shutil

Path_xml = 'V:\Coding\9-long\data-mammogram\labels'
Path_Img = 'V:\Coding\9-long\data-mammogram\images'
Img_Type = 'jpg'
Xml_Type = 'xml'

class screen_file:
    def __init__(self, xml_path, image_path, img_type, xml_type):
        self.xml_path = xml_path
        self.image_path = image_path
        self.img_type = img_type
        self.xml_type = xml_type

    def screening(self):
        move_path = self.image_path + '\\' + 'JPEGimages'
        if not os.path.exists(move_path):
            os.mkdir(move_path)
        for xml_file in os.listdir(self.xml_path):
            xml_name = os.path.splitext(xml_file)
            for image_file in os.listdir(self.image_path):
                image_name =  os.path.splitext(image_file)
                if image_name[0] == xml_name[0]:
                    source_path = self.image_path + '\\' + image_file
                    shutil.move(source_path, move_path)        

def main():
    work = screen_file(Path_xml, Path_Img, Img_Type, Xml_Type)
    work.screening()

if __name__ == '__main__':
    main()