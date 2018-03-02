#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/3 14:21
# @Author  : Kaiwen Xue
# @File    : batch_rename.py
# @Software: PyCharm
"""
A personal script to rename pics and vids.
"""
import os
import shutil


def move(path):
    """
    Move pics and vids outside of folders
    """
    folder_name = ('图片', '图', '视频', '图包')
    for folders in os.listdir(path):
        for folder in os.listdir(path + folders + '/'):
            if folder in folder_name:
                for file in os.listdir(path + folders + '/' + folder + '/'):
                    shutil.move(path + folders + '/' + folder + '/' + file, path + folders + '/')
                os.rmdir(path + folders + '/' + folder + '/')


def rename(path):
    """
    Renames files.
    """
    pic = ('.jpg', '.png', '.jpeg', '.bmp', '.gif')
    vid = ('.mp4', '.mov', '.flv', '.3gp', '.avi', '.mkv', '.wmv', '.vob', '.swf', '.rmvb')
    for folders in os.listdir(path):
        dash = folders.index('—')
        # black = folders.index('】')
        blank = folders.index(' ')
        girl_name = folders[: dash]
        series_name = folders[dash+1: blank]
        for files in os.listdir(path + folders + '/'):
            dot = files.rindex('.')
            file_type = files[dot:]
            try:
                lbracket = files.index('(')
                rbracket = files.index(')')
                number = files[lbracket+1 : rbracket]
                new_number = int(number) + 1000
            except ValueError:
                print(folders)
            os.chdir(path + folders + '/')
            if file_type.lower().endswith(pic):
                os.rename(files, girl_name + '-' + series_name + ' ' +
                          '(' + str(new_number) + ')' + file_type)
            if file_type.lower().endswith(vid):
                os.rename(files, girl_name + '-' + series_name + ' ' +
                          '(' + str(new_number) + ')' + file_type)


def main():
    """
    This is the main() function
    """
    path = 'C:/Go/linshi/linshi/go/'
    move(path)
    rename(path)


if __name__ == '__main__':
    main()
