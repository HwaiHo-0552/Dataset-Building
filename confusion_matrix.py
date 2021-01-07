#! /usr/bin/python
#-*- coding:UTF-8 -*-

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

classes = ['2', '3', '4a', '4b', '4c', '5']
results = 'V:\\Coding\\Data_Analysis\\results.txt'
list_of_results = []
list_of_GT = []
list_of_Pre = []


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

def plot_confusion_matrix(cm, savename, title='Confusion Matrix'):

    plt.figure(figsize=(12, 8), dpi=100)
    np.set_printoptions(precision=2)

    # 在混淆矩阵中每格的概率值
    ind_array = np.arange(len(classes))
    x, y = np.meshgrid(ind_array, ind_array)
    for x_val, y_val in zip(x.flatten(), y.flatten()):
        c = cm[y_val][x_val]
        if c > 0.001:
            plt.text(x_val, y_val, "%0.2f" % (c,), color='red', fontsize=15, va='center', ha='center')
    
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title(title)
    plt.colorbar()
    xlocations = np.array(range(len(classes)))
    plt.xticks(xlocations, classes, rotation=90)
    plt.yticks(xlocations, classes)
    plt.ylabel('Ground Truth')
    plt.xlabel('Predicted Label')
    
    # offset the tick
    tick_marks = np.array(range(len(classes))) + 0.5
    plt.gca().set_xticks(tick_marks, minor=True)
    plt.gca().set_yticks(tick_marks, minor=True)
    plt.gca().xaxis.set_ticks_position('none')
    plt.gca().yaxis.set_ticks_position('none')
    plt.grid(True, which='minor', linestyle='-')
    plt.gcf().subplots_adjust(bottom=0.15)
    
    # show confusion matrix
    plt.savefig(savename, format='png')
    plt.show()

def main():
    working = get_data(results, list_of_results, list_of_GT, list_of_Pre)
    working.getting()

    # 获取混淆矩
    cm = confusion_matrix(list_of_GT, list_of_Pre)
    plot_confusion_matrix(cm, 'confusion_matrix.png', title='confusion matrix') 

if __name__=='__main__':
    main()

