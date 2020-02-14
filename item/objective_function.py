# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:03:27 2019

@author: wangwenjie
"""

import numpy as np
import pandas as pd
import os
from write_bladegen_bgi_to_bgd import write_bgi_bgd
from write_bladgen_bgd_to_cfx import write_bgd_cfx
from write_cfxpre_to_cfxsolver import write_cfxpre_cfxsolver
from write_cfxsolver_to_csv import write_cfxsolver_csv
def objective_pump(x):
    write_bgi_bgd(x)
    write_bgd_cfx(x)
    write_cfxpre_cfxsolver(x)
    write_cfxsolver_csv(x)
        
    current_path=os.getcwd()
    x_row=np.shape(x)[0]
    obj1_pumpefficiency=np.zeros([x_row,1])
    obj2_pumphead=np.zeros([x_row,1])
    obj3_pumppower=np.zeros([x_row,1])
    for i in np.arange(x_row):
        filepath_ind_results      = (current_path+'\\b_results\\indi_results_'+'%6.4f'%x[i,0])
        filename_result_csv       = (filepath_ind_results+'\\'+'res_'+'%6.4f'%x[i,0]+'_001.csv')
        if os.path.isfile(filename_result_csv):
            df = pd.DataFrame(pd.read_csv(filename_result_csv))
            performance_data=df.to_numpy()
            obj1_pumpefficiency[i]=np.average(performance_data[-50:,1])
            obj2_pumphead[i]=np.average(performance_data[-50:,2])        
            obj3_pumppower[i]=np.average(performance_data[-50:,3])
            
        else:
            obj1_pumpefficiency[i]=0;
            obj2_pumphead[i]=0;
            obj3_pumppower[i]=0;
            
    pump_performance=np.hstack((obj1_pumpefficiency,obj2_pumphead,obj3_pumppower))
    return pump_performance

