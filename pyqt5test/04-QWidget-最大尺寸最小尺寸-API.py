#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===================================================
# @Time : 2020/7/7 10:36                           
# @Author : weni09                                  
# @File : 04-QWidget-最大尺寸最小尺寸-API.py
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
    wd.setWindowTitle("最小尺寸最大尺寸限定")
    # wd.resize(500,500)
    # wd.setFixedSize(500,500)
    wd.setMinimumSize(500,500)
    #wd.setMaximumSize(1024,768)
    wd.show()
    sys.exit(app.exec())