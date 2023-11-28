import os,sys,math,numpy as npy
from mayavi import mlab
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
# from calculatePureVariables import calculatePressure,calculateTemperature,calculateDensity
from wrapperFunctions import calculatePressure,calculateTemperature,calculateDensity

M = 44.01

#Setting which set of parameters to use for calculation.
param_set = 'Self'

P,T = npy.mgrid[1.5:65.0:100j,320.0:1100.0:100j]

Pstar = 419.915520
Tstar = 341.772507
Vstar = 0.71558405

#==============================================================================================================
#Calculating the PVT surface.
#==============================================================================================================

rho_surf = P

#print P.shape
#print T.shape
#print rho_surf.shape

for i in range(0,len(P[0])):
	for j in range(0,len(T[0])):
		rho_surf[i][j] = calculateDensity(P[i][j],T[i][j],M,Pstar=Pstar,Tstar=Tstar,Vstar=Vstar)

#==================================================================================
mlab.figure(figure=None, bgcolor=(1,1,1), fgcolor=None, engine=None, size=(400, 350))
s = mlab.surf(P,T,rho_surf,warp_scale='auto')
mlab.outline(color=(0,0,0))
mlab.text(0.7, 0.16, "Temperature", width=0.2,color=(0,0,0),background_color=(1,1,1))
mlab.text(0.19, 0.15, "Pressure", width=0.2,color=(0,0,0),background_color=(1,1,1))
mlab.text(0.04, 0.5, "Density", width=0.2,color=(0,0,0),background_color=(1,1,1))
#mlab.text(0.28, 0.92, "CO2 Sanchez-Lacombe EOS", width=0.2)
mlab.text(0.20, 0.87, "P*=419.9MPa, T*=341.8K, V*=0.7156g/cm3", width=0.5)

mlab.show()