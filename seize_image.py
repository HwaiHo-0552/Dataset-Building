#!/usr/bin/python
#-*- coding:UTF-8 -*-

                                            #思翠人工智能, 机器学习研发
                                            #此代码是将BoundingBox中区域的特征抠取出来  
import os
import cv2
from skimage import io
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET

save_dir = 'V:\\Coding\\Thyroid_9long\\paper\\Algorithm_2_1'
source_data = 'source_data'

class crop:   
    file_name = []
    counts = 0

    def __init__(self, save_pth, source_pth):
        self.save_pth = save_pth
        self.source_pth = source_pth
        self.dataset_pth = os.path.join(self.save_pth, 'dataset')

    def get_name(self):
        if not os.path.exists(self.dataset_pth):
            os.makedirs(self.dataset_pth)
            print('make dir .\\dataset')

        name_txt = os.path.join(self.dataset_pth, 'file_name.txt')
        if not os.path.exists(name_txt):
            csv_pth = os.path.join(self.save_pth, '特征表格\\dataset.xlsx')
            df = pd.read_excel(csv_pth)
        
            for i in range(df['image_name'].size):
                crop.file_name.append(df['image_name'][i])
                with open(name_txt, 'w+', encoding='UTF-8') as w_f:
                    for name in crop.file_name:
                        w_f.writelines(name + '\n')
            print('make file .\\file_name.txt')
        else:
            with open(name_txt, 'r+', encoding='UTF-8') as r_f:
                line = r_f.readlines()
            for n in line:
                n = n.rstrip('\n')
                crop.file_name.append(n)
        
    def get_file(self):
        source = os.path.join(self.dataset_pth, self.source_pth)
        crop_dataset = os.path.join(self.dataset_pth, 'crop_img')
        if not os.path.exists(crop_dataset):
            os.makedirs(crop_dataset)
        
        for name in crop.file_name:
            img = os.path.join(source, name + '.jpg')
            xml = os.path.join(source, name + '.xml')
            crop.seize(img, xml, crop_dataset)
    
    def seize(c_img, c_xml, crop_pth):
        list_temp = []
        img = os.path.split(c_img)[1]
        img_name = img.split('.')[0]

        tree = ET.parse(c_xml)
        tree_root = tree.getroot()
        for index, obj in enumerate( tree_root.findall('object') ):
            BB = obj.find('bndbox')
            f_name = obj.find('name')

            for i in range(len(BB)):
                list_temp.append(BB[i].text)
            
            img = cv2.imread(c_img)

            '''
            try:
                io.imread(c_img)
            except Exception as e:
                print(c_img)
            '''
            print(list_temp)
#            xmin = np.int64(list_temp[0])
#            ymin = np.int64(list_temp[1])
#            xmax = np.int64(list_temp[2])
#            ymax = np.int64(list_temp[3])
            
#            img_1 = img[ymin:ymax, xmin:xmax]
            
            '''
            if index == 0:
                crop_img = os.path.join(crop_pth, img_name+'.jpg')
            else:
                crop_img = os.path.join(crop_pth, img_name + '_'+str(index)+'_'+f_name.text + '.jpg') 
            '''       
#            crop_img = os.path.join(crop_pth, img_name+'.jpg')
#            crop.counts += 1
#            cv2.imwrite(crop_img, img_1)
            
#            list_temp.clear()                                                                           #清空list_temp中的数据
    
def main():
    job = crop(save_dir, source_data)
    job.get_name()
    job.get_file()
    

if __name__ == '__main__':
    main()
    print(crop.counts)