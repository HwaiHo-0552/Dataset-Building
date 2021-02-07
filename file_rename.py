#!/usr/bin/python
#-*- coding:UTF-8 -*-

                       #此代码的功能是解决文件名中存在'空格'的情况, 改写名字, 将名字改为连续完整的格式.
                       #2021.1.14
import os

Path = 'V:\\Coding\\9-long\\data-mammogram\\datasets_2\\data-mamo\\test\\随机1300张'
Type = 'jpg'

class Rename:
    def __init__(self, path, file_type):
        self.path = path
        self.file_type = file_type

    #这个函数主要将后缀名为'JPG'的改为'jpg'
    def modify_file_type(self):
        for content in os.listdir(self.path):
            file_content = os.path.splitext(content)
            if (file_content[-1] != '.' + self.file_type):
                print(content)
#                old_name = self.path + '\\' + content
#                new_name = self.path + '\\' + file_content[0] + '.' + self.file_type
#                os.rename(old_name, new_name)

    def naming(self):
        for file_content in os.listdir(self.path):
            content =os.path.splitext(file_content)
            
            list_of_name = list(content[0])
            for i in list_of_name:
                if i == ' ':
                    list_of_name.remove(i)
            new_name = "".join(list_of_name)
                        
            if(new_name != content[0]):
                image_path = self.path + '\\'
                old = image_path + file_content
                new = image_path + new_name + content[1]
                os.rename(old, new)

def main():
    work = Rename(Path, Type)
    work.modify_file_type()
    work.naming()

if __name__ == '__main__':
    main()
