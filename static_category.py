#!/usr/bin/python
#-*- coding:UTF-8 -*-
                                               #此段代码是统计bounding box的类别个数
                                               #2021.3.1  思翠人工智能 机器学习研发工程师 

import os
import xml.etree.ElementTree as ET

DataPath = 'V:\Coding\Thyroid_9long\paper\已标注2630张'
FileType = 'xml'
Type = 'name'

class collect:
    counter_1 = 0;
    counter_2 = 0;
    counter_3 = 0;
    counter_4 = 0;
    counter_5 = 0;

    def __init__(self, data_path, file_type, type):
        self.data_path = data_path
        self.file_type = file_type
        self.type = type

    def working(self):
        for xml_file in os.listdir(self.data_path):
            if xml_file.endswith(self.file_type):
                tree = ET.parse(self.data_path + '\\' + xml_file)
                xml_root = tree.getroot()
                for xml_name in xml_root.iter(self.type):
                    if xml_name.text == '1':
                        collect.counter_1 += 1;
                    elif xml_name.text == '2':
                        collect.counter_2 += 1;
                    elif xml_name.text == '3':
                        collect.counter_3 += 1;
                    elif xml_name.text == '4':
                        collect.counter_4 += 1;
                    else:
                        collect.counter_5 += 1;

def main():
    D = collect(DataPath, FileType, Type)
    D.working()

if __name__ == '__main__':
    main()
    print(collect.counter_1, collect.counter_2, collect.counter_3, collect.counter_4, collect.counter_5)