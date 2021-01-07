#!/usr/bin/python
#-*-coding: UTF-8 -*-

import os
import shutil

TYPE = 'xml'
DICT = 'C:\Coding\source_data\Img_4A'
DEST = 'C:\Coding\Test'

class Find_Image:
    counter = 0;

    def __init__(self, type, dict, dest):
        self.type = type
        self.dict = dict
        self.dest = dest
        
    def finding_and_copying(self):
        for Img_name in os.listdir(self.dict):
            if Img_name.endswith(self.type):
                source = self.dict + '/' + Img_name
                shutil.copy(source, self.dest)
                Find_Image.counter += 1

def main():
    Check = Find_Image(TYPE, DICT, DEST)
    Check.finding_and_copying()

if __name__ == '__main__':
    main()
    print('\n%d images were Finished, My Lord.' % Find_Image.counter)