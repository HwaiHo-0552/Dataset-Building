#!/usr/bin/python
#-*-coding:UTF-8-*-
                                #此代码功能是将文件夹下的图片拷贝至所属的类别中
                                #2021.1.14
import os
import xml.etree.ElementTree as ET
import shutil

Cate_path = 'V:\\Coding\\9-long\\data-mammogram\\datasets_4\\source_data'
Img_path = 'V:\\Coding\\9-long\\data-mammogram\\datasets_4\\image'
Type_1 = 'jpg'
Type_2 = 'xml'

class classifying_file:

    def __init__(self, image_path, cate_path, file_type_1, file_type_2):
        self.image_path = image_path
        self.cate_path = cate_path
        self.file_type_1 = file_type_1
        self.file_type_2 = file_type_2

    def classifying(self):
        for root, folders, files in os.walk(self.cate_path):
            for folder in folders:
                folder_path = os.path.join(root, folder)
                
                for img in os.listdir(self.image_path):
                    if img.endswith(self.file_type_1):
                        img_name = os.path.splitext(img)[0]

                        for xml in os.listdir(folder_path):
                            if xml.endswith(self.file_type_2):
                                xml_name = os.path.splitext(xml)[0]

                                if(img_name == xml_name):
                                    img_path = os.path.join(self.image_path, img)
                                    shutil.move(img_path, folder_path)

def main():
    work = classifying_file(Img_path, Cate_path, Type_1, Type_2)
    work.classifying()

if __name__ == '__main__':
    main()