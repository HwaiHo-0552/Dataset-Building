#!/usr/bin/python
#-*- coding:UTF-8 -*- 
                                               #此段代码通过faster-rcnn预测的结果，按阈值筛选
                                               #2021.5.14  思翠人工智能 机器学习研发工程师 

import os

folder_path = 'V:\\Coding\\Project_2\\results\\preds'
image_name = 'V:\\Coding\\Project_2\\results\\test.txt'

class screen:
    def __init__(self, root_pth, img_names):
        self.root_pth = root_pth
        self.img_names = img_names

    def reading(self):
        list_b = []
        list_m = []
        for root, folders, files in os.walk(self.root_pth):
            for f in files:
                f_name = os.path.splitext(f)[0]
                gt = f_name.split('_')[-1]

                f_pth = os.path.join(root, f)
                with open(f_pth, 'r', encoding='utf-8') as F:
                    lines = F.readlines()
                for i in lines:
                    content = i.strip().split(' ')
                    image_name = content[0]
                    pred_value = content[1]
                    if float(pred_value)>=float(0.5):
                        info = image_name + " " + pred_value + " " + gt
                        if gt == 'benign':
                            list_b.append(info)
                        else:
                            list_m.append(info)     

        return list_b, list_m

    def offset(self, list_t):
        dict_temp = {}
        pred_label = []
        with open(self.img_names, 'r', encoding='UTF-8') as F:
            lines = F.readlines()
        for i in lines:
            i = i.strip()
            dict_temp[i] = 0

        for i in list_t:
            content = i.strip().split(' ')
            image_name = content[0]
            pred_value = content[1]
            pred_label = content[2]

            if float(dict_temp[image_name])<float(pred_value):
                dict_temp[image_name] = pred_value

        for i in dict_temp:
            dict_temp[i] = str(dict_temp[i]) + ' ' + pred_label

        return dict_temp

    def building(self, dict_1, dict_2):
        d_1 = dict_1
        d_2 = dict_2
        dict_preds = {}

        for name_1 in d_1:
            preds_1 = d_1[name_1].split(' ')[0]
            label_1 = d_1[name_1].split(' ')[1]
            for name_2 in d_2:
                preds_2 = d_2[name_2].split(' ')[0]
                label_2 = d_2[name_2].split(' ')[1]
                if name_1 == name_2:
                    if float(preds_1)>=float(preds_2):
                        dict_preds[name_1] = d_1[name_1]
                    elif float(preds_1)<float(preds_2):
                        dict_preds[name_2] = d_2[name_2]
        file_pth = 'V:\\Coding\\Project_2\\results\\result.txt'
        if os.path.exists(file_pth):
            os.remove(file_pth)
        File = open(file_pth, 'w', encoding='UTF-8')
        for i in dict_preds:
            content = i + ' ' + dict_preds[i] + '\n'
            File.writelines(content)
        File.close()
                   
def main():
    work = screen(folder_path, image_name)
    list_b, list_m = work.reading()
    dict_b = work.offset(list_b)
    dict_m = work.offset(list_m)
    work.building(dict_b, dict_m)

if __name__ == '__main__':
    main()

'''
            for index_2, c_2 in enumerate(d_2):
                n_2 = c_2.split(' ')[0]
                p_2 = c_2.split(' ')[1]
                if n_1 == n_2:
                    if p_1>p_2:
                        l_2.pop(index_2)
                    elif p_1<p_2:
                        l_1.pop(index_1)     
'''