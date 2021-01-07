#!/usr/bin/python
#-*- coding: UTF-8 -*-

import os

Path = 'V:\\Coding\\Faster_RCNN(Project_1)\\Result\\comp4_det_test_2.txt'
File = 'V:\\Coding\\Data_Analysis\\Category_2.txt'
list_results = []
list_names_and_pres= []
Cate = '2'
Threshold = 0.5

class build_list:
    counts = 0;
    
    def __init__(self, path, image_results, image_ids_and_pres, classes, threshold):
        self.path = path
        self.image_results = image_results
        self.image_ids_and_pres =  image_ids_and_pres
        self.classes = classes
        self.threshold = threshold
    
    def building(self):
        with open(self.path, 'r', encoding='UTF-8') as f:
            lines = f.readlines()

        for temp in lines:
            content = temp.strip().split(' ')
            self.image_results.append(content)

        for temp in self.image_results:
            s = float(temp[1])
            if s > self.threshold:
                content = self.classes + ' ' + temp[0] + ' ' + temp[1]
                self. image_ids_and_pres.append(content)
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
    working = build_list(Path, list_results, list_names_and_pres, Cate, Threshold)
    working.building()
    print(list_names_and_pres)

    Working = Write(list_names_and_pres, File)
    Working.read_and_write()

if __name__ == '__main__':
    main()
    print('\n%d images were Finished, My Lord.' %Write.counter)
