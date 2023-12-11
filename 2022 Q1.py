#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 16:06:48 2023

@author: jameswest
"""

import numpy as np

def function(N):
    array = np.zeros(N+1)
    x = np.linspace(1, N+1, N+1)
    array = 1/x**2
    
    approx_pi = np.sqrt(6*np.sum(array))
    
    
    prev_pi = np.sqrt(6*(np.sum(array)-array[N]))
    estimated_error = (approx_pi - prev_pi)/approx_pi
    tru_error = (np.pi - approx_pi)/np.pi
    return approx_pi, tru_error, estimated_error

print(function(10))
print(function(100))
print(function(1000))
