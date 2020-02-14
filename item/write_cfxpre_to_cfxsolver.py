# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:00:50 2019

@author: wangwenjie
"""

import numpy as np
import os
def write_cfxpre_cfxsolver(x):
    current_path=os.getcwd()
    x_row=np.shape(x)[0]
    for i in np.arange(x_row):
        filepath_ind_results      = (current_path+'\\b_results\\indi_results_'+'%6.4f'%x[i,0])
        filename_cfx_def          = (filepath_ind_results+'\\'+'cfx_'+'%6.4f'%x[i,0]+'.def')
        filename_result           = (filepath_ind_results+'\\'+'res_'+'%6.4f'%x[i,0]+'_001')
        filename_result_wb_backup = (filepath_ind_results+'\\'+'.workbench_'+'%6.4f'%x[i,0]+'_wb_files.backup')
        filename_cfxsolve_bat          = (filepath_ind_results+'\\'+'launcher_cfx_'+'%6.4f'%x[i,0]+'.bat')
                               
        # write bat file  
        fp_cfxsolve_bat=open(current_path+'\\'+'B3_bat_cfxsolve.txt').readlines()
        fp_new_cfxsolve_bat=open(filename_cfxsolve_bat,'w')
        try:
            for eachline in fp_cfxsolve_bat:
                fp_new_cfxsolve_bat.write(eachline.replace('filenamedef',filename_cfx_def)\
                                                  .replace('filenamerespath',filename_result)
                                                  )

        finally:
            fp_new_cfxsolve_bat.close()
        
        # launch cfxsolver
        if not os.path.isdir(filename_result_wb_backup): 
            os.system(filename_cfxsolve_bat)
            print('cfxsolve bat is successful')