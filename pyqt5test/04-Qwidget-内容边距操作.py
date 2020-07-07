#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===================================================
# @Time : 2020/7/7 11:04                           
# @Author : weni09                                  
# @File : 04-Qwidget-内容边距操作.py
#===================================================

import sys
from PyQt5.Qt import *
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    def setup_ui(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = window()
    wd.setWindowTitle("内容边距的设定")
    wd.resize(500,500)
    label = QLabel(wd)
    label.setText("中国梅花草日光灯发到")
    label.resize(300,300)
    label.setStyleSheet("background-color:cyan;")
    label.setContentsMargins(170,270,0,0)
    print(label.contentsRect())
    print(label.getContentsMargins())
    wd.show()
    sys.exit(app.exec())