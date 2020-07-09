#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===================================================
# @Time : 2020/7/9 10:18                           
# @Author : weni09                                  
# @File : 04-QWidget-鼠标相关操作.py
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
    wd.setWindowTitle("鼠标操作")
    wd.resize(500,500)


    # pixmap = QPixmap("./mouseicon.png")
    # new_pixmap = pixmap.scaled(30,30)
    # cursor = QCursor(new_pixmap,0,0)
    # wd.setCursor(cursor)
    # # wd.unsetCursor()
    # print(wd.cursor())
    #
    # currentCursor = wd.cursor()
    # print(currentCursor.pos())
    # currentCursor.setPos(100,100)
    # print(currentCursor.pos())

    # label = QLabel(wd)
    # label.setText("大本营代震墀电光火石")
    # label.resize(100,100)
    # label.setStyleSheet("background-color:cyan;")
    # label.setCursor(Qt.WhatsThisCursor)


    wd.show()
    sys.exit(app.exec_())