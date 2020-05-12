#!/Users/terrycaipen/miniconda3/bin/python3
''' mac.py maccormack solution of Burgers equation'''
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import pdb
import math
#pdb.set_trace()
#===========================================================
# https://www.geeks.forgeeks.org/predictorr-corrector-or-modified-euler-method-for-
# solving-differential-equation.com
# Tannehill, Anderson, Pletcher, Computational Fluid Dynamics and 
# Heat Transfer, 2nd ed, 1994, p. 146.
# Python3 code for solving the 1D Burgers' equation 
# using MacCormack method
# with the given conditions, u(0,t) = 0.0, step size(h) = 1 
# to find u(x,t) 
#===========================================================
# initialize variables
#===========================================================
t=0.
t1=1.
x0=0.
x1=1.
u=[[]]
x=[]
cols=102
rows=102
#dx=3.14159/(cols-1)
dx=0.01
dt=.01
h=dt/dx
u=np.zeros((rows,cols))
x=np.linspace(0,1.01,102)
#===========================================================
#for k in range(0,102):
u[:][0]=1.0
u[0][:]=1.0
u[101][:]=1.0
#===========================================================
for m in range(1,101):
	for n in range(1,101):
		#predictor
		ubar  = u[m][n-1] - 0.5*h*((u[m+1][n-1])**2-(u[m][n-1]**2))
		#corrector
		fbar  = 0.5*(ubar**2)
		fbarm = 0.5*(u[m-1][n]**2)
		u[m][n]=0.5*(u[m][n-1]+ubar-h*(fbar-fbarm))
		print(u[m][n-1],u[m+1,n-1],u[m][n-1],u[m,n])
		if n==50:
			y=u[m][:]
			plt.plot(x,y)
			plt.show()
