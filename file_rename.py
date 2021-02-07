#!/usr/bin/python
#-*- coding:UTF-8 -*-

                       #此代码的功能是解决文件名中存在'空格'的情况, 改写名字, 将名字改为连续完整的格式.
                       #2021.1.14

Path = 'V:\Coding\9-long\data-mammogram\datasets_4\image'

import os

class Rename:
    def __init__(self, path):
        self.path = path

    def naming(self):
        for root, folders, files in os.walk(self.path):
            for folder in folders:
                file_path = os.path.join(root, folder)
                
                for file_content in os.listdir(file_path):
                    content = os.path.splitext(file_content)
                    list_of_name = list(content[0])
                    for i in list_of_name:
                        if i == ' ':
                            list_of_name.remove(i)
                    new_name = "".join(list_of_name)
                        
                    if(new_name != content[0]):
                        image_path = file_path + '\\'
                        old = image_path + file_content
                        new = image_path + new_name + content[1]
                        os.rename(old, new)

def main():
    work = Rename(Path)
    work.naming()

if __name__ == '__main__':
    main()
