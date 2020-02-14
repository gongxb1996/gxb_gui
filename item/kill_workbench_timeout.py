# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:12:57 2019

@author: wenji
"""

import threading
import sys
import os

class Dispacher(threading.Thread):
    def __init__(self, fun,args):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.result = None
        self.error = None
        self.fun = fun
        self.args = args
        self.start()
    def run(self):
        try:
            self.result = self.fun(self.args)
        except:
            self.error = sys.exc_info()

def workbench_fun(filename_workbench_bat):
    os.system(filename_workbench_bat)


def run_workbench(filename_workbench_bat):
    c = Dispacher(workbench_fun, filename_workbench_bat)
    c.join(600)
    if c.isAlive():
        print('TimeOutError')
        os.system("taskkill /F /IM AnsysFW.exe")            