# -*- coding:utf-8 -*-
import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class OpenWindow(QMainWindow):
    def __init__(self):
        super(OpenWindow, self).__init__()
        self.initUI()
    # 初始化
    def initUI(self):
        self.setWindowTitle('新建文本文档')
        self.setWindowIcon(QIcon('..\\icon\\new.ico'))
        self.resize(660, 550)
        self.move(300,50)
        self.setMinimumSize(300,200)

        bar = self.menuBar()
        file = bar.addMenu('File')
        open = QAction('Open',self)
        file.addAction(open)
        save = QAction('Save', self)
        save.setShortcut('Ctrl + S')
        file.addAction(save)

        open.triggered.connect(self.openItem)
        save.triggered.connect(self.saveItem)

        quit = QAction('Quit', self)
        file.addAction(quit)
        quit.triggered.connect(self.close)

        self.opentext = QTextEdit(self)
        self.setCentralWidget(self.opentext)
        self.opentext.setToolTip('请编辑文本')
        self.opentext.setPlaceholderText('在此输入文本')
    def openItem(self):
        dialog = QFileDialog()
        dialog.setWindowTitle('打开文件')
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            filename = dialog.selectedFiles()
            with open(filename[0], encoding='utf-8', mode='r+') as f:
                data = f.read()
                self.opentext.setText(data)
                f.close()
    # 窗口关闭保存事件
    def closeEvent(self, QCloseEvent):
        res = QMessageBox.question(self, '保存提醒', '是否保存文件？',
                                   QMessageBox.Yes | QMessageBox.No|QMessageBox.Cancel,QMessageBox.Yes)
        if res == QMessageBox.Yes:
            savedialog1 = QFileDialog()
            savedialog1.setWindowTitle('保存文件')
            fname = savedialog1.getSaveFileName(self, '保存文件', '../', '文本文件(*.txt )')
            with open(fname[0], 'w') as f:
                my_text = self.opentext.toPlainText()
                f.write(my_text)
                f.close()
                QCloseEvent.ignore()
        elif res == QMessageBox.No:
            self.close()
        elif res == QMessageBox.Cancel:
            QCloseEvent.ignore()
    def saveItem(self):
        savedialog = QFileDialog()
        savedialog.setWindowTitle('保存文件')
        fname = savedialog.getSaveFileName(self, '保存文件', '../', '文本文件(*.txt )')
        with open(fname[0], 'w') as f:
            my_text = self.opentext.toPlainText()
            f.write(my_text)
            f.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OpenWindow()
    ex.show()
    sys.exit(app.exec_())