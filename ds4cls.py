#!/usr/bin/python
#-*- coding:UTF-8 -*- 
                                               #此段代码将爬取到的数据整理成train-val-test数据
                                               #2021.5.13  思翠人工智能 机器学习研发工程师 

import os
import math
import pandas as pd

csv_path = 'V:\\Coding\\Thyroid_9long\\paper\\Algorithm_2_1\\all.csv'
Pie4T = float(0.75)
Pie4V = float(0.25)

class making:
    def __init__(self, csv_pth, pie4t, pie4v):
        self.csv_pth = csv_pth
        self.pie4t = pie4t
        self.pie4v = pie4v

    def reading(self):
        dict_all = {}
        df = pd.read_csv(self.csv_pth)
        list_name = [i for i in df['image_name']]
        list_gt = [i for i in df['target']]
        for i, v in enumerate(list_name):
            dict_all[v] = list_gt[i]
        
        return dict_all

    def getting(self, dict_temp):
        dict_2 = {}
        dict_3 = {}
        dict_4 = {}
        dict_5 = {}
        for i in dict_temp:
            if dict_temp[i] == 2:
                dict_2[i] = dict_temp[i]
            elif dict_temp[i] == 3:
                dict_3[i] = dict_temp[i]
            elif dict_temp[i] == 4:
                dict_4[i] = dict_temp[i]
            elif dict_temp[i] == 5:
                dict_5[i] = dict_temp[i]
        
        return dict_2, dict_3, dict_4, dict_5

    def building(self, d_2, d_3, d_4, d_5):
        dict4T = {}
        dict4V = {}

        pie_2 = math.ceil(len(d_2)*self.pie4t)
        for index, v in enumerate(d_2):
            if index <= pie_2:
                dict4T[v] = d_2[v]
            else:
                dict4V[v] = d_2[v]

        pie_3 = math.ceil(len(d_3)*self.pie4t)
        for index, v in enumerate(d_3):
            if index <= pie_3:
                dict4T[v] = d_3[v]
            else:
                dict4V[v] = d_3[v]

        pie_4 = math.ceil(len(d_4)*self.pie4t)
        for index, v in enumerate(d_4):
            if index <= pie_4:
                dict4T[v] = d_4[v]
            else:
                dict4V[v] = d_4[v]
        
        pie_5 = math.ceil(len(d_5)*self.pie4t)
        for index, v in enumerate(d_5):
            if index <= pie_5:
                dict4T[v] = d_5[v]
            else:
                dict4V[v] = d_5[v]

        return dict4T, dict4V

    def outputing(self, d_t, d_v):
        keys_train = [i for i in d_t]
        values_train = [d_t[i] for i in d_t]
        df_1 = pd.DataFrame(columns=['image_name', 'target'])
        train_pth = os.path.join('V:\\Coding\\Thyroid_9long\\paper\\Algorithm_2_1', 'train.csv')
        df_1['image_name'] = keys_train
        df_1['target'] = values_train
        df_1.to_csv(train_pth)

        keys_val = [i for i in d_v]
        values_val = [d_v[i] for i in d_v]
        df_2 = pd.DataFrame(columns=['image_name', 'target'])
        val_pth = os.path.join('V:\\Coding\\Thyroid_9long\\paper\\Algorithm_2_1', 'val.csv')
        df_2['image_name'] = keys_val
        df_2['target'] = values_val
        df_2.to_csv(val_pth)

def main():
    work = making(csv_path, Pie4T, Pie4V)
    dict_all = work.reading()
    dict_2, dict_3, dict_4, dict_5 = work.getting(dict_all)
    dict4T, dict4V = work.building(dict_2, dict_3, dict_4, dict_5)
    work.outputing(dict4T, dict4V)

if __name__ == '__main__':
    main()