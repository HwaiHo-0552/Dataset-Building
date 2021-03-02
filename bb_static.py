#!/usr/bin/python
#-*- coding:UtF-8 -*-

#统计
import xml.etree.ElementTree as ET
import os

XML = 'V:\Coding\Thyroid_9long\paper\已标注2630张'
Type = 'xml'

class statics:
    counter = 0;
    counter_1 = 0;
    def __init__(self, xml_path, file_type):
        self.xml_path = xml_path
        self.file_type = file_type

    def working(self):
        for f in os.listdir(self.xml_path):
            if f.endswith(self.file_type):
                tree = ET.parse(self.xml_path + '\\' + f)
                root = tree.getroot()
                for son in root.findall('object'):
                    name = son.find('name').text
                    statics.counter += 1
                if statics.counter > 1:
                    print(statics.counter)
                    statics.counter_1 += 1
                statics.counter = 0
                    
def main():
    work = statics(XML, Type)
    work.working()

if __name__ == '__main__':
    main()
    print(statics.counter_1)