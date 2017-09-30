# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 20:38:03 2017

@author: joaomarcos
"""

import numpy as np
import matplotlib.pyplot as plt

import fseries as fs

import csv

with open('p1.csv', 'r') as f:
  reader = csv.reader(f)
  p1_ = list(reader)
  
p1_.pop(0)  
p1_.pop(0)  
p1 = np.ndarray(len(p1_),dtype='float64')
t = np.ndarray(len(p1_),dtype='float64')

#extração dos valores de tensão e tempo correspondentes
for i in range(len(p1)):
    p1[i] = float(p1_[i][1])
    t[i]  = float(p1_[i][0])

