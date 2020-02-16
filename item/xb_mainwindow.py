# -*- coding:utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from xb_testWindow import TestWindow
from xb_openWindow import OpenWindow
from xb_printWindow import PrintWindow
from xb_data1Window import Data1Window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
    # 初始化
    def initUI(self):
        self.setWindowTitle('算法测试')
        self.setWindowIcon(QIcon('..\\icon\\panda.ico'))
        self.resize(700, 500)
        self.center()
        QToolTip.setFont(QFont('SansSerif',12))
        # 菜单栏1
        self.menu1 = self.menuBar()
        self.file = self.menu1.addMenu('文件')
        self.open = QAction('新建',self)
        self.file.addAction(self.open)
        self.save = QAction('保存',self)
        self.save.setShortcut('Ctrl+S')
        self.file.addAction(self.save)
        self.print = QAction('打印', self)
        self.file.addAction(self.print)
        self.quit = QAction('退出', self)
        self.file.addAction(self.quit)

        self.open.triggered.connect(OpenWindow)
        self.print.triggered.connect(PrintWindow)
        # 菜单栏2
        self.menu2 = self.menuBar()
        self.find = self.menu2.addMenu('查找')
        find1 = QAction('查找',self)
        self.find.addAction(find1)

        # 菜单栏3
        self.menu3 = self.menuBar()
        self.data = self.menu3.addMenu('数据')
        data1 = QAction('Data1',self)
        data2 = QAction('Data2', self)
        data3 = QAction('Data3', self)
        self.data.addAction(data1)
        self.data.addAction(data2)
        self.data.addAction(data3)
        data1.triggered.connect(Data1Window)
        # 菜单栏4
        self.menu4 = self.menuBar()
        self.test = self.menu4.addMenu('测算')
        testing = QAction('测试',self)
        testset = QAction('设置',self)
        self.test.addAction(testing)
        self.test.addAction(testset)
        testing.triggered.connect(TestWindow)
        # 菜单栏5
        self.menu5 = self.menuBar()
        self.help = self.menu5.addMenu('帮助')

        # 工具栏
        self.tool = self.addToolBar('File')
        self.new = QAction(QIcon('..\\icon\\new.ico'),'新建',self)
        self.tool.addAction(self.new)
        self.open = QAction(QIcon('..\\icon\\open2.ico'), '打开', self)
        self.tool.addAction(self.open)
        self.save = QAction(QIcon('..\\icon\\save2.ico'), '保存', self)
        self.tool.addAction(self.save)
        self.find = QAction(QIcon('..\\icon\\find2.ico'), '查找', self)
        self.tool.addAction(self.find)
        self.test = QAction(QIcon('..\\icon\\test1.ico'), '测试', self)
        self.tool.addAction(self.test)
        self.tool.actionTriggered.connect(self.testcall)

        # 状态栏
        self.status = self.statusBar()
        self.status.showMessage('这是提示信息',5000)
        # 按钮模块
        self.exit_button = QPushButton('关闭窗口')
        self.exit_button.clicked.connect(self.exitbutton)
        layout = QHBoxLayout()
        layout.addWidget(self.exit_button)
        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    # 窗口居中
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        width = (screen.width() - size.width()) / 2
        height = (screen.height() - size.height()) / 2
        self.move(width, height)
    # 退出按钮
    def exitbutton(self):
        sender = self.sender()
        print(sender.text() + '被按下了')
        qApp = QApplication.instance()
        qApp.quit()
    # tool_texttrigger
    def testcall(self, a):
        if a.text() == '测试':
            self.testwindow = TestWindow()
            self.testwindow.show()
        elif a.text() == '新建':
            self.open = OpenWindow()
            self.open.show()
        elif a.text() == '打开':
            self.open = OpenWindow()
            self.open.show()
        elif a.text() == '保存':
            self.open = OpenWindow()
            self.open.show()
        elif a.text() == '查找':
            pass





if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('..\\icon\\panda.ico'))
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())