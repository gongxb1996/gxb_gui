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
            f = open(filename[0], encoding='utf-8', mode='r+')
            with f:
                data = f.read()
                self.opentext.setText(data)


    def saveDialog(self):
        dialog = QDialog()
        dialog.setWindowTitle('保存提醒')
        dialog.setGeometry(400,300,50,50)
        layout = QVBoxLayout()
        hbox = QHBoxLayout()
        btn1 = QPushButton('保存')
        btn2 = QPushButton('不保存')
        btn3 = QPushButton('取消')
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

        label = QLabel('是否要保存文件')
        layout.addWidget(label)
        layout.addLayout(hbox)
        dialog.setLayout(layout)
        btn1.clicked.connect(self.saveItem)
        btn2.clicked.connect(dialog.close)
        btn3.clicked.connect(dialog.close)
        # 设置模式状态，除非关闭对话框，否则原窗口无法使用
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()
    def saveItem(self):
        savedialog = QFileDialog()
        savedialog.setWindowTitle('保存文件')
        fname = savedialog.getSaveFileName(self, '保存文件', '../', '文本文件(*.txt )')
        if savedialog.exec():
            with open(fname[0], 'w') as f:
                my_text = self.opentext.toPlainText()
                f.write(my_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OpenWindow()
    ex.show()
    sys.exit(app.exec_())