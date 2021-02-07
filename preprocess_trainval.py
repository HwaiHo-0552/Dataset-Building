#!/usr/bin/python
#-*- coding:UTF-8 -*-
                                               # 此代码是对数据的预处理, 仿照Pascal VOC数据集.
                                               # 1. 首先遍历整个文件夹, 将xml里标注统一; 
                                               # 2. 然后制作数据集, 将文件夹中.jpg和.xml文件分别类存放在各自文件夹中;
                                               # 3. 制作模型训练的数据集比例：70%:30%, 并制作txt文件为模型训练.
import os
import shutil
import xml.etree.ElementTree as ET
import random
import math

Root = 'V:\Coding\9-long\data-mammogram\datasets_4'
source_path = 'source_dataset'
training_path = 'Training_File'
Type_Img = 'jpg'
Type_La = 'xml'
training_ratio = float(0.7)
val_ratio = float(0.3) #这里的val集比例只是为了显示出, 数据集各个比例的划分, 实际并不参与运算就可以通过函数求出.#   
name_of_class = []

#构建一个类, 工作为遍历文件夹, 建立不同类别的文件夹, 以及其子文件夹分别存放jpg和xml文件.
class Build_ClaFolder:
    def __init__(self, path, training_path, type_image, type_label, list_name):
        self.path = path
        self.training_path = training_path
        self.type_image = type_image
        self.type_label = type_label
        self.list_name = list_name

    def building_file(self):
        for root, folders, files in os.walk(self.path):
            for folder_class in folders:
                class_folder = os.path.join(self.training_path, folder_class)
                if os.path.exists(class_folder):
                    print('Work 1: class_folders: %s is exist.' % folder_class)
                else:
                    os.mkdir(class_folder)
                    self.list_name.append(folder_class)
                    print('Work 1: class_folders: %s is built done.' % folder_class)
                    
                    image_folder = os.path.join(class_folder, folder_class + '_' + self.type_image)
                    os.mkdir(image_folder)

                    label_folder = os.path.join(class_folder, folder_class + '_' + self.type_label)
                    os.mkdir(label_folder)
                    
#构建一个类, 工作为遍历文件夹, 将各类的.jpg和.xml文件分别放置在各种属性的文件夹中.   
class Build_ClaFile:
    counter_image = 0;
    counter_label = 0;

    def __init__(self, class_path, training_path, type_image, type_label):
        self.class_path = class_path
        self.training_path = training_path
        self.type_image = type_image
        self.type_label = type_label

    def Copying_and_Refining(self):
        for root, folders, files in os.walk(self.class_path):
            for folder in folders:
                folder_path = os.path.join(root, folder)
                for file_type in os.listdir(folder_path):
                    source_path = os.path.join(folder_path, file_type)
                    move_folder = os.path.join(self.training_path, folder)

                    if file_type.endswith(self.type_image):
                        dict_path = os.path.join(move_folder, folder + '_' + self.type_image)
                        shutil.copy(source_path, dict_path)
                        Build_ClaFile.counter_image += 1
                    elif file_type.endswith(self.type_label):
                        dict_path = os.path.join(move_folder, folder + '_' + self.type_label)
                        shutil.copy(source_path, dict_path)
                        Build_ClaFile.counter_label += 1
        
        #通过计数判断, 复制文件过程中是否出错.
        if Build_ClaFile.counter_image != Build_ClaFile.counter_label:
            print('Work 2: ERROR!')
            print('Work 2: move_image: %d, move_label: %d' %(Build_ClaFile.counter_image, Build_ClaFile.counter_label))
        else:
            print('Work 2: Moving Image and Label finished.')

#建立训练集的文件以备查询, 和txt文件作为训练时使用.
class Build_for_training:
    def __init__(self, dataset_path, list_class, ratio_train, folder_type):
        self.dataset_path = dataset_path
        self.list_class = list_class
        self.ratio_train = ratio_train
        self.folder_type = folder_type

    def Creating(self):
        for root, folders, files in os.walk(self.dataset_path):
            for folder in folders:
                for name in self.list_class:
                    if folder == name + '_' + self.folder_type:
                        folder_path = os.path.join(root, folder)
                        file_list = os.listdir(folder_path)
                        nums = len(file_list)
                        print('----------------%s has %d images----------------' %(folder, nums))                        
                        
#                        position_dataset =range(nums - 1)
                        position_dataset = range(nums)
                        all_index = set(position_dataset)

                        #制作用于train的数据
                        nums_train = nums * self.ratio_train
                        train_list = random.sample( position_dataset, round(nums_train) )
                        print('number of train_index: %.2f files ~= %d files' % ( nums_train, round(nums_train) ) )
                        train_index = set(train_list)
                        train_txt = self.dataset_path + '\\' + name + '\\' + 'train.txt'
                        with open(train_txt, 'w+', encoding='UTF-8') as W:
                            for i in train_index:
                                file_name = os.path.splitext(file_list[i])[0] + '\n'
                                W.writelines(file_name)
                        W.close()

                        #制作用于val的数据
                        val_index = all_index - train_index
                        print('number of val_index: %.2f files ~= %d files' % ( len(val_index), len(val_index) ) )
                        val_txt = self.dataset_path + '\\' + name + '\\' + 'val.txt'
                        with open(val_txt, 'w+', encoding='UTF-8') as W:
                            for i in val_index:
                                file_name = os.path.splitext(file_list[i])[0] + '\n'
                                W.writelines(file_name)
                        W.close()

def main():

    #原始数据集存放地址.
    Path = os.path.join(Root, source_path)
    #网络模型训练集预存放地址.
    training_folder = os.path.join(Root, training_path)

    if os.path.exists(training_folder):
        print('Folder has been built')
    else:
        os.mkdir(training_folder)
        print('---File is Building Done For Training---')
    
    #建立一个新的文件夹, 其中依据''类别名称''自动分配建立各自类别的文件夹.
    work_1 = Build_ClaFolder(Path, training_folder, Type_Img, Type_La, name_of_class)
    work_1.building_file()
    
    print('训练集类别: ')
    for name in name_of_class:
        print(name)
    
    #将jpg和xml分别拷贝入各自属性的文件夹下, 特别针对xml文件的名字和标注信息对应不上的文件进行的代码更改, 使其一致.
    work_2 = Build_ClaFile(Path, training_folder, Type_Img, Type_La)
    work_2.Copying_and_Refining()

    #建立一个文件夹放置可训练的数据集.
    work_3 = Build_for_training(training_folder, name_of_class, training_ratio, Type_Img)
    work_3.Creating()

if __name__ == "__main__":
    main()
    print('All task has been Finished, My Lord.')