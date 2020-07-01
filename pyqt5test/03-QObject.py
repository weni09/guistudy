#!/usr/bin/python3
# -*- coding: utf-8 -*-
#===================================================
# @Time : 2020/6/29 15:50
# @Author : weni09
# @File : test1.py
#===================================================
import sys
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget,QApplication


class CommonHelper:
    def __init__(self):
        pass
    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()

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



        print(obj1.parent())
        print(obj2.parent())
        print(obj0.children())
        print(obj0.findChildren(QObject,None,Qt.FindChildrenRecursively))
        print(obj0.findChild(QObject,"3",Qt.FindChildrenRecursively))

        #********************内存管理***************************开始
        obj1 = QObject()
        self.obj1 = obj1
        obj2 = QObject()
        obj2.setParent(obj1)

        # 监听obj2对象被释放

        obj2.destroyed.connect(lambda _:print("obj2对象被释放了"))
        del self.obj1

        #*********************内存管理**************************结束


if __name__ == '__main__':
    app = QApplication(sys.argv)

    qssStayle  = CommonHelper.readQss('./QObject.qss')
    # print(qssStayle)
    app.setStyleSheet(qssStayle)
    wd1 = QWidget()
    wd1.setObjectName('one')
    wd1.show()

    wd2 = QWidget()
    wd2.setObjectName('one')
    wd2.setProperty("one_level","normal")
    wd2.setParent(wd1)
    wd2.resize(200,200)
    wd2.show()

    sys.exit(app.exec())