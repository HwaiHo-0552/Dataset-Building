#!/usr/bin/python
#-*- coding:UTF-8 -*-

import os

Path = 'V:\Coding\9-long\data-mammogram\datasets_4\Training_File'
Type = 'txt'
trainval = []
train = []
val = []

class creat_txt:
    def __init__(self, path, file_type, list_trainval, list_train, list_val):
        self.path = path
        self.file_type = file_type
        self.list_trainval = list_trainval
        self.list_train = list_train
        self.list_val = list_val
    
    def reading(self):
        for root, folders, files in os.walk(self.path):
            for fi in files:
                if fi.endswith(self.file_type):
                    file_path = os.path.join(root, fi)

                    if fi == 'train.txt':
                        with open(file_path, 'r', encoding='UTF-8') as R:
                            lines = R.readlines()
                        for name in lines:
                            self.list_trainval.append(name)
                            self.list_train.append(name)
                    elif fi == 'val.txt':
                        with open(file_path, 'r', encoding='UTF-8') as R:
                            lines = R.readlines()
                        for name in lines:
                            self.list_trainval.append(name)
                            self.list_val.append(name)

    def creating(self):
        trainval_txt = self.path + '\\' + 'trainval.txt'
        with open(trainval_txt, 'w+', encoding='UTF-8') as W:
            for name in self.list_trainval:
                W.writelines(name)
        
        train_txt = self.path + '\\' + 'train.txt'
        with open(train_txt, 'w+', encoding='UTF-8') as W:
            for name in self.list_train:
                W.writelines(name)        
        
        val_txt = self.path + '\\' + 'val.txt'
        with open(val_txt, 'w+', encoding='UTF-8') as W:
            for name in self.list_val:
                W.writelines(name)        

def main():
    work = creat_txt(Path, Type, trainval, train, val)
    work.reading()
    work.creating()

if __name__=='__main__':
    main()