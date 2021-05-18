#!/usr/bin/python
#-*- coding:UTF-8 -*- 
                                               #此段代码通过Bounding Box坐标值，将ROI区域裁剪下来
                                               #2021.5.13  思翠人工智能 机器学习研发工程师 
import os
import cv2
import pandas as pd
import random
import xml.etree.cElementTree as ET

img_path = 'V:\\Coding\\Thyroid_9long\\paper\\base_1\\JPEGImages'
xml_path = 'V:\\Coding\\Thyroid_9long\\paper\\base_1\\Annotations'
save_path = 'V:\\Coding\\Thyroid_9long\\paper\\Algorithm_2_1\\crop'

class crop_img:
    def __init__(self, img_pth, xml_pth, save_pth):
        self.img_pth = img_pth
        self.xml_pth = xml_pth
        self.save_pth = save_pth

    def getting_name(self):
#        self.list_name = [os.path.splitext(i)[0] for i in os.listdir(self.img_pth)]
        self.list_name = [i for i in os.listdir(self.img_pth)]
        return self.list_name
    
    def cropping(self, list_source):
        list_temp = list_source
        list_crop_info = {}    
        
        for f in os.listdir(self.xml_pth):
            f_name = os.path.splitext(f)[0]
            f_pth = os.path.join(self.xml_pth, f)
            f_root = ET.parse(f_pth)
            for son in f_root.iter('object'):
                son_name = son.find('name').text
                BB = son.find('bndbox')
                x_min = BB.find('xmin').text
                y_min = BB.find('ymin').text
                x_max = BB.find('xmax').text
                y_max = BB.find('ymax').text

                for img in list_temp:
                    img_name = os.path.splitext(img)[0]
                    if f_name == img_name:
                        image = os.path.join(self.img_pth, img)
                        cv_img = cv2.imread(image)
                        crop_img = cv_img[int(y_min):int(y_max), int(x_min):int(x_max), :]
                        
                        crop_img_name = img_name+'_'+son_name+'.jpg'
                        save_img = os.path.join(self.save_pth, crop_img_name)
                        cv2.imwrite(save_img, crop_img)

                        list_crop_info[crop_img_name] = son_name
                        list_temp.remove(img)

        return list_crop_info

    def writting_csv(self, list_info):
        list_clean = {}
        for i in list_info:
            if list_info[i] != '1':
                list_clean[i] = list_info[i]           
        keys = [i for i in list_clean]
        values = [list_info[i] for i in list_clean]
        pth = os.path.join('V:\\Coding\\Thyroid_9long\\paper\\Algorithm_2_1', 'all.csv')
        df = pd.DataFrame(columns=['image_name', 'target'])
        df['image_name'] = keys
        df['target'] = values
        df.to_csv(pth)

def main():
    work = crop_img(img_path, xml_path, save_path)
    list_name = work.getting_name()
    crop_info = work.cropping(list_name)
    work.writting_csv(crop_info)

    print('finish')

if __name__ == '__main__':
    main()