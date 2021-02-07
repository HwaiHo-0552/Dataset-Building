#!/usr/bin/python
#-*- coding:UTF-8 -*- 
#---------------------------此代码是将多类疾病等级的分类，改为二分类标签------------------------------------------

import os

Path = 'V:\Coding\9-long\data-mammogram\9Long Results\9Long(Test_1-7521张数据)'
File = 'confusion_matrix （结果统计，第一列是医生标注，第二列图像名称，第三列预测概率值，第四列预测值）.txt'
New = '2class_CM.txt'
list_1 = []

class Read:
    def __init__(self, path_source, list_t):
        self.path_source = path_source
        self.list_t = list_t

    def reading(self):
        with open(self.path_source, 'r', encoding='UTF-8') as R:
            lines = R.readlines()
        for line in lines:
            line = line.strip()
            content = line.split(' ')
            
            if (content[0]=='2') or (content[0]=='3'):
                label = 'benign'
            else:
                label = 'malignant'

            if (content[3]=='2') or (content[3]=='3'):
                pre = 'benign'
            else:
                pre = 'malignant'

            new_content = label + ' ' + content[1] + ' ' + content[2] + ' ' + pre
            self.list_t.append(new_content)

class Write:
    def __init__(self, path_file, list_t):
        self.path_file = path_file
        self.list_t = list_t

    def writting(self):
        with open(self.path_file, 'w+', encoding='UTF-8') as W:
            for content in self.list_t:
                W.writelines(content + '\n')

def main():
    source_path = os.path.join(Path, File)
    new_file = os.path.join(Path, New)

    if not os.path.exists(new_file):
        open(new_file, 'w', encoding='UTF-8')
    else:
        print('The new file has been exists.')

    work_1 = Read(source_path, list_1)
    work_1.reading()

    work_2 = Write(new_file, list_1)
    work_2.writting()

if __name__ == '__main__':
    main()