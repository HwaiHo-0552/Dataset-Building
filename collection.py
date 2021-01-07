#!/usr/bin/python
#-*- coding:UTF-8 -*-

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

def main():
    working = build_list(Path, list_results, list_names_and_pres, Cate, 0.5)
    working.building()
    print(list_names_and_pres)

 #   computing = save_score(0.5, list_pres, save_pres)
    
if __name__ == '__main__':
    main()
    print('\nThere are %d results.' % build_list.counts)


    