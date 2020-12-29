#! /usr/bin/python
#-*- coding: UTF-8 -*-

import os
import xml.etree.ElementTree as ET

DICT = ''
ATTRIB = ''
CONT = ''

class Modify_xml:
    counter = 0;

    def __init__(self, dict, attribute, content):
        self.dict = dict
        self.attribute = attribute
        self.content = content

    def modifying(self):
        xml_files = os.listdir(self.dict)
        for file in xml_files:
            tree = ET.parse(self.dict + '\\' + file)
            root = tree.getroot()
            for son in root.iter(self.attribute):
                son.text = self.content
                print('instead..', str(son.text))
                Modify_xml.counter += 1
            tree.write(self.dict + '\\' + file)
                

def main():
    work = Modify_xml(DICT, ATTRIB, CONT)
    work.modifying()

if __name__ == "__main__":
    main()
    print('\n%d .xml files were Finished, My Lord.' % Modify_xml.counter)
