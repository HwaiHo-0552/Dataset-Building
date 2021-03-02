#!/usr/bin/python
#-*- coding:UTF-8 -*-
                                               #此段代码是将bounding box中的坐标在原始图像中勾勒，并展示出来
                                               #2021.3.1  思翠人工智能 机器学习研发工程师 

import os
import cv2
import numpy as np
import xml.etree.ElementTree as ET

DataPath = 'V:\Coding\Thyroid_9long\paper\source_dataset'
BB_Path = 'V:\Coding\Thyroid_9long\paper\BoundingBox'
ImgType = 'jpg'
FileType = 'xml'
Type_Up = 'object'
Type_Down = 'bndbox'
Dict_Corner ={}

class draw:
    def __init__(self, data_path, bb_path, img_type, file_type, type_up, type_down, dict_corner):
        self.data_path = data_path
        self.bb_path = bb_path
        self.img_type = img_type
        self.file_type = file_type
        self.type_up = type_up
        self.type_down = type_down
        self.dict_corner = dict_corner

    def working(self):
        #判断，并新建类别名称，以存放显示bounding box的图像
        for root, floders, files in os.walk(self.data_path):
            for floder in floders:
                source_root = os.path.join(root + '\\' + floder)             #原始数据的文件夹路径
                file_path = os.path.join(self.bb_path + '\\' + floder)       #打算存放绘制BoundingBox图像的路径
                if not os.path.exists(file_path):
                    os.mkdir(file_path)
                
                for xml_file in os.listdir(source_root):
                    if xml_file.endswith(self.file_type):                    #判断，并将xml提取出来
                        tree = ET.parse(source_root + '\\' + xml_file)
                        xml_root = tree.getroot()
                        img_name = xml_root.find('filename').text
                        img = cv2.imread(source_root + '\\' + img_name)          #将对应的图像读取出来
                        for child in xml_root.findall(self.type_up):
                            for son in child.find(self.type_down):
                                self.dict_corner[son.tag] = son.text
                            cv2.rectangle(
                                            img,
                                            ( int(self.dict_corner['xmin']), int(self.dict_corner['ymin']) ),
                                            ( int(self.dict_corner['xmax']), int(self.dict_corner['ymax']) ),
                                            (0, 255, 0),
                                            1
                                          )
                            cv2.imwrite(file_path + '\\' + img_name, img)           

def main():
    D = draw(DataPath, BB_Path, ImgType, FileType, Type_Up, Type_Down, Dict_Corner)
    D.working()

if __name__ == '__main__':
    main()



#        '''for f in os.listdir(self.data_path):
#            if f.endswith(self.file_type):
#                tree = ET.parse(self.data_path + '\\' + f)
#                root = tree.getroot()
#                img_name = root.find('filename').text
#                img = os.path.join(self.data_path+ '\\' + img_name)
#                print(img)
#                img = cv2.imread(img)
#                print(img)
#                for child in root.findall(self.type_up):
#                    for son in child.find(self.type_down):
#                        self.dict_corner[son.tag] = son.text
#                    print(self.dict_corner)
#                    print('--------------------')
#                    cv2.rectangle(
#                                  img, 
#                                  ( int(self.dict_corner['xmin']), int(self.dict_corner['ymin']) ), 
#                                  ( int(self.dict_corner['xmax']), int(self.dict_corner['ymax']) ),
#                                  (0, 255, 0),
#                                  1
#                                )
#                    cv2.imwrite(self.data_path+ '\\' + 'bounding Box.jpg', img)'''    