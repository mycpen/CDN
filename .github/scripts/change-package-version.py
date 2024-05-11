#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 源码参考  https://blog.csdn.net/qq_38150250/article/details/118026219

import os
import re
from datetime import datetime
import random

# 文件查找 find . -name file_name -type f
# 查找函数：search_path 查找根路径 

# 获取文章路径
def search(search_path, search_result, search_fileType_list):
    # 获取当前路径下地所有文件
    all_file = os.listdir(search_path)
    # 对于每一个文件
    for each_file in all_file:
        # 若文件为一个文件夹
        if os.path.isdir(search_path + each_file):
            # 递归查找
            search(search_path + each_file + '/', search_result, search_fileType_list)
        # 如果是需要被查找的文件
        else:
            for i in search_fileType_list:
                if re.findall(f'.*\\{i}$', each_file) == [each_file]:
                    search_result.append(search_path + each_file)


# 替换 sed -i 's/old_str/new_str/'
# 文本替换 replace_file_name 需要替换的文件路径，replace_old_str 要替换的字符，replace_new_str 替换的字符
def replace(replace_file_name, replace_old_str, replace_new_str):
    with open(replace_file_name, "r", encoding = "UTF-8") as f1: 
        content = f1.read()
        f1.close()
        t = content.replace(replace_old_str, replace_new_str)
    with open(replace_file_name, "w", encoding = "UTF-8") as f2:
        f2.write(t)
    f2.close()


# npm time version | npm_converted_time
# ------------------------------------------------------------------
# 将数字和字母对应关系定义为字典
npm_num_mapping = {
    '0': ['a', 'b', 'u'], '1': ['c', 'd', 'v'], '2': ['e', 'f', 'w'], '3': ['g', 'h', 'x'],
    '4': ['i', 'j', 'y'], '5': ['k', 'l', 'z'], '6': ['m', 'n'], '7': ['o', 'p'],
    '8': ['q', 'r'], '9': ['s', 't']
}
# 当前时间
npm_now = datetime.now()
# 格式化当前时间为指定格式 2403230741
npm_formatted_time = npm_now.strftime("%y%m%d%H%M")
# 数字替换为随机映射字母   ejugfhupjv
npm_converted_time = ''
for char in npm_formatted_time:
    if char.isdigit():
        npm_converted_time += ''.join(random.choice(npm_num_mapping[char]) if char in npm_num_mapping else char)
    else:
        npm_converted_time += char


# ------------------------------------------------------------------


# 文件名后缀
file_type_list = ['.html', '.css', '.js', '.xml', '.txt', '.md', '.py', '.yml', '.json']

# 具体文件路径
file_path_list = []

# 目录，当前根路径
path_list = [
    './',
]


# npm package version
old_pkg_version = '0.0.0-customSuffix'
new_pkg_version = '0.0.0-' + npm_converted_time


if __name__ == '__main__':
    result = []                 # 存放文件路径
    # 默认当前目录
    # path = os.getcwd()
    for path in path_list:
        search(path, result, file_type_list)    # 获取文章路径
    result = result + file_path_list
    # 过滤路径
    filtered_result = [path for path in result if not path.startswith('./.github/')]

    count = 0
    for file_name in filtered_result:
        replace(file_name, old_pkg_version, new_pkg_version)
        count += 1
        print("{} done  {}".format(file_name, count))
