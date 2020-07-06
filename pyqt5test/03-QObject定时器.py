#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===================================================
# @Time : 2020/7/6 14:10
# @Author : weni09
# @File : 03-QObject定时器.py
#===================================================

import sys
from PyQt5.Qt import *
class MyObject(QObject):
    def timerEvent(self,evt):
        print(evt,"1")
class MyLabel(QLabel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setText("10")
        self.move(100, 100)
        self.setStyleSheet("font-size:30px;color:red;")
        #self.time_id = self.startTimer(1000)
    def setSec(self,sec):
        self.setText(str(sec))
    def startMyTimer(self,ms):
        self.time_id = self.startTimer(ms)
    def timerEvent(self,*args,**kwargs):
        #print("xx")
        #1.获取当前标签的内容
        current_sec = int(self.text())
        current_sec -= 1
        print(current_sec)
        self.setText(str(current_sec))
        if current_sec == 0:
            print("停止")
            self.killTimer(self.time_id)

class MyWidget(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #print("test1",self.width(),self.height())
        self.resize(100,150)
        #print("tes2",self.width(),self.height())
    def startMyTimer(self,ms):
        self.time_id = self.startTimer(ms)
    def timerEvent(self,*args,**kwargs):
        #print(self.width())
        current_w = self.width()
        current_h = self.height()
        print(current_w, current_h)
        current_w += 50
        current_h += 50
        self.resize(current_w,current_h)
        print(self.width(),self.height())
        if current_w >= 500 and current_h >= 500:
            print("停止放大")
            self.killTimer(self.time_id)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = MyWidget()
    wd.setWindowTitle("QObject定时器的使用")
    wd.startMyTimer(100)

    # wd.resize(500,500)
    # wd.setWindowTitle("QObject定时器的使用")
    # label = MyLabel(wd)
    # label.setSec(5)
    # label.startMyTimer(2000)
    #wd.startTimer(100)
    wd.show()
    sys.exit(app.exec_())