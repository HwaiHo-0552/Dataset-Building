#!/usr/bin/python
#-*- coding:UTF-8 -*-
                                                # SAIL LAB 机器学习研发 2021.6.22
                                                # 此代码功能是将数据集打乱, 生成train-75% val-25%的数据
import os
import cv2
import shutil
import random

root_path = 'V:\\Coding\\Code\\thyroid 2clas\\dataset'
save_path = 'V:\\Coding\\Code\\thyroid 2clas\\data'

class make_dataset:
    def __init__(self, roots, saved):
        self.roots = roots
        self.saved = saved

    def moving_file(self):
        list_val = []
        for root, folders, files in os.walk(self.roots):
            for f in folders:
                folder = os.path.join(root, f)
                imgs = [img for img in os.listdir(folder)]
                
                val_nums = int(len(imgs)*float(0.25))                                              # 向下取整
                temp_i = random.sample( range(0, len(imgs)-1), val_nums )
                list_val = [imgs[i] for i in temp_i]                                               # 存放25%的数据
                for i in list_val:                                                                 
                    imgs.remove(i)                                                                 # 移除验证集中的数据

                train_pth = os.path.join(self.saved, 'train', f)
                val_pth = os.path.join(self.saved, 'val', f)
                for i in list_val:
                    image = os.path.join(folder, i)
                    shutil.copy(image, val_pth)
                for i in imgs:
                    image = os.path.join(folder, i)
                    shutil.copy(image, train_pth)

def main():
    work = make_dataset(root_path, save_path)
    work.moving_file()

if __name__ == '__main__':
    main()