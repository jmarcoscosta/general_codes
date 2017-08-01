# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:11:45 2017

@author: João Marcos Costa

"""

def find_capacitance(desired_PF,actual_PF,V_rms,f_Hz,Power_W_load):
	import math
	theta_desired_PF = (math.acos(desired_PF))
	theta_actual_PF = (math.acos(actual_PF))
#	print(theta_actual_PF,theta_desired_PF)
	return Power_W_load*(math.tan(theta_actual_PF)-math.tan(theta_desired_PF))/(2*math.pi*f_Hz*V_rms**2)
	
C = find_capacitance(0.95,0.8,120,60,4000)
print "%.1e" % C