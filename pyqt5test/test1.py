#!/usr/bin/python3
# -*- coding: utf-8 -*-
#===================================================
# @Time : 2020/6/29 15:50
# @Author : weni09
# @File : test1.py
#===================================================

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    def setup_ui(self):
        obj0 = QObject()
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()
        obj4 = QObject()
        obj5 = QObject()
        obj2.setObjectName("2")
        obj3.setObjectName("3")
        print("obj0",obj0)
        print("obj1",obj1)
        print("obj2",obj2)
        print("obj3",obj3)
        print("obj4",obj4)
        print("obj5",obj5)

        obj1.setParent(obj0)
        obj2.setParent(obj0)
        obj3.setParent(obj1)
        obj4.setParent(obj2)
        obj5.setParent(obj2)

        # print(obj1.parent())
        # print(obj2.parent())
        # print(obj0.children())
        # print(obj0.findChildren(QObject,None,Qt.FindChildrenRecursively))
        # print(obj0.findChild(QObject,"3",Qt.FindChildrenRecursively))
