# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:22:07 2019

@author: LJ
"""

import os

class md_file():
    # 存放单个文件的信息
    def __init__(self,year,month,day,title,origin_title):
        self.title = title
        self.year = year
        self.month = month
        self.day = day
        self.origin_title = origin_title

class parent_dir():
    # 存放该目录下所有文件的信息
    # file_list是md_file类组成的list
    # dir_name是二级目录的名称
    def __init__(self,dir_name,file_list):
        self.dir_name = dir_name
        self.file_list = file_list
        
dir_1 = './source' # 一层目录
dir_2 = os.listdir(dir_1) # 二层目录
dir_3 = [] # 元素为parent_dir对象

for sub_dir in dir_2: # 对每一个子目录遍历查找文件
    sub_files = os.listdir(dir_1 + '/' + sub_dir)
    file_list = []
    for each_file in sub_files: # 从文件名(e.g. 2019-08-26-filename.md)中提取信息
        # 可以提取到年, 月, 日, 标题. 如果命名不规范就跳过.
        file_info = each_file.split('-')
        if len(file_info) == 4:
            [year,month,day,title] = file_info
            title = title.replace('.md','') # 删去后缀名
            file = md_file(year,month,day,title,each_file)
            file_list.append(file)
    dir_3.append(parent_dir(sub_dir,file_list))
    
index_contents = [] # index.md的文件内容
index_head = '# MyBlog  \n## [全部文章](./source/all_posts.md)  \n## 近期文章  \n'
index_contents.append(index_head)
for each_dir in dir_3:
    dir_index = [] # 每个目录的主页
    dir_index.append('# '+ each_dir.dir_name + '  \n')
    file_list = each_dir.file_list 
    # 给子目录主页添加内容                 
    for each_file in file_list:
            dir_index.append(''.join([\
                                           '  * ',each_file.year,'年',\
                                           each_file.month,'月',\
                                           each_file.day,'日: ','[',each_file.title,\
                                           '](','./',\
                                           each_file.origin_title,')','  \n'])) 
    # 给网站主页添加内容           
    index_contents.append(''.join(['## ','[',each_dir.dir_name,']','(',dir_1,'/',each_dir.dir_name,'/contents.md',')','  \n\n']))                              
    # 只显示最近5条
    if file_list != [] and len(file_list) > 5:  
        for each_file in file_list[0:4]:
            index_contents.append(''.join([\
                                           '  * ',each_file.year,'年',\
                                           each_file.month,'月',\
                                           each_file.day,'日: ','[',each_file.title,\
                                           '](',dir_1,'/',each_dir.dir_name,'/',\
                                           each_file.origin_title,')  \n']))
    # 如果不足5条就全部显示
    else:
        for each_file in file_list:
            index_contents.append(''.join([\
                                           '  * ',each_file.year,'年',\
                                           each_file.month,'月',\
                                           each_file.day,'日: ','[',each_file.title,\
                                           '](',dir_1,'/',each_dir.dir_name,'/',\
                                           each_file.origin_title,')  \n']))
    with open(''.join([dir_1,'/',each_dir.dir_name,'/contents.md']),'w') as contents:
        contents.writelines(dir_index)
with open('./index.md','w') as index:
    index.writelines(index_contents)
    
    
    
    
    
    
    
    
    
    
    
    