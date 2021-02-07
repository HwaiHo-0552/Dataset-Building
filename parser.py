
# coding: utf-8

# In[7]:


import os
import numpy as np
import xml.etree.ElementTree as ET


classmaps={'2':0, '3':1, '4a':2, '4b':3, '4c':4, '5':5}

def confusion_matrix(preds, labels, conf_matrix):
    for p, t in zip(preds, labels):
        conf_matrix[p, t] += 1
    return conf_matrix

def getRealType(xmlfile):
    xmlfile = os.path.join("Annotations", xmlfile + ".xml")
    
    et = ET.parse(xmlfile)
    root = et.getroot()
    element_objs = root.findall('object')
    for element_obj in element_objs:
        class_name = element_obj.find('name').text.lower()
    return classmaps[class_name]

def walkpath():
    conf_matrix = np.zeros((6,6),dtype = 'int') 
    
    predDict = {}
    spath = "."
    for root, dirs, files in os.walk(spath):
        for file in files:
            if(file.endswith('.txt')):
                segs = os.path.splitext(file)
                pred = segs[0].split('_')[-1] #according the result file name to create the predict type tn
                
                with open(file) as f:
                    fileDict = {}
                    for line in f:
                        segs = line.split(" ")
                        pic = segs[0]
                        prob = float(segs[1])
                        if(pic not in fileDict):
                            fileDict[pic] = prob
                        else:
                            if(prob > fileDict[pic]):
                                fileDict[pic] = prob
                                
                    for key in fileDict:
                        if(fileDict[key] > 0.3):
                            if key not in predDict:
                                #sdict[key] = {tn:fileDict[key]}
                                predDict[key] = (pred, fileDict[key])
                            else:
                                if(predDict[key][1] < fileDict[key]):
                                    #sdict[key][tn] = fileDict[key]
                                    predDict[key] = (pred, fileDict[key])
    print(len(predDict))
    #print(predDict)
    for key in predDict:
        p = classmaps[predDict[key][0]]
        t = getRealType(key)
        conf_matrix[p, t] += 1  
    print(conf_matrix)
        
def main():
    walkpath()
    
if __name__ == "__main__":
    main()

