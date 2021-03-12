###########################################################################
#机器学习研发，苏州思翠人工智能研究所
#coding on 2021-3-10
#此代码主要是数据清洗，将文件中的名字缺损和文件命名方式统一
#首先爬取xml文件的属性信息，将未命名的文件命名；其次是将图片信息统一
###########################################################################

#!/usr/bin/python
#-*- coding:UTF-8 -*-

import os
import cv2
import shutil
from PIL import Image
import numpy as np
import xml.etree.ElementTree as ET

Root_Path = 'V:\\Coding\\Faster_RCNN(Project_1)\\SecondTest\\source'
Img_Type = 'jpg'
Img_Type_bmp = 'bmp'
Xml_Type = 'xml'

class modifing:
    def __init__(self, root_path, xml_type, img_type, img_type_bmp):
        self.root_path = root_path
        self.xml_type = xml_type
        self.img_type = img_type
        self.img_type_bmp = img_type_bmp

    def searching_file(self):
        for Root, Floders, Files in os.walk(self.root_path):
            for floder in Floders:
                floder_path = os.path.join(Root, floder)

                #调用函数，将Image改为jpg格式
                work_2 = To_jpg(self.img_type, self.img_type_bmp, self.xml_type, floder_path)
                work_2.img_rename()

                #调用函数，改动xml相关信息
#                self.modify_file(floder_path)                                                              

    #将xml文件的名字重新定义
    def modify_file(self, path):
        for file in os.listdir(path):
            if file.endswith(self.xml_type):                                                               #判断是否，为xml文件
                file_path = os.path.join(path, file)                                                       #源文件xml路径
                
                xml_file_name = os.path.splitext(file)[0]                                                  #xml的文件名字
                tree = ET.parse(file_path)
                xml_root = tree.getroot()
                for xml_name in xml_root.iter('filename'):
                    source_name = os.path.splitext(xml_name.text)[0]                                       #xml中filename属性的值
                    name_list = list(source_name)                                                          #首先将str转换成list，方便后面判断list中每一位的值
                    self.clear_nonInfo(name_list)                                                          #改写名称，去除其中干扰信息
                    clear_name = "".join(name_list)                                                        #将list改为字符串

                    if xml_file_name != clear_name:                                                        #判断xml文件名是否符合条件
                        new_name_path = os.path.join(path, clear_name + '.' + self.xml_type)               #新命名的xml文件
                        shutil.move(file_path, new_name_path)                                      
    
    #用于改写名称，去除其中干扰信息
    def clear_nonInfo(self, list_temp):                                                           
        for p in list_temp:
            if p==' ':
                list_temp.remove(p)
            elif p=='_':
                list_temp.remove(p)
            elif p.isspace():
                list_temp.remove(p)                              
            elif p=='\t':
                list_temp.remove(p)

#图像数据转换，由于采用PIL和OPENCV函数，将BMP转换成JPG时都会有损，部分代码功能如bmp->jpg暂时搁置。
class To_jpg:
    def __init__(self, Img_Type, img_Type_bmp, Xml_Type, image_path):
        self.Img_Type = Img_Type
        self.img_Type_bmp = img_Type_bmp
        self.Xml_Type = Xml_Type
        self.image_path = image_path
    
    def img_rename(self):
        for image_file in os.listdir(self.image_path):
            if image_file.endswith(self.Img_Type) or image_file.endswith(self.img_Type_bmp):
                file_path = os.path.join(self.image_path, image_file)
                img_name = os.path.splitext(image_file)[0]
                img_T = os.path.splitext(image_file)[-1]
                name_list = list(img_name)
                modifing.clear_nonInfo(self, name_list)
                clear_name = "".join(name_list)
                
                if img_name != clear_name:                                                             #判断image文件名是否符合条件
                    new_name_path = os.path.join(self.image_path, clear_name + img_T)                  #新命名的image文件
                    shutil.move(file_path, new_name_path)                    

#     def redefine(self):
#        for img_file in os.listdir(self.image_path):
#            if (not img_file.endswith(self.Img_Type) ) and (not img_file.endswith(self.Xml_Type)):
#                image_name = os.path.splitext(img_file)[0]
#                source_image = os.path.join(self.image_path, img_file)
#                #new_image = os.path.join(self.image_path, image_name + '.' + self.Img_Type)

#                img = cv2.imread(source_image)
#                cv2.imwrite(new_image, image)
                

def main():
    work_1 = modifing(Root_Path, Xml_Type, Img_Type, Img_Type_bmp)
    work_1.searching_file()

if __name__ == '__main__':
    main()