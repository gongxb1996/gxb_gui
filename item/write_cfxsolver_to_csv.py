# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:27:10 2019

@author: wangwenjie
"""

import numpy as np
import os
def write_cfxsolver_csv(x):
    current_path=os.getcwd()
    x_row=np.shape(x)[0]

    for i in np.arange(x_row):
        filepath_ind_results      = (current_path+'\\b_results\\indi_results_'+'%6.4f'%x[i,0])
        filename_cfxmondata_bat   = (filepath_ind_results+'\\'+'launcher_mondata_'+'%6.4f'%x[i,0]+'.bat')
        filename_result_res       = (filepath_ind_results+'\\'+'res_'+'%6.4f'%x[i,0]+'_001.res')
        filename_result_csv       = (filepath_ind_results+'\\'+'res_'+'%6.4f'%x[i,0]+'_001.csv')
        if os.path.isfile(filename_result_res):
        # write bat file  
            fp_cfxmondata_bat=open(current_path+'\\'+'B4_bat_cfxmondata.txt').readlines()
            fp_new_cfxmondata_bat=open(filename_cfxmondata_bat,'w')
            try:
                for eachline in fp_cfxmondata_bat:
                    fp_new_cfxmondata_bat.write(eachline.replace('filenameres',filename_result_res)\
                                                  .replace('filenamecsv',filename_result_csv)
                                                  )

            finally:
                fp_new_cfxmondata_bat.close()
        
            # launch cfxsolver

            os.system(filename_cfxmondata_bat)
            print('cfxmondata bat is successful')
        else:
            print('cfxmondata bat of this case is failed')

    
        