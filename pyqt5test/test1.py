#!/usr/bin/python3
# -*- coding: utf-8 -*-
#===================================================
# @Time : 2020/6/29 15:50
# @Author : weni09
# @File : test2.py
#===================================================
import sys
from PyQt5.Qt import *

''''
def getSubClasses(cls):
    for subcls in cls.__subclasses__():
        print(subcls)
        if len(cls.__subclasses__())>0:
            getSubClasses(subcls)
getSubClasses(QWidget)

'''
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    def setup_ui(self):
