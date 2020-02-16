# -*- coding:utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

class PrintWindow(QMainWindow):
    def __init__(self):
        super(PrintWindow, self).__init__()
        self.initUI()
    # 初始化
    def initUI(self):
        self.setWindowTitle('打印')
        self.setGeometry(300,300,500,400)
        self.printer = QPrinter()

        self.editor = QTextEdit(self)
        self.editor.setGeometry(20,20,300,270)

        self.openbtn = QPushButton('打开文件',self)
        self.openbtn.move(350,20)

        self.settingbtn = QPushButton('打印设置',self)
        self.settingbtn.move(350,50)

        self.printbtn = QPushButton('打印',self)
        self.printbtn.move(350,80)

        self.openbtn.clicked.connect(self.openFile)
        self.settingbtn.clicked.connect(self.showSettingDialog)
        self.printbtn.clicked.connect(self.showPrintDialog)

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self,'打开文本文件','./')
        if fname[0]:
            with open(fname[0],'r',encoding='utf-8',errors='ignore') as f:
                self.editor.setText(f.read())
    def showSettingDialog(self):
        printDialog = QPageSetupDialog(self.printer,self)
        printDialog.exec()
    def showPrintDialog(self):
        printdialog = QPrintDialog(self.printer,self)
        if QDialog.Accepted == printdialog.exec():
            self.editor.print(self.printer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PrintWindow()
    ex.show()
    sys.exit(app.exec_())