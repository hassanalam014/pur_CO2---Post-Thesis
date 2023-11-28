import os,sys,math,matplotlib.pyplot as plt,numpy as npy
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import AutoMinorLocator
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
# from calculatePureVariables import calculatePressure,calculateTemperature,calculateDensity
from wrapperFunctions import calculatePressure,calculateTemperature,calculateDensity


#Setting font size
axis_size = 6
title_size = 6
size = 6
label_size = 6
plt.rcParams['xtick.labelsize'] = label_size
plt.rcParams['ytick.labelsize'] = label_size

M = 44.01

#Initializing the array of pressure and temperature.
p = npy.linspace(1.5,65.0,250)
t = npy.linspace(320,1100,250)
P,T = npy.meshgrid(p,t)

Pstar = 419.915520
Tstar = 341.772507
Vstar = 0.71558405
Rstar = 1 / Vstar
#==============================================================================================================
#Calculating the PVT surface.
#==============================================================================================================

#Initializing the PVT surface array.
rho_surf = npy.zeros((len(P),len(T)))

#Calculating the PVT surface.
for i in range(0,len(p)):
	for j in range(0,len(t)):
		rho_surf[i,j] = calculateDensity(p[i],t[j],M,Pstar=Pstar,Tstar=Tstar,Rstar=Rstar)

#==================================================================================
#Relative deviation versus T plots.
fig = plt.figure(num=None, figsize=(2.00, 1.70), dpi=300, facecolor='w', edgecolor='k')
ax = fig.add_subplot(111,projection='3d')
levels = npy.arange(0.01, 0.99, 0.01)
#plt.contour(P,T,rho_surf,levels,linewidths=0.5)
#RdYlBu
surf = ax.plot_surface(P,T,rho_surf,rstride=3,cstride=3,cmap=cm.coolwarm,linewidth=0, antialiased=True)

#Setting the axis limits.
ax.set_xlim3d(1.0,68)
ax.set_ylim3d(310.0,1100.0)
ax.set_zlim3d(0.0,1.0)

#title = 'CO2 Sanchez-Lacombe EOS'
param_graphic = r'P*=419.9MPa, T*= 341.8K, $\rho$*=1.397g/cm$^3$'

#Setting the axis labels and title.
ax.set_xlabel('Pressure',fontsize=axis_size)
ax.set_ylabel('Temperature',fontsize=axis_size)
ax.set_zlabel('Density',fontsize=axis_size)
ax.set_title(param_graphic,fontsize=axis_size)

#Removing ticks and tick labels.
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

#Changing the figure orientation.
#ax.view_init(elev=20.0,azim=45.0)

#Saving the figure at the appropriate resolution. Note, saving the figure
#displayed after plt.show() will not preserve resolution.
# fig.savefig('TOC_graphic.png', dpi=300)

#Show plot windows.
plt.show()