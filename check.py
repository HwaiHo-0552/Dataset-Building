#!/usr/bin/python
#-*- coding:UTF-8 -*-

file_path = 'V:\\Coding\\Data_Analysis\\results.txt'

with open(file_path, 'r', encoding='UTF-8') as R:
    lines = R.readlines()

for temp in lines:
    content = temp.strip().split(' ')
    if content[0] == '4a'!= content[3]:
        print(content)
