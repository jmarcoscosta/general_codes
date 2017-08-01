# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:11:45 2017

@author: João Marcos Costa

"""

def find_capacitance(desired_PF,actual_PF,V_rms,w_angfreq,Power_W_load):
	import math
	theta_desired_PF = math.degrees(math.acos(desired_PF))
	theta_actual_PF = math.degrees(math.acos(actual_PF))
	
	return Power_W_load*(math.tan(theta_actual_PF)-math.tan(theta_desired_PF))/(w_angfreq*V_rms**2)
	
