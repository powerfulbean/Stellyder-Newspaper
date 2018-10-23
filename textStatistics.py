# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 11:37:55 2018

@author: Jin Dou
"""
import os
import collections as Coll
import re
root_filedir_list =['D:\\Appendix\\spyder_target']

suffix = "txt"

filelist = []
#load file name
for file_dir in root_filedir_list:
    filelist_per=[]
    for root, dirs, files in os.walk(file_dir): 
        for i in files:
            print(i)
            Suffix_up = suffix.upper()
            Suffix_low = suffix.lower()
            if i.endswith(Suffix_low) or i.endswith(Suffix_up):
                temp = os.path.join(root,i)
                filelist_per.append(temp) #当前路径下所有非目录子文件
    filelist.append(filelist_per)
                
# load file
    
freq_sum = Coll.Counter('')

for file_name in filelist[0]:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        freq_temp = Coll.Counter(re.split(r"[()\,.;:'?!\s\“”’‘\d\"\']+",content))
        freq_sum += freq_temp
        
answer=freq_sum.most_common(100)

