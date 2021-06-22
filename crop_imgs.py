#!/usr/bin/python
#-*- coding:UTF-8 -*-
                                                # SAIL LAB 机器学习研发 2021.6.22
                                                # 此代码功能是根据xml的bounding box信息, 将原始图像中ROI区域按标注坐标、结合设置的阈值，取出ROI部分，再保存为新的图像
                                                # 映射成新类别, crop图像并保持
import os
import cv2
import math
import shutil
import numpy as np
import xml.etree.ElementTree as ET

root_path = 'V:\\Coding\\Thyroid_9long\\paper\\Algorithm_2\\dataset'
save_path = 'V:\\Coding\\Code\\thyroid 2clas\\dataset'
mapping = {'2':'benign', '3':'benign', '4':'malignant', '5':'malignant'}

class crop:
    def __init__(self, roots, saved, map):
        self.roots = roots
        self.saved = saved
        self.map = map

    def build_folder(self):
        os.mkdir(self.saved)
        one_cls = os.path.join(self.saved, 'benign')
        two_cls = os.path.join(self.saved, 'malignant')
        os.mkdir(one_cls)
        os.mkdir(two_cls)

        return one_cls, two_cls

    def read(self, p_1, p_2):
        for root, folders, files in os.walk(self.roots):
            for folder in folders:
                folder_pth = os.path.join(root, folder)
                for f in os.listdir(folder_pth):
                    f_name = os.path.splitext(f)[0]
                    f_img = os.path.join(folder_pth, f_name + '.jpg')
                    f_xml = os.path.join(folder_pth, f_name + '.xml')

                    self.cropping(f_name, f_img, f_xml)

    def cropping(self, img_name, img, xml):
        list_temp = []
        counter = 0

        tree = ET.parse(xml)
        tree_root = tree.getroot()
        for index, obj in enumerate( tree_root.iterfind('object') ):
            BB = obj.find('bndbox')
            clas = obj.find('name').text
            counter += 1

            for i in range(len(BB)):
                list_temp.append(BB[i].text)
            
            image = cv2.imread(img)

            '''
            try:
                io.imread(c_img)
            except Exception as e:
                print(c_img)
            '''
            xmin = np.int64(list_temp[0])
            ymin = np.int64(list_temp[1])
            xmax = np.int64(list_temp[2])
            ymax = np.int64(list_temp[3])

            wider = xmax - xmin
            length = ymax - ymin

            if wider > length:
                x = (wider - length)/2
                ymax = int(ymax + x)
                ymin = math.ceil(ymin - x)
            elif wider < length:
                x = (length - wider)/2
                xmax = int(xmax + x)
                xmin = math.ceil(xmin - x)     

            if ymin<=0:
                ymin=0
            elif xmin<=0:
                xmin=0      
                
            img_1 = image[ymin:ymax, xmin:xmax]
            cls_name = self.map[clas]
            for root, folders, files in os.walk(self.saved):
                for f in folders:
                    if cls_name == f:
                        crop_pth = os.path.join(root, cls_name)

            count = str(counter)
            img_name = img_name+'_'+count+'.jpg'
            crop_img = os.path.join(crop_pth, img_name)                           # counter主要用于一张图像中不同位置的命名
            cv2.imwrite(crop_img, img_1)              
            
            list_temp.clear()                                                     # 清空list_temp中的数据
            counter = 0                                                           # counter清0

def main():
    work = crop(root_path, save_path, mapping)
    if not os.path.exists(save_path):
        pth_1, pth_2 = work.build_folder()
    else:
        shutil.rmtree(save_path)                                                  # os.remove和os.removedirs会出现bug
        pth_1, pth_2 = work.build_folder()

    work.read(pth_1, pth_2)

if __name__ == '__main__':
    main()