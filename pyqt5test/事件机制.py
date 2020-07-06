#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===================================================
# @Time : 2020/7/3 8:14                           
# @Author : weni09                                  
# @File : 事件机制.py
#===================================================

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton
from PyQt5.QtCore import QEvent

class App(QApplication):
    def notify(self,recevier, evt):
        if recevier.inherits("QPushButton") and evt.type() == QEvent.MouseButtonRelease:
            #print(recevier,evt)
            pass
        return super().notify(recevier,evt)

class Btn(QPushButton):
    def event(self,evt):
        if evt.type() == QEvent.MouseButtonRelease:
           print("按钮被点击了-Ww",evt)
        return super().event(evt)
    def mouseReleaseEvent(self,evt):
        print("鼠标被松开了")
        return super().mouseReleaseEvent(evt)
    
if __name__ == '__main__':
    app = App(sys.argv)
    window = QWidget()
    btn = Btn(window)
    btn.setText("按钮")
    btn.move(150,150)
    n = 1
    def slot():
        global n
        print("按钮被点击了",n,"次")
        n += 1
    btn.clicked.connect(slot)
    window.show()
    sys.exit(app.exec_())