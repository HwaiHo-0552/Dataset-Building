#!/usr/bin/python
#-*- coding: UTF-8 -*-

import os

DICT = ''
File_txt = ''
Cate = ''

class Write:

    counter = 0;

    def __init__(self, dict, file_txt, category):
        self.dict = dict
        self.file_txt = file_txt
        self.category = category
        

    def read_and_write(self):
        read = open(self.file_txt, 'w+')
        for Img_name in os.listdir(self.dict):
#            content = os.path.splitext(Img_name)[0] + '-' + self.category + '\n'
            content = os.path.splitext(Img_name)[0] + '\n'
            read.writelines(content)

            Write.counter += 1
            print(Img_name)
        read.close()

def main():
    Working = Write(DICT, File_txt, Cate)
    Working.read_and_write()

if __name__ == '__main__':
    main()
    print('\n%d images were Finished, My Lord.' %Write.counter)