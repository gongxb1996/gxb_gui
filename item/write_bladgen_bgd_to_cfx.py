# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:38:50 2019

@author: wangwenjie
"""

import numpy as np
import os
from kill_workbench_timeout import run_workbench
def write_bgd_cfx(x):
    current_path=os.getcwd()
    current_path_wbpj_new=current_path.replace('\\', '/')
    x_row=np.shape(x)[0]
    for i in np.arange(x_row):
        filepath_ind_results    = (current_path+'\\b_results\\indi_results_'+'%6.4f'%x[i,0])                    
        file_path_wbpj_new      = filepath_ind_results.replace('\\', '/')
        filename_workbench_wbjn = (filepath_ind_results+'\\'+'workbench_'+'%6.4f'%x[i,0]+'_'+'wb'+'.wbjn') 
        filename_workbench_wbpj = ('workbench_'+'%6.4f'%x[i,0]+'_'+'wb'+'.wbpj') 
        filename_impeller_bgd   = ('bladegen_impeller_'+'%6.4f'%x[i,0]+'.bgd')
        filename_workbench_bat  = (filepath_ind_results+'\\'+'launcher_workbench_'+'%6.4f'%x[i,0]+'.bat')
        filename_cfx_def        = (filepath_ind_results+'\\'+'workbench_'+'%6.4f'%x[i,0]+'_'+'wb'+'_'+'files'\
                                   +'\\dp0\\CFX\\CFX\\CFX.def')
        if os.path.isfile(filename_workbench_bat):
            os.remove(filename_workbench_bat)
        if os.path.isfile(filename_workbench_wbjn):
            os.remove(filename_workbench_wbjn)
        # write wbjn file 
        fp_wbjn=open(current_path+'\\'+'C_workbench_cfx_basic.txt',encoding='utf-8').readlines()
        fp_new_wbjn=open(filename_workbench_wbjn,'w',encoding='utf-8')
        try:
            for eachline in fp_wbjn:
                fp_new_wbjn.write(eachline.replace('current_name_wbpj',current_path_wbpj_new)\
                                         .replace('reference_path_name_wbpj',file_path_wbpj_new)\
                                         .replace('reference_name_wbpj',filename_workbench_wbpj)\
                                         .replace('bladegen_reference_impeller',filename_impeller_bgd))

        finally:
            fp_new_wbjn.close()
        # write bat file  
        fp_workbench_bat=open(current_path+'\\'+'B2_bat_workbench.txt').readlines()
        fp_new_workbench_bat=open(filename_workbench_bat,'w')
        try:
            for eachline in fp_workbench_bat:
                fp_new_workbench_bat.write(eachline.replace('filenamewbjn',filename_workbench_wbjn))

        finally:
            fp_new_workbench_bat.close()
        
        # launch workbench
#        os.system(filename_workbench_bat)
        run_workbench(filename_workbench_bat)
        print('workbench bat is successful')
        
        # rename and copy def
        new_filename_cfx_def      = (filepath_ind_results+'\\'+'cfx_'+'%6.4f'%x[i,0]+'.def')
        os.renames (filename_cfx_def,new_filename_cfx_def)

    