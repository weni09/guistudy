#!/usr/bin/python3
# -*- coding: utf-8 -*-
#===================================================
# @Time : 2020/7/1 10:06                           
# @Author : weni09                                  
# @File : __main__.py
#===================================================
import sys
from pyqt5test. import window
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = window()
    #wd.show()
    sys.exit(app.exec())