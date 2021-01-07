#!/usr/bin/python
#-*- coding: UTF-8 -*-

import os

File = 'V:\\Coding\\Faster_RCNN(Project_1)\\Dataset\\test\\test_5.txt'
list_content = []
Cate = '5'

class build_list:
    counts = 0;
    
    def __init__(self, file, list_content, classes):
        self.file = file
        self.list_content = list_content
        self.classes = classes
    
    def building(self):
        with open(self.file, 'r', encoding='UTF-8') as f:
            lines = f.readlines()

        for temp in lines:
            content = self.classes + ' ' + temp.strip()
            self.list_content.append(content)

            build_list.counts += 1  

class Write:
    counter = 0;

    def __init__(self, list_of_content, file_txt):
        self.list_of_content = list_of_content
        self.file_txt = file_txt

    def read_and_write(self):
        read = open(self.file_txt, 'w+')
        for contents in self.list_of_content:
            content = contents + '\n'
            read.writelines(content)
            Write.counter += 1
        read.close()

def main():
    working = build_list(File, list_content, Cate)
    working.building()

    Working = Write(list_content, File)
    Working.read_and_write()

if __name__ == '__main__':
    main()

    if(build_list.counts == Write.counter):
        print('\n%d images were Finished, My Lord.' %Write.counter)
    else:
        print('ERROR')