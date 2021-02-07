#!/usr/bin/python
#-*-coding:UTF-8-*-
                                #此代码功能是将文件夹下的图片拷贝至所属的类别中
                                #2021.1.14
import os
import shutil

Cate_path = 'V:\Coding\Thyroid_9long\source_dataset'
Img_path = 'V:\Coding\Thyroid_9long\source'
Type = 'jpg'
categroy = ['2', '3', '4', '5']

class classifying_file:
    counts = 0;
    def __init__(self, image_path, cate_path, file_type, list_of_class):
        self.image_path = image_path
        self.cate_path = cate_path
        self.file_type = file_type
        self.list_of_class = list_of_class

    def classifying(self):
        for root, folders, files in os.walk(self.cate_path):
            for folder in folders:
                for folder_name in self.list_of_class:
                    if folder == folder_name:
                        class_path = root + '\\' +folder
                        for xml in os.listdir(class_path):
                            xml_name = os.path.splitext(xml)
                            for image in os.listdir(self.image_path):
                                image_name = os.path.splitext(image)
                                if xml_name[0] == image_name[0]:
                                    source_path = self.image_path + '\\' + image
                                    shutil.copy(source_path, class_path + '\\' + image)
                                    classifying_file.counts += 1;

def main():
    work = classifying_file(Img_path, Cate_path, Type, categroy)
    work.classifying()

if __name__ == '__main__':
    main()
    print(classifying_file.counts)