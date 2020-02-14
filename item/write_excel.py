# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:59:23 2019

@author: wangwenjie
"""

import pandas as pd
def write_results_excel(x,results_file_path,columns_head):
    df=pd.DataFrame(x,columns=columns_head)
    writer=pd.ExcelWriter(results_file_path)
    df.to_excel(writer)
    writer.close()