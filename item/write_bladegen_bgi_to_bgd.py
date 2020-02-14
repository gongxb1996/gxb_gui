# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:00:32 2019

@author: wangwenjie
"""

import numpy as np
import os
def write_bgi_bgd(x):
    # create folder for each case
    current_path=os.getcwd()
    x_row=np.shape(x)[0]
    for i in np.arange(x_row):
        filepath_ind_results=(current_path+'\\b_results\\indi_results_'+'%6.4f'%x[i,0])
        if not os.path.isdir(filepath_ind_results):
            os.mkdir('b_results\indi_results_'+'%6.4f'%x[i,0])
        else:
            os.rmdir('b_results\indi_results_'+'%6.4f'%x[i,0])
            os.mkdir('b_results\indi_results_'+'%6.4f'%x[i,0])
        filename_bladegen_impeller_bat = (filepath_ind_results+'\\'+'launcher_bladegen_impeller_'+'%6.4f'%x[i,0]+'.bat')
        filename_impeller_bgi          = (filepath_ind_results+'\\'+'bladegen_impeller_'+'%6.4f'%x[i,0]+'.bgi')
        filename_impeller_bgd          = (filepath_ind_results+'\\'+'bladegen_impeller_'+'%6.4f'%x[i,0]+'.bgd')
        filename_impeller_rtzt         = (filepath_ind_results+'\\'+'bladegen_impeller_'+'%6.4f'%x[i,0]+'.rtzt')
        if os.path.isfile(filename_bladegen_impeller_bat):
            os.remove(filename_bladegen_impeller_bat)
        if os.path.isfile(filename_impeller_bgi):
            os.remove(filename_impeller_bgi)
        if os.path.isfile(filename_impeller_bgd):
            os.remove(filename_impeller_bgd)
        if os.path.isfile(filename_impeller_rtzt):
            os.remove(filename_impeller_rtzt)
        # write bgi file 
        fp_bgi=open(current_path+'\\'+'C_bladegen_impeller_basic.txt').readlines()
        fp_new_bgi=open(filename_impeller_bgi,'w')
        try:
            for eachline in fp_bgi:
                fp_new_bgi.write(eachline.replace('variable001','%6.4f'%x[i,0])\
                                         .replace('variable002','%6.4f'%x[i,1])\
                                         .replace('variable003','%6.4f'%x[i,2])\
                                         .replace('variable004','%6.4f'%x[i,3])\
                                         .replace('variable005','%6.4f'%x[i,4])\
                                         .replace('variable006','%6.4f'%x[i,5])\
                                         .replace('variable007','%6.4f'%x[i,6])\
                                  )

        finally:
            fp_new_bgi.close()
        # write bat file  
        fp_bladegen_bat=open(current_path+'\\'+'B1_bat_bladegen.txt').readlines()
        fp_new_bladegen_bat=open(filename_bladegen_impeller_bat,'w')
        try:
            for eachline in fp_bladegen_bat:
                fp_new_bladegen_bat.write(eachline.replace('filenamebgibatch',filename_impeller_bgi)\
                                         .replace('filenamebgdbatch',filename_impeller_bgd)\
                                         .replace('filenamertztbatch',filename_impeller_rtzt)\
                                  )

        finally:
            fp_new_bladegen_bat.close()   
            
        # launch bladegen
        os.system(filename_bladegen_impeller_bat)
        print('bladegen bat is successful')
            
            
            
            
            
            