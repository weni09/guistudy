#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===================================================
# @Time : 2020/7/6 17:18                           
# @Author : weni09                                  
# @File : 04-QWidget-案例.py
#===================================================

import sys
from PyQt5.QtWidgets import QWidget,QApplication
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    def setup_ui(self):
        pass

####控件的位置和大小
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = window()
    wd.setWindowTitle("QWidget案例")
    wd.resize(500,500)
    wd.move(600,300)
    # 总的控件个数
    widget_count = 100
    # 列数
    column_num = 5
    # 控件列行距
    column_interval,row_interval = 10,10
    #控件宽和高
    widget_w = (500-(column_num-1)*column_interval) / column_num
    widget_h = (500 + row_interval) / (widget_count/column_num) - row_interval
    for i in range(widget_count):
        w = QWidget(wd)
        widget_x = (i % column_num) * (widget_w + column_interval)
        widget_y = (i // column_num) * (widget_h + row_interval)
        #w.resize(widget_w,widget_h)
        #w.move(widget_x,widget_y)
        w.setGeometry(widget_x,widget_y,widget_w,widget_h)
        #w.resize(100,100)
        w.setStyleSheet("background-color: gray;border: 1px solid red;")

    wd.show()
    sys.exit(app.exec())