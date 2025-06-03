#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import shutil

忽略文件列表 = '.DS_Store'
序号类型列表 = ('話', '话', '卷')


def 创建子文件夹(路径):
    for 文件 in os.listdir(路径):
        if 文件 not in 忽略文件列表 and os.path.isfile(路径 + 文件): # 忽略系统文件，且忽略文件夹
            分割符 = ' '
            文件名 = '.'.join(文件.split('.')[0:-1])
            漫画名称 = 文件名.split(分割符)[0]
            os.makedirs(路径 + 漫画名称, exist_ok = True)

def 移动文件(路径):
    for 文件 in os.listdir(路径):
        if 文件 not in 忽略文件列表 and os.path.isfile(路径 + 文件): # 忽略系统文件，且忽略文件夹
            分割符 = ' '
            文件名 = '.'.join(文件.split('.')[0:-1])
            漫画名称 = 文件名.split(分割符)[0]
            shutil.move(路径 + 文件, 路径 + 漫画名称 + '/')

def 重命名文件(路径):
    for 漫画文件夹 in os.listdir(路径):
        if os.path.isdir(路径 + 漫画文件夹 + '/'):
            for 文件 in os.listdir(路径 + 漫画文件夹 + '/'):
                if 文件 not in 忽略文件列表 and os.path.isfile(路径 + 漫画文件夹 + '/' + 文件):
                    分割符 = ' '
                    格式 = 文件.split('.')[-1]
                    文件名 = '.'.join(文件.split('.')[0:-1])

                    try:
                        序号部分 = 文件名.split(分割符)[1]

                        for 序号类型 in 序号类型列表:
                            if 序号类型 in 序号部分:
                                序号部分 = 序号部分.replace(序号类型,'')
                                新序号部分 = 序号部分 + 序号类型
                                新文件名称 = 新序号部分 + '.' + 格式
                                os.rename(路径 + 漫画文件夹 + '/'+ 文件, 路径 + 漫画文件夹 + '/'+ 新文件名称)
                    except:
                        print('【报错】', '【重命名文件】',漫画文件夹 + '/' + 文件)

def main():
    print('---------------------------Running---------------------------')
    路径 = '/Users/xuekaiwen/Downloads/test/'
    创建子文件夹(路径)
    print('子文件夹创建完毕!')
    移动文件(路径)
    print('移动文件完毕!')
    重命名文件(路径)
    print('重命名文件完毕!')
    print('---------------------------Job Done--------------------------')

if __name__ == '__main__':
    main()