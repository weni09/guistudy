#!/usr/bin/python3
# -*- coding: utf-8 -*-
#===================================================
# @Time : 2020/6/29 15:50                           
# @Author : weni09                                  
# @File : test2.py
#===================================================

from PyQt5.Qt import *
def getSubClasses(cls):
    for subcls in cls.__subclasses__():
        print(subcls)
        if len(cls.__subclasses__())>0:
            getSubClasses(subcls)
getSubClasses(QWidget)