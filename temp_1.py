#!/usr/bin/python
#-*- coding: UTF-8 -*-

import os

Path_1 = 'V:\\Coding\\Faster_RCNN(Project_1)\\Dataset\\test\\ground_truth.txt'
Path_2 = 'V:\\Coding\\Data_Analysis\\predicted.txt'
File = 'V:\\Coding\\Data_Analysis\\results.txt'
list_labels = []
list_pres = []
list_results = []

class build_list:
    counts = 0;
    
    def __init__(self, path_1, path_2, label_list, pre_list, result_list):
        self.path_1 = path_1
        self.path_2 = path_2
        self.label_list = label_list
        self.pre_list = pre_list
        self.result_list = result_list
    
    def building(self):
        with open(self.path_1, 'r', encoding='UTF-8') as f:
            lines_1 = f.readlines()
        for temp in lines_1:
            content = temp.strip().split(' ')
            self.label_list.append(content)

        with open(self.path_2, 'r', encoding='UTF-8') as f:
            lines_2 = f.readlines()
        for temp in lines_2:
            content = temp.strip().split(' ')
            self.pre_list.append(content)

        for temp in self.pre_list:
            name_temp = temp[0]
            for tip in self.label_list:
                name_tip = tip[1]
                if name_tip == name_temp:
                    content =  tip[0] + ' ' + temp[0] + ' ' + temp[1] + ' ' + temp[2]
                    self.result_list.append(content)
            
            build_list.counts += 1  

class Write:
    counter = 0;

    def __init__(self, list_of_content, file_txt):
        self.list_of_content = list_of_content
        self.file_txt = file_txt

    def read_and_write(self):
        read = open(self.file_txt, 'w+', encoding='UTF-8')
        for contents in self.list_of_content:
            content = contents + '\n'
            read.writelines(content)
            Write.counter += 1
        read.close()

def main():
    working = build_list(Path_1, Path_2, list_labels, list_pres, list_results)
    working.building()

    Working = Write(list_results, File)
    Working.read_and_write()

if __name__ == '__main__':
    main()
    print('\n%d images were Finished, My Lord.' %Write.counter)
