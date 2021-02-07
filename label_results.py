#!/usr/bin/python
#-*- coding:UTF-8 -*-
#-----------------------此代码是在得到test的统计数据后，爬取出其中数据并加上标签，为了后续的confusion matrix计算用---------------------------------------

Path = 'V:\\Coding\\Thyroid_9long\\2ndTraining\\results\\Main'
GroundTruth_Path = 'V:\\Coding\\Thyroid_9long\\2ndTraining\\source_dataset'
Threshold = float(0.5)
Output_list = []
CM_list = []
Predicted_file = 'predicted_statics.txt'
Confusion_Matrix = 'confusion_matrix.txt'
File_type = 'jpg'

import os

class label_results:
    def __init__(self, root_path, threshold, output_list):
        self.root_path = root_path
        self.threshold = threshold
        self.output_list = output_list

    def labeling(self):
        for root, folders, files in os.walk(self.root_path):
            for file_content in files:
                file_name = os.path.splitext(file_content)
                file_class = file_name[0].split('_')[-1]
                
                file_path = os.path.join(self.root_path, file_content)
                with open(file_path, 'r', encoding='UTF-8') as R:
                    lines = R.readlines()

                for content in lines:
                    predicted_value = content.split(' ')[1]
                    if float(predicted_value) >= self.threshold:
                        image = content.split(' ')[0]
                        output_content = image + ' ' + predicted_value + ' ' + file_class
                        self.output_list.append(output_content)  
                    
class get_results:
    def __init__(self, path, list_results):
        self.path = path
        self.list_results = list_results

    def getting(self):
        with open(self.path, 'w+', encoding='UTF-8') as W:
            for content in self.list_results:
                W.writelines(content + '\n')

class get_ConfusionMatrix:
    def __init__(self, ground_truth_path, predicted_path, file_type, list_predicted, list_CM):
        self.ground_truth_path = ground_truth_path
        self.predicted_path = predicted_path
        self.file_type = file_type
        self.list_predicted = list_predicted
        self.list_CM = list_CM

    def getting_CM(self):
        for root, folders, files in os.walk(self.ground_truth_path):
            for folder in folders:
                file_path = os.path.join(root, folder)
                for image_file in os.listdir(file_path):
                    if image_file.endswith(self.file_type):
                        GT_name = os.path.splitext(image_file)[0]
                        for content in self.list_predicted:
                            predicted_name = content.split(' ')[0]
                            if GT_name == predicted_name:
                                value = folder + ' ' + content 
                                self.list_CM.append(value)

def main():
    work_1 = label_results(Path, Threshold, Output_list)
    work_1.labeling()

    Predicted_path = Path + '\\' + Predicted_file
    work_2 = get_results(Predicted_path, Output_list)
    work_2.getting()

    work_3 = get_ConfusionMatrix(GroundTruth_Path, Predicted_path, File_type, Output_list, CM_list)
    work_3.getting_CM()
    
    confusion_matrix = Path + '\\' + Confusion_Matrix
    work_4 = get_results(confusion_matrix, CM_list)
    work_4.getting()

if __name__ == '__main__':
    main()