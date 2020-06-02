#!/Users/terrycaipen/miniconda3/bin/python3
'''
mac.py maccormack solution of Burgers equation
'''
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

# ===========================================================
# https://www.geeks.forgeeks.org/predictorr-corrector-or-modified-euler-method-for-
# solving-differential-equation.com
# Tannehill, Anderson, Pletcher, Computational Fluid Dynamics and 
# Heat Transfer, 2nd ed, 1994, p. 146.
# Python3 code for solving the 1D Burgers' equation 
# using MacCormack method
# with the given conditions, u(0,t) = 0.0, step size(h) = 1 
# to find u(x,t) 
# ===========================================================
# initialize variables
# ===========================================================
t = 0.0
t1 = 1.0
x0 = 0.0
x1 = 1.0
cols = 101
rows = 201
dx = 0.01
dt = 0.005
h = dt / dx
u = np.zeros((rows, cols))
x = np.linspace(0, 1.0, cols)
# ===========================================================
fig = plt.figure()
ax = plt.axes()
line, =ax.plot([],[],lw=3)
time_text=ax.text(0.02, 0.95, '', transform=ax.transAxes)
ax.set_ylim(0, 2.0)
ax.set_xlim(0, 1.0)
ax.set_xlabel('x-axis')
ax.set_ylabel('u-axis')
ax.set_title('1D Burgers Eq using MacCormack method')
# ===========================================================
def init():
        line.set_data([],[])
        time_text.set_text('')
        return line,time_text

# ===========================================================
def animate(i):
        xp = np.linspace(0, 1.0, cols)
        yp = u[i][0:cols]
        line.set_data(xp,yp)
        t1=.01*i
        time_text.set_text('time = %.3f msec' % t1)
        return line,

# ===========================================================
for i in range(0,50):
    u[0][i] = 1.0
for k in range(1,rows):
    u[k][0] = 1.0
f = 100
# ===========================================================
for m in range(1, rows):
    for n in range(1, cols-1):
        # predictor
        ubar = u[m-1][n] - 0.5 * h * ((u[m -1][n + 1]) ** 2 -
                                        (u[m-1][n] ** 2))
        # corrector
        fbar = 0.5 * (ubar ** 2)
        fbarm = 0.5 * (u[m][n-1] ** 2)
        u[m][n] = 0.5 * (u[m-1][n] + ubar - h * (fbar - fbarm))
#ax.plot(u[100][0:101], x[0:101], c='k')
anim = animation.FuncAnimation(fig,animate,init_func=init,interval=10,frames=f)
mywriter = animation.FFMpegWriter(fps=10, codec="libx264")
anim.save('mac2.mp4', writer=mywriter)
plt.draw()
plt.show()
('\n'
 'FFMpegWriter block taken from:\n'
 'https://github.com/BV-DR/foamBazar/blob/master/pythonScripts/waveProbesPP.py\n')
