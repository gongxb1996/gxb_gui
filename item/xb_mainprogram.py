# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:50:33 2019

@author: wangwenjie
"""
import numpy as np
import pandas as pd
import os
from objective_function import objective_pump
from write_excel import write_results_excel
from pyDOE2 import lhs

pathfile_bladegen = 'D:\\Program Files\\ANSYS Inc\\v180\\aisol\\BladeModeler\\BladeGen'
pathfile_cfturbo = 'C:\\Program Files\\CFturbo 10.3\\cfturbo.exe'
pathfile_workbench = 'D:\\Program Files\\ANSYS Inc\\v180\\Framework\\bin\\Win64\\RunWB2.exe'
pathfile_cfxsolve = 'D:\\Program Files\\ANSYS Inc\\v180\\CFX\\bin\\cfx5solve.exe'
pathfile_cfxmondata = 'D:\\Program Files\\ANSYS Inc\\v180\\CFX\\bin\\cfx5mondata.exe'
pathfile_cfxpost = 'D:\\Program Files\\ANSYS Inc\\v180\\CFX\\bin\\cfx5post.exe'

current_path = os.getcwd()
filepath_results = (current_path + '\\b_results')
if not os.path.isdir(filepath_results):
    os.mkdir(filepath_results)
bladegen_bat = 'B1_bat_bladegen.txt'
cfturbo_bat = 'B1_bat_cfturbo.txt'
workbench_bat = 'B2_bat_workbench.txt'
cfxsolve_bat = 'B3_bat_cfxsolve.txt'
cfxmondata_bat = 'B4_bat_cfxmondata.txt'
cfxpost_bat = 'B5_bat_cfxpost.txt'
if os.path.isfile(bladegen_bat):
    os.remove(bladegen_bat)
if os.path.isfile(cfturbo_bat):
    os.remove(cfturbo_bat)
if os.path.isfile(workbench_bat):
    os.remove(workbench_bat)
if os.path.isfile(cfxsolve_bat):
    os.remove(cfxsolve_bat)
if os.path.isfile(cfxmondata_bat):
    os.remove(cfxmondata_bat)
if os.path.isfile(cfxpost_bat):
    os.remove(cfxpost_bat)

# write bladegen basic bat file
bladegen_bat_base = 'A1_bat_bladegen.txt'
fp_bladegen01_bat = open(current_path + '\\' + bladegen_bat_base).readlines()
fp_bladegen02_bat = open(bladegen_bat, 'w')
try:
    for eachline in fp_bladegen01_bat:
        fp_bladegen02_bat.write(eachline.replace('bladegen_set_path', pathfile_bladegen))
finally:
    fp_bladegen02_bat.close()

# write cfturbo basic bat file
cfturbo_bat_base = 'A1_bat_cfturbo.txt'
fp_cfturbo01_bat = open(current_path + '\\' + cfturbo_bat_base).readlines()
fp_cfturbo02_bat = open(cfturbo_bat, 'w')
try:
    for eachline in fp_cfturbo01_bat:
        fp_cfturbo02_bat.write(eachline.replace('cfturbo_set_path', pathfile_cfturbo))
finally:
    fp_cfturbo02_bat.close()

# write workbench basic bat file
workbench_bat_base = 'A2_bat_workbench.txt'
fp_workbench01_bat = open(current_path + '\\' + workbench_bat_base).readlines()
fp_workbench02_bat = open(workbench_bat, 'w')
try:
    for eachline in fp_workbench01_bat:
        fp_workbench02_bat.write(eachline.replace('workbench_set_path', pathfile_workbench))
finally:
    fp_workbench02_bat.close()

# write cfxsolve basic bat file
core_cfx_num = input('How many cores do you want to use for cfx: ')
cfxsolve_bat_base = 'A3_bat_cfxsolve.txt'
fp_cfxsolve01_bat = open(current_path + '\\' + cfxsolve_bat_base).readlines()
fp_cfxsolve02_bat = open(cfxsolve_bat, 'w')
try:
    for eachline in fp_cfxsolve01_bat:
        fp_cfxsolve02_bat.write(eachline.replace('cfxsolve_set_path', pathfile_cfxsolve) \
                                .replace('corenum', core_cfx_num))
finally:
    fp_cfxsolve02_bat.close()

# write cfxmondata basic bat file
cfxmondata_bat_base = 'A4_bat_cfxmondata.txt'
fp_cfxmondata01_bat = open(current_path + '\\' + cfxmondata_bat_base).readlines()
fp_cfxmondata02_bat = open(cfxmondata_bat, 'w')
try:
    for eachline in fp_cfxmondata01_bat:
        fp_cfxmondata02_bat.write(eachline.replace('cfxmondata_set_path', pathfile_cfxmondata))
finally:
    fp_cfxmondata02_bat.close()

# write cfxpost basic bat file
cfxpost_bat_base = 'A5_bat_cfxpost.txt'
fp_cfxpost01_bat = open(current_path + '\\' + cfxpost_bat_base).readlines()
fp_cfxpost02_bat = open(cfxpost_bat, 'w')
try:
    for eachline in fp_cfxpost01_bat:
        fp_cfxpost02_bat.write(eachline.replace('cfxpost_set_path', pathfile_cfxpost))
finally:
    fp_cfxpost02_bat.close()

# write all results
results_file_path = 'pump_performance_data.xlsx'
columns_head = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'efficiency', 'head', 'power']

# input dialog 1
calculation = ('Des', 'Opt')

if calculation == calculation[0]:
    print('Des is choosed')
    x = np.array([[60.5, 45.8, 49.7, 54.8, 60.7, 60.0, 65.8]])
    pump_performance = objective_pump(x)
    all_data = np.hstack((x, pump_performance))
    write_results_excel(all_data, results_file_path, columns_head)
else:
    print('Opt is choosed')
    choose_opt_method = ('DOE', 'IA')
    opt_method = input('Which method do you want to choose? design of experiment or intelligent algorithm(DOE/IA): ')
    while opt_method not in choose_opt_method:
        opt_method = input(
            'Which method do you want to choose? design of experiment or intelligent algorithm(DOE/IA): ')
    if opt_method == choose_opt_method[0]:
        print('DOE is choosed')
        choose_DOE = ('New', 'Existed')
        DOE_opt = input('Is the DOE New or Existed(New or Existed): ')
        while DOE_opt not in choose_DOE:
            DOE_opt = input('Is the DOE New or Existed(New or Existed): ')
        if DOE_opt == choose_DOE[0]:
            print('DOE is New')
            x_initial = lhs(7, samples=5, criterion='center')
            ub_array = np.array([70.0, 80.0, 80.0, 80.0, 80.0, 80.0, 68.0])
            lb_array = np.array([50.0, 40.0, 40.0, 40.0, 40.0, 40.0, 58.0])
            x = np.multiply(x_initial, (ub_array - lb_array)) + lb_array
            filename_new_doe = 'DOE_new_design.xlsx'
            if not os.path.isdir(filename_new_doe):
                write_results_excel(x, filename_new_doe, ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7'])
            else:
                os.rmdir(filename_new_doe)
                write_results_excel(x, filename_new_doe, ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7'])
            pump_performance = objective_pump(x)
            all_data = np.hstack((x, pump_performance))
            write_results_excel(all_data, results_file_path, columns_head)
        else:
            print('DOE is Existed')
            filename_existed_doe = 'DOE_existed_design.xlsx'
            df = pd.DataFrame(pd.read_excel(filename_existed_doe))
            x = df.to_numpy()[..., 1:]
            pump_performance = objective_pump(x)
            all_data = np.hstack((x, pump_performance))
            write_results_excel(all_data, results_file_path, columns_head)
    else:
        print('IA is choosed')
        f_objective = lambda x: objective_pump(x)
        numpop = 20
        numiter = 500
        functiondim = 2
        lb = -32 * np.ones([1, functiondim])
        ub = 32 * np.ones([1, functiondim])
        echo = 'on'
        opt_method_algorithm = ['PSO', 'GSA', 'GA', 'BA', 'ABC']
        opt_algorithm = input('which algorithm is used: ')
        while opt_method_algorithm not in opt_algorithm:
            opt_algorithm = input('which algorithm is used: ')
        if opt_algorithm == 'PSO':
            from pso_algorithm import pso

            print('PSO is choosed')
            [xgbest, fgbest, fbest] = pso(f_objective, numpop, functiondim, lb, ub, numiter, echo)
        #        elif opt_algorithm=='GSA':
        #            from gsa_algorithm import gsa
        #            print ('GSA is choosed')
        #            [xgbest,fgbest,fbest]=gsa(f_objective,numpop,functiondim,lb,ub,numiter,echo)
        #        elif opt_algorithm=='GA':
        #            from ga_algorithm import ga
        #            print ('GA is choosed')
        #            [xgbest,fgbest,fbest]=gsa(f_objective,numpop,functiondim,lb,ub,numiter,echo)
        #        elif opt_algorithm=='BA':
        #            from ba_algorithm import ba
        #            print ('BA is choosed')
        #            [xgbest,fgbest,fbest]=ba(f_objective,numpop,functiondim,lb,ub,numiter,echo)
        #        else:
        #            from abc_algorithm import abc
        #            print ('ABC is choosed')
        #            [xgbest,fgbest,fbest]=abc(f_objective,numpop,functiondim,lb,ub,numiter,echo)

        all_data = np.hstack((xgbest, fgbest))
        filename_global_best = 'IA_global_best.xlsx'
        write_results_excel(all_data, filename_global_best, ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'y'])
        filename_iteration_best = 'IA_iteration_best.xlsx'
        write_results_excel(fbest, filename_iteration_best, ['y'])















