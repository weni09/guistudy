#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===================================================
# @Time : 2020/7/6 17:18                           
# @Author : weni09                                  
# @File : 04-QWidget-案例.py
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
    wd.setWindowTitle("QWidget案例")
    wd.resize(500,500)
    wd.move(300,300)
    # 总的控件个数
    widget_count = 20
    # 列数
    for i in range(widget_count):
        w = QWidget(wd)
        w.resize(100,100)
        w.setStyleSheet("background-color:red;border")

    wd.show()
    sys.exit(app.exec())