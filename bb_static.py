#!/usr/bin/python
#-*- coding:UtF-8 -*-

#统计
import xml.etree.ElementTree as ET
import os

XML = 'V:\\Coding\\Thyroid_9long\\paper\\base_1\\test\\static'
Type = 'xml'

class statics:
    counter_1 = 0;
    counter_2 = 0;
    counter_3 = 0;
    counter_4 = 0;
    counter_5 = 0;
    
    def __init__(self, xml_path, file_type):
        self.xml_path = xml_path
        self.file_type = file_type

    def working(self):
        for f in os.listdir(self.xml_path):
            if f.endswith(self.file_type) or f.endswith('XML'):
                tree = ET.parse(self.xml_path + '\\' + f)
                root = tree.getroot()
                for son in root.findall('object'):  
                    name = son.find('name').text
                    if name == '2':
                        statics.counter_2 += 1
                    elif name == '3':
                        statics.counter_3 += 1
                    elif name == '4':
                        statics.counter_4 += 1
                    elif name == '1':
                        statics.counter_1 += 1
                    else:
                        statics.counter_5 += 1
                    
def main():
    work = statics(XML, Type)
    work.working()

if __name__ == '__main__':
    main()
    print(statics.counter_1)
    print(statics.counter_2)
    print(statics.counter_3)
    print(statics.counter_4)
    print(statics.counter_5)
    
    
    
    
    
    
    
    
    
'''
                        if name == '2':
                        statics.counter_2 += 1
                    elif name == '3':
                        statics.counter_3 += 1
                    elif name == '4A':
                        statics.counter_4a += 1
                    elif name == '4B':
                        statics.counter_4b += 1
                    elif name == '4C':
                        statics.counter_4c += 1
                    elif name == '5':
                        statics.counter_5 += 1
    print(statics.counter_3)
    print(statics.counter_4a)
    print(statics.counter_4b)
    print(statics.counter_4c)
'''