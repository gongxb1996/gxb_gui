# -*- coding:utf-8 -*-
import re
import sys
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from xb_testwindow import TestWindow


class Data1Window(QWidget):
    def __init__(self):
        super(Data1Window, self).__init__()
        self.initUI()
    # 初始化
    def initUI(self):
        self.setWindowTitle('读取数据')
        self.setWindowIcon(QIcon('..\\icon\\data.ico'))
        self.resize(780,300)
        # 读取文件数据
        dialog = QFileDialog()
        dialog.setWindowTitle('打开文件')
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            filename = dialog.selectedFiles()
            with open(filename[0], encoding='utf-8', mode='r+') as f:
                data = f.read()
                f.close()
        # 正则表达提取数据group(2)
        result1 = re.search(r'New AngleCurve(.*?)Begin Data(.*?)End Data', data, flags=re.S)
        result2 = re.search(r'New ThicknessCurve(.*?)Begin Data(.*?)End Data', data, flags=re.S)
        AngleCurveData = result1.group(2)
        ThicknessCurveData = result2.group(2)
        # 读取到列表
        list1_str = re.findall(r'(-?\d+\.\d+)', AngleCurveData)
        list2_str = re.findall(r'(-?\d+\.\d+)', ThicknessCurveData)
        xs1 = list1_str[::2]
        ys1 = list1_str[1::2]
        xs2 = list2_str[::2]
        ys2 = list2_str[1::2]
        # tableAngleCurve数据表格
        self.tableAngleCurve = QTableWidget()
        self.tableAngleCurve.setWindowTitle('AngleCurve')
        self.tableAngleCurve.setColumnCount(8)
        self.tableAngleCurve.setRowCount(2)
        self.tableAngleCurve.setHorizontalHeaderLabels([str(j) for j in range(1, 9)])
        self.tableAngleCurve.setVerticalHeaderLabels(['x1', 'y1'])
        # tableThicknessCurve数据表格
        self.tableThicknessCurve = QTableWidget()
        self.tableThicknessCurve.setColumnCount(8)
        self.tableThicknessCurve.setRowCount(2)
        self.tableThicknessCurve.setHorizontalHeaderLabels([str(j) for j in range(1, 9)])
        self.tableThicknessCurve.setVerticalHeaderLabels(['x2', 'y2'])
        # 布局
        vbox = QVBoxLayout()
        self.labelAngle = QLabel('AngleCurve')
        self.labelThickness = QLabel('ThicknessCurve')
        vbox.addWidget(self.labelAngle)
        vbox.addWidget(self.tableAngleCurve)
        vbox.addWidget(self.labelThickness)
        vbox.addWidget(self.tableThicknessCurve)

        for i in range(7):
            x1_item = QTableWidgetItem(xs1[i])
            self.tableAngleCurve.setItem(0,i,x1_item)
        for i in range(7):
            y1_item = QTableWidgetItem(ys1[i])
            self.tableAngleCurve.setItem(1,i,y1_item)
        for i in range(7):
            x2_item = QTableWidgetItem(xs2[i])
            self.tableThicknessCurve.setItem(0,i,x2_item)
        for i in range(7):
            y2_item = QTableWidgetItem(ys2[i])
            self.tableThicknessCurve.setItem(1,i,y2_item)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('..\\icon\\data.ico'))
    ex = Data1Window()
    ex.show()
    sys.exit(app.exec_())