#!/usr/bin/python
#-*- coding:UTF-8 -*-

import os
import shutil

Path_file = 'V:\\Coding\\Thyroid_9long\\2ndTraining\\JEPGImages'
Path_txt = 'V:\\Coding\\Thyroid_9long\\2ndTraining\\ImageSets\\Main\\test.txt'

class move_test_file:
    def __init__(self, file_path, txt_path):
        self.file_path = file_path
        self.txt_path = txt_path

    def moving(self):
        test_folder_path = self.file_path + '\\' + '9long_test'
        if not os.path.exists(test_folder_path):
            os.mkdir(test_folder_path)  

        with open(self.txt_path, 'r', encoding='UTF-8') as R:
            lines = R.readlines()
        for name in lines:
            for file_content in os.listdir(self.file_path):
                file_name = os.path.splitext(file_content)
                if file_name[0] == name.strip('\n'):
                    source_path = self.file_path + '\\' + file_content
                    shutil.copy(source_path, test_folder_path + '\\' + file_content)

def main():
    work = move_test_file(Path_file, Path_txt)
    work.moving()

if __name__=='__main__':
    main()