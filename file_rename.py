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
                file_path = os.path.join(root, folder)                  //读入计算机内部，获取路径.
                
                for file_content in os.listdir(file_path):              //将路径中的文件存储于list中表示，以便循环调取.
                    content = os.path.splitext(file_content)            //将文件名分隔为如下格式：list=[文件名, 文件属性].
                    list_of_name = list(content[0])                     // 取list=[文件名, 文件属性]的第一个，即文件名，then存储于一个新的list_new中.
                    for i in list_of_name:                              // 循环list_new
                        if i == ' ':                                    // 判断取到的字符是否为 “空格”
                            list_of_name.remove(i)                      // 如果是就remove
                    new_name = "".join(list_of_name)                    // 新建一个new_name
                        
                    if(new_name != content[0]):                         //如果new_name 不等于 原本的name
                        image_path = file_path + '\\'                   // 定义保存路径
                        old = image_path + file_content                 // 取老名字文件地址
                        new = image_path + new_name + content[1]        // 定义new_name  文件的地址
                        os.rename(old, new)                             // 改名操作

def main():
    work = Rename(Path)
    work.naming()

if __name__ == '__main__':
    main()
