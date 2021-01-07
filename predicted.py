#!/usr/bin/python
#-*- coding:UTF-8 -*-

import os

Path = 'V:\\Coding\\Faster_RCNN(Project_1)\\Result\\comp4_det_test_2.txt'
File = 'V:\\Coding\\Data_Analysis\\Category_2.txt'
list_results = []
list_names = []
list_pres = []
save_pres = []
Cate = '2'


class build_list:
    def __init__(self, path, image_results, image_ids, image_pres):
        self.path = path
        self.image_results = image_results
        self.image_ids = image_ids
        self.image_pres = image_pres
    
    def building(self):
        with open(self.path, 'r', encoding='UTF-8') as f:
            lines = f.readlines()

        for temp in lines:
            content = temp.strip().split(' ')
            self.image_results.append(content)

        for temp in self.image_results:
            self.image_ids.append(temp[0])
            self.image_pres.append(temp[1])

class save_score:
    counts = 0;

    def __init__(self, threshold, list_of_score, pres):
        self.thershold = threshold
        self.list_of_score = list_of_score
        self.pres= pres

        for scores in self.list_of_score:
            s = float(scores)
            if s > self.thershold:
                self.pres.append(scores)
                save_score.counts += 1    

def main():
    working = build_list(Path, list_results, list_names, list_pres)
    working.building()

    computing = save_score(0.5, list_pres, save_pres)

if __name__ == '__main__':
    main()
    print('\nThere are %d results.' % save_score.counts)
#confidence = np.array([float(x[1]) for x in splitlines])
#BB = np.array([[float(z) for z in x[2:]] for x in splitlines])