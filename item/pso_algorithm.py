# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:13:44 2019

@author: wangwenjie
"""
import numpy as np

def pso(f_objective,numpop,functiondim,lb,ub,numiter,echo):    

    echo='on'
    lb_array=np.tile(lb,(numpop,1))
    ub_array=np.tile(ub,(numpop,1))

#--------------------------initialization--------------------------  
    t_rand=np.random.random((numpop,functiondim))
    
    x = np.multiply(t_rand,(ub_array-lb_array))+lb_array
    v = np.zeros([numpop,functiondim],dtype=float)
    vmax=0.1*(ub_array-lb_array)
#--------------------------coefficients of pso--------------------------
    wmax=1.2
    wmin=0.8
    c1=2
    c2=2
#--------------------------initialization calculation--------------------------

    fbest=np.zeros([numiter,1],dtype=float)
    f=f_objective(x)
    fmin=np.min(f)
    fminindex=np.where(f==np.min(fmin))[0][0]
    xgbest=np.multiply(np.ones([numpop,1]),x[fminindex,...])
    fgbest=np.multiply(np.ones([numpop,1]),fmin)
    fpbest=f
    xpbest=x
    j=0
    fbest[j]=fgbest[0]
    if echo=='on':
        print("The current iteration is %5d, the global minimum is %12.7f" %(j,fgbest[0]))
    
    
    while j<numiter-1:
        j=j+1
        #-------update coefficients, velocity and position of pso
        w=wmax+(wmin-wmax)*j/numiter
        v=w*v+c1*np.multiply(np.random.random((numpop,functiondim)),(xpbest-x))+\
        c2*np.multiply(np.random.random((numpop,functiondim)),(xgbest-x))
        x=x+v
        #-------constrain the velocity and position
        [row,col]=np.where(x>ub_array)
        x[row,col]=ub_array[row,col]
        [row,col]=np.where(x<lb_array)
        x[row,col]=lb_array[row,col]
        
        [row,col]=np.where(v>vmax)
        v[row,col]=vmax[row,col]
        [row,col]=np.where(v<-vmax)
        v[row,col]=-vmax[row,col]
        
        
        #-------update the fpbest and fgbest of pso
        f=f_objective(x)
        
        row_min=np.where(f<fpbest)[0]
        xpbest[row_min]=x[row_min]
                
        fmin=np.min(f)
        fminindex=np.where(f==np.min(fmin))[0][0]
        if fmin<fgbest[0]:
            xgbest=np.multiply(np.ones([numpop,1]),x[fminindex,...])
            fgbest=np.multiply(np.ones([numpop,1]),fmin)
        fbest[j]=fgbest[0]
        if echo=='on':
            print("The current iteration is %5d, the global minimum is %12.7f" %(j,fbest[j]))
    if echo=='on':
        print("Finally, the global value of the objective is %12.7f" %fbest[j])
        
#--------------------------initialization calculation-------------------------- 
    return (xgbest,fgbest,fbest)
        
            
    