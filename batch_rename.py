#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/3 14:21
# @Author  : Kaiwen Xue
# @文件    : batch_rename.py
# @Software: PyCharm
"""

"""
import os
import shutil


def move(路径):
    """
    Move 照片s and 视频s outside of 外层文件夹
    """
    文件夹名称 = ('pic', 'pics', 'vid', 'vids')
    for 外层文件夹 in os.listdir(路径):
        for 内层文件夹 in os.listdir(路径 + 外层文件夹 + '/'):
            if 内层文件夹 in 文件夹名称:
                for 文件 in os.listdir(路径 + 外层文件夹 + '/' + 内层文件夹 + '/'):
                    shutil.move(路径 + 外层文件夹 + '/' + 内层文件夹 + '/' + 文件, 路径 + 外层文件夹 + '/')
                os.rmdir(路径 + 外层文件夹 + '/' + 内层文件夹 + '/')


def rename(路径):
    """
    Renames 文件s.
    """
    照片 = ('.jpg', '.png', '.jpeg', '.bmp', '.gif')
    视频 = ('.mp4', '.mov', '.flv', '.3gp', '.avi', '.mkv', '.wmv', '.vob', '.swf', '.rmvb')
    for 外层文件夹 in os.listdir(路径):
        连接符 = 外层文件夹.index('—')
        # 右黑括号 = 外层文件夹.index('】')
        空格 = 外层文件夹.index(' ')
        人物名称 = 外层文件夹[: 连接符]
        系列名称 = 外层文件夹[连接符+1: 空格]
        for 文件 in os.listdir(路径 + 外层文件夹 + '/'):
            点 = 文件.rindex('.')
            文件类型 = 文件[点:]
            try:
                左括号 = 文件.index('(')
                右括号 = 文件.index(')')
                编号 = 文件[左括号+1 : 右括号]
                新编号 = int(编号) + 1000
            except ValueError:
                print(外层文件夹)
            os.chdir(路径 + 外层文件夹 + '/')
            if 文件类型.lower().endswith(照片):
                os.rename(文件, 人物名称 + '-' + 系列名称 + ' ' +
                          '(' + str(新编号) + ')' + 文件类型)
            if 文件类型.lower().endswith(视频):
                os.rename(文件, 人物名称 + '-' + 系列名称 + ' ' +
                          '(' + str(新编号) + ')' + 文件类型)


def main():
    """
    This is the main() function
    """
    路径 = 'C:/Go/linshi/linshi/go/'
    move(路径)
    rename(路径)


if __name__ == '__main__':
    main()
