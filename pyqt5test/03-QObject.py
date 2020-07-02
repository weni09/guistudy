#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===================================================
# @Time : 2020/6/29 15:50
# @Author : weni09
# @File : test1.py
#===================================================
import sys
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton
from PyQt5.QtCore import Qt
# from PyQt5.Qt import *
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
        #self.QObject对象名称和属性()
        self.QObject信号操作()
    def QObject对象名称和属性(self):
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
        print(obj0.findChild(QObject,"2",Qt.FindChildrenRecursively))
        #********************内存管理***************************开始
        obj1 = QObject()
        self.obj1 = obj1
        obj2 = QObject()
        obj2.setParent(obj1)

        # 监听obj2对象被释放

        obj2.destroyed.connect(lambda _:print("obj2对象被释放了"))
        del self.obj1

        #*********************内存管理**************************结束
    def QObject信号操作(self):
        # self.obj = QObject()
        # def destroy_cao(obj):
        #     print("对象被释放了",obj)
        # self.obj.destroyed.connect(destroy_cao)
        # del self.obj
        # def obj_name_cao(name):
        #     print("对象名称发生了改变",name)
        # def obj_name_cao2(name):
        #     print("对象名称发生了改变2",name)
        # self.obj.objectNameChanged.connect(obj_name_cao)
        # self.obj.objectNameChanged.connect(obj_name_cao2)
        # self.obj.setObjectName("XXXXXX")
        # print(self.obj.receivers(self.obj.objectNameChanged)) #返回连接到信号的接收器数量
        # print(self.obj.signalsBlocked())#信号是否被阻止 (获取阻塞状态)
        # # self.obj.objectNameChanged.disconnect(obj_name_cao)
        #
        # self.obj.blockSignals(True) # 阻塞信号 是否阻塞连接
        # print(self.obj.signalsBlocked())
        # self.obj.setObjectName("oooooooooooo")
        # self.obj.blockSignals(False) #恢复连接
        # print(self.obj.signalsBlocked())
        # # self.obj.objectNameChanged.connect(obj_name_cao)
        # self.obj.setObjectName("xxxoo")
        #***********************信号与槽案例************************开始
        btn = QPushButton(self)
        btn.setText("点击我")
        btn.move(150,150)
        def slot():
            print("占我嘎哈?")
        btn.clicked.connect(slot)
        #***********************信号与槽案例************************结束

def QWidget控件的父子关系():
    app = QApplication(sys.argv)
    qssStayle  = CommonHelper.readQss('./QObject.qss')
    app.setStyleSheet(qssStayle)
    # print(qssStayle)
    wd1 = QWidget()
    wd1.setObjectName('one')
    wd1.show()
    wd2 = QWidget()
    wd2.setObjectName('one')
    wd2.setProperty("one_level","normal")
    wd2.setParent(wd1)
    wd2.resize(200,200)
    wd2.show()
    sys.exit(app.exec())()
def QObject信号与槽案例():
    """
    @修改窗口标题时自动加上前缀`械-`
    """
    app = QApplication(sys.argv)
    wd = QWidget()
    def cao(title):
        print("窗口标题变化了",title)
        wd.blockSignals(True)
        wd.setWindowTitle("械-" + title)
        wd.blockSignals(False)
    wd.windowTitleChanged.connect(cao)
    wd.setWindowTitle("hello ww")
    wd.setWindowTitle("hello ww2")
    wd.setWindowTitle("hello ww3")
    wd.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # QWidget控件的父子关系()
    # QObject信号与槽案例()
    wd = window()
    wd.resize(400,400)
    wd.setWindowTitle("OObject的学习")
    wd.show()
    sys.exit(app.exec())