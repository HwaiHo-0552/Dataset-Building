#! /usr/bin/python
#-*- coding:UTF-8 -*- 
                                                            #此代码为制作混肴矩阵的数据图
                                                            #     2021-1-18于苏州

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

classes = ['1', '2', '3', '4', '5']
#classes = ['benignt', 'malignan']
results = 'V:\\Coding\\Thyroid_9long\\2ndTraining\\results\\Main\\confusion_matrix.txt'
list_of_results = []
list_of_GT = []
list_of_Pre = []
sum_cm = []

class get_data:
    def __init__(self, path_GTandPre, Results_list, GT_list, Pre_list):
        self.path_GTandPre = path_GTandPre
        self.Results_list = Results_list
        self.GT_list = GT_list
        self.Pre_list = Pre_list

    def getting(self):
        with open(self.path_GTandPre, 'r', encoding='UTF-8') as R:
            lines = R.readlines()
        for temp in lines:
            content = temp.strip().split(' ')
            self.Results_list.append(content)
            
        for temp in self.Results_list:
            gt = temp[0]
            self.GT_list.append(gt)
            pre = temp[3]
            self.Pre_list.append(pre)

class get_figure:
    def __init__(self, computed_data, save_name, save_format, category, sum_list):
        self.computed_data = computed_data
        self.save_name = save_name
        self.save_format = save_format
        self.category = category
        self.sum_list = sum_list

    def drawing(self):
        fig, ax = plt.subplots(figsize=(8, 8), dpi=480)
        plt.xlabel('Ground Truth')
        plt.ylabel('Predictd')
        plt.title('Confusion Matrix for 9Long\'s Dataset')
        im_plt = plt.imshow(self.computed_data, cmap="YlGn")
        
        ax.set_xticks(np.arange(len(self.category)))
        ax.set_yticks(np.arange(len(self.category)))
        ax.set_xticklabels(self.category)
        ax.set_yticklabels(self.category)
        color_bar = ax.figure.colorbar(im_plt, ax=ax)
        
        for i in range(self.computed_data.shape[0]):
            for j in range(self.computed_data.shape[1]):
#                im_plt.axes.text(j, i, "%d" % self.computed_data[i][j], color='red', fontsize=16, va='center', ha='center')
                value = self.computed_data[i][j] / self.sum_list[j]
                im_plt.axes.text(j, i, "%0.3f" % value, color='red', fontsize=16, va='center', ha='center')
        
        plt.savefig(self.save_name, format=self.save_format)
        plt.show()

def main():
    working = get_data(results, list_of_results, list_of_GT, list_of_Pre)
    working.getting()

    C_M = confusion_matrix(list_of_GT, list_of_Pre)
    print(C_M)
    sum_cm = C_M.sum(axis=0)
    print(sum_cm)

    figure = get_figure(C_M, '9Long_thyroid(CM %).jpg', 'jpg', classes, sum_cm)
    figure.drawing()
    
if __name__=='__main__':
    main()