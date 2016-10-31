# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 22:35:13 2016

@author: Tayari
"""

import pandas as pd
import numpy as np
def bscatter(X,Y,k):
    Xnom, thresh=pd.qcut(X, k, retbins=True)
    tp = pd.DataFrame({'Xnom': Xnom, 'X': X, 'Y':Y})
    GMn  = tp.groupby('Xnom').mean()
    SeMn = tp.groupby('Xnom').std()/ np.sqrt(tp.groupby('Xnom').count())
    Xq = GMn.X
    Yq = GMn.Y
    XSe = SeMn.X
    YSe = SeMn.Y
    return(Xq,XSe,Yq,YSe)