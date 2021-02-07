#!/usr/bin/python
#-*- coding:UTF-8 -*-

                                            #此代码是用于制作confusion matrix的数据，最终得到的是一个写入txt文件的dict字典，
                                            #Key是name,为图像的名字;包含的三个value写在一个list中,list[0]是predicated概率值;list[1]是predicted值;list[2]Ground Truth标签.
                                            #------------------------------------------coding by 2021.1.20--------------------------------------------------------------

Path = 'V:\\Coding\\9-long\\data-mammogram\\datasets\\new\\results_txt\\predicted_statics.txt'
GT_Path = 'V:\\Coding\\9-long\\data-mammogram\\datasets\\source_dataset'
CM_file = 'V:\\Coding\\9-long\\data-mammogram\\datasets\\new\\results_txt\\CM.txt'
Dict_1 = {}
Type = 'jpg'

import os

class get_results:
    def __init__(self, path_result, dict_1):
        self.path_result = path_result
        self.dict_1 = dict_1

    def getting(self):
        with open(self.path_result, 'r', encoding='UTF-8') as R:
            lines = R.readlines() 
        for line in lines:
            line = line.strip()
            name = line.split(' ')[0]
            value = line.split(' ')[1]
            label = line.split(' ')[2]
            self.dict_1[name] = [value, label]

class CM_dict:
    def __init__(self, path_gt, type_file, dict_result):
        self.path_gt = path_gt
        self.type_file = type_file
        self.dict_result = dict_result

    def creatting(self):
        for root, folders, files in os.walk(self.path_gt):
            for folder in folders:
                file_path = os.path.join(root, folder)
                for image in os.listdir(file_path):
                    if image.endswith(self.type_file):
                        image_name = os.path.splitext(image)[0]
                        for name in self.dict_result:
                            if image_name == name:
                                self.dict_result[name].append(folder)
class CM_txt:
    def __init__(self,cm_file, cm_dict):
        self.cm_file = cm_file
        self.cm_dict = cm_dict

    def writting(self):
        with open(self.cm_file, 'w+', encoding='UTF-8') as W:
            for name in self.cm_dict:
                content = self.cm_dict[name][2] + ' ' + name + self.cm_dict[name][0] + ' ' + self.cm_dict[name][1] + '\n'
                W.writelines(content)

def main():
    work_1 = get_results(Path, Dict_1)
    work_1.getting()

    work_2 = CM_dict(GT_Path, Type, Dict_1)
    work_2.creatting()

    if not os.path.exists(CM_file):
        txt_file = open(CM_file, 'w+', encoding='UTF-8')
    else:
        with open(CM_file, 'a+', encoding='UTF-8') as C:
            C.truncate(0)
    
    work_3 = CM_txt(CM_file, Dict_1)
    work_3.writting()

if __name__ == '__main__':
    main()

