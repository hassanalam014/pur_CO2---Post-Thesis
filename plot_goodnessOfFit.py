import os,sys,math,csv,matplotlib.pyplot as plt,numpy as npy
from loadExperimentalData import *
from all_s_params import *
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
from calculatePureResidual import calculateSSQ,calculateARD
from calculatePureVariables import calculateHoleVolume,scaledCurves,calculatePureCriticalPoint
from pylab import *

#CO2 molecular weight
M = 44.01

#Setting font size
axis_size = 20
title_size = 20
size = 16
label_size = 16
plt.rcParams['xtick.labelsize'] = label_size
plt.rcParams['ytick.labelsize'] = label_size

#Setting saved image properties
img_extension = '.pdf'
img_dpi = None
output_folder = 'plot_goodness_of_fit'

#Checking for existence of output directory. If such a directory doesn't exist, one is created.
if not os.path.exists('./'+output_folder):
    os.makedirs('./'+output_folder)

weight = True

PE = 1.5
TE = 15.0
	
x0 = npy.linspace(0,0.18,20)

sP0 = npy.concatenate((P0_323,P0_373,P0_380,P0_400,P0_420,P0_660,P0_1100),axis=0)
sT0 = npy.concatenate((T0_323,T0_373,T0_380,T0_400,T0_420,T0_660,T0_1100),axis=0)
sR0 = npy.concatenate((R0_323,R0_373,R0_380,R0_400,R0_420,R0_660,R0_1100),axis=0)
sM0 = npy.concatenate((M0_323,M0_373,M0_380,M0_400,M0_420,M0_660,M0_1100),axis=0)
sI0 = npy.concatenate((I0_323,I0_373,I0_380,I0_400,I0_420,I0_660,I0_1100),axis=0)

SSQ_P_Wang = calculateSSQ(P0,T0,R0,M0,I0,'P',Pc0,Tc0,Rc0,PE,TE,Pstar=Wang_Pstar,Tstar=Wang_Tstar,Rstar=Wang_Rstar)
#SSQ_R_Wang = calculateSSQ(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Wang_Pstar,Tstar=Wang_Tstar,Rstar=Wang_Rstar)
result = scaledCurves(Wang_Pstar,Wang_Tstar,Wang_Rstar,sP0,sT0,sR0,sM0,sI0)
GP_Wang = result[0]
GR_Wang = result[1]
SSQ_R_Wang = 0.0085
print('Wang SSQ_P: {}, SSQ_R: {}, v*: Not Fixed'.format(SSQ_P_Wang,SSQ_R_Wang))

SSQ_P_Kilpatrick = calculateSSQ(P0,T0,R0,M0,I0,'P',Pc0,Tc0,Rc0,PE,TE,Pstar=Kilpatrick_Pstar,Tstar=Kilpatrick_Tstar,Rstar=Kilpatrick_Rstar)
SSQ_R_Kilpatrick = calculateSSQ(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Kilpatrick_Pstar,Tstar=Kilpatrick_Tstar,Rstar=Kilpatrick_Rstar)
ARD_R_Kilpatrick = calculateARD(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Kilpatrick_Pstar,Tstar=Kilpatrick_Tstar,Rstar=Kilpatrick_Rstar,weight=weight)
result = scaledCurves(Kilpatrick_Pstar,Kilpatrick_Tstar,Kilpatrick_Rstar,sP0,sT0,sR0,sM0,sI0)
GP_Kilpatrick = result[0]
GR_Kilpatrick = result[1]
Kilpatrick_vs = calculateHoleVolume(Kilpatrick_Pstar,Kilpatrick_Tstar)
r = (Kilpatrick_Pstar*M)/(8.31*Kilpatrick_Tstar*Kilpatrick_Rstar)
Kilpatrick_Tc = Kilpatrick_Tstar*(2*r/(1+math.sqrt(r))**2)
Kilpatrick_Pc = Kilpatrick_Pstar*(2/(1+math.sqrt(r))**2)*(r*math.log(1+1/math.sqrt(r))+0.5-math.sqrt(r))
print('Kilpatrick SSQ_P: {}, SSQ_R: {},  ARD_R: {}, Tc: {} , Pc: {}, v*: {}'.format(SSQ_P_Kilpatrick,SSQ_R_Kilpatrick,ARD_R_Kilpatrick,Kilpatrick_Tc,Kilpatrick_Pc,Kilpatrick_vs))

SSQ_P_Kiszka = calculateSSQ(P0,T0,R0,M0,I0,'P',Pc0,Tc0,Rc0,PE,TE,Pstar=Kiszka_Pstar,Tstar=Kiszka_Tstar,Rstar=Kiszka_Rstar)
SSQ_R_Kiszka = calculateSSQ(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Kiszka_Pstar,Tstar=Kiszka_Tstar,Rstar=Kiszka_Rstar)
ARD_R_Kiszka = calculateARD(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Kiszka_Pstar,Tstar=Kiszka_Tstar,Rstar=Kiszka_Rstar,weight=weight)
result = scaledCurves(Kiszka_Pstar,Kiszka_Tstar,Kiszka_Rstar,sP0,sT0,sR0,sM0,sI0)
GP_Kiszka = result[0]
GR_Kiszka = result[1]
Kiszka_vs = calculateHoleVolume(Kiszka_Pstar,Kiszka_Tstar)
r = (Kiszka_Pstar*M)/(8.31*Kiszka_Tstar*Kiszka_Rstar)
Kiszka_Tc = Kiszka_Tstar*(2*r/(1+math.sqrt(r))**2)
Kiszka_Pc = Kiszka_Pstar*(2/(1+math.sqrt(r))**2)*(r*math.log(1+1/math.sqrt(r))+0.5-math.sqrt(r))
print('Kiszka SSQ_P: {}, SSQ_R: {}, ARD_R: {}, Tc: {}, Pc: {}, v*: {}'.format(SSQ_P_Kiszka,SSQ_R_Kiszka,ARD_R_Kiszka,Kiszka_Tc,Kiszka_Pc,Kiszka_vs))

SSQ_P_Pope = calculateSSQ(P0,T0,R0,M0,I0,'P',Pc0,Tc0,Rc0,PE,TE,Pstar=Pope_Pstar,Tstar=Pope_Tstar,Rstar=Pope_Rstar)
SSQ_R_Pope = calculateSSQ(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Pope_Pstar,Tstar=Pope_Tstar,Rstar=Pope_Rstar)
ARD_R_Pope = calculateARD(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Pope_Pstar,Tstar=Pope_Tstar,Rstar=Pope_Rstar,weight=weight)
result = scaledCurves(Pope_Pstar,Pope_Tstar,Pope_Rstar,sP0,sT0,sR0,sM0,sI0)
GP_Pope = result[0]
GR_Pope = result[1]
Pope_vs = calculateHoleVolume(Pope_Pstar,Pope_Tstar)
r = (Pope_Pstar*M)/(8.31*Pope_Tstar*Pope_Rstar)
Pope_Tc = Pope_Tstar*(2*r/(1+math.sqrt(r))**2)
Pope_Pc = Pope_Pstar*(2/(1+math.sqrt(r))**2)*(r*math.log(1+1/math.sqrt(r))+0.5-math.sqrt(r))
print('Pope SSQ_P: {}, SSQ_R: {}, ARD_R: {}, Tc: {}, Pc: {}, v*: {}'.format(SSQ_P_Pope,SSQ_R_Pope,ARD_R_Pope,Pope_Tc,Pope_Pc,Pope_vs))

SSQ_P_Hariharan = calculateSSQ(P0,T0,R0,M0,I0,'P',Pc0,Tc0,Rc0,PE,TE,Pstar=Hariharan_Pstar,Tstar=Hariharan_Tstar,Rstar=Hariharan_Rstar)
SSQ_R_Hariharan = calculateSSQ(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Hariharan_Pstar,Tstar=Hariharan_Tstar,Rstar=Hariharan_Rstar)
ARD_R_Hariharan = calculateARD(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Hariharan_Pstar,Tstar=Hariharan_Tstar,Rstar=Hariharan_Rstar,weight=weight)
result = scaledCurves(Hariharan_Pstar,Hariharan_Tstar,Hariharan_Rstar,sP0,sT0,sR0,sM0,sI0)
GP_Hariharan = result[0]
GR_Hariharan = result[1]
Hariharan_vs = calculateHoleVolume(Hariharan_Pstar,Hariharan_Tstar)
r = (Hariharan_Pstar*M)/(8.31*Hariharan_Tstar*Hariharan_Rstar)
Hariharan_Tc = Hariharan_Tstar*(2*r/(1+math.sqrt(r))**2)
Hariharan_Pc = Hariharan_Pstar*(2/(1+math.sqrt(r))**2)*(r*math.log(1+1/math.sqrt(r))+0.5-math.sqrt(r))
print('Hariharan SSQ_P: {}, SSQ_R: {}, ARD_R: {}, Tc: {}, Pc: {}, v*: {}'.format(SSQ_P_Hariharan,SSQ_R_Hariharan,ARD_R_Hariharan,Hariharan_Tc,Hariharan_Pc,Hariharan_vs))

SSQ_P_Garg = calculateSSQ(P0,T0,R0,M0,I0,'P',Pc0,Tc0,Rc0,PE,TE,Pstar=Garg_Pstar,Tstar=Garg_Tstar,Rstar=Garg_Rstar)
SSQ_R_Garg = calculateSSQ(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Garg_Pstar,Tstar=Garg_Tstar,Rstar=Garg_Rstar)
ARD_R_Garg = calculateARD(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Garg_Pstar,Tstar=Garg_Tstar,Rstar=Garg_Rstar,weight=weight)
result = scaledCurves(Garg_Pstar,Garg_Tstar,Garg_Rstar,sP0,sT0,sR0,sM0,sI0)
GP_Garg = result[0]
GR_Garg = result[1]
Garg_vs = calculateHoleVolume(Garg_Pstar,Garg_Tstar)
r = (Garg_Pstar*M)/(8.31*Garg_Tstar*Garg_Rstar)
Garg_Tc = Garg_Tstar*(2*r/(1+math.sqrt(r))**2)
Garg_Pc = Garg_Pstar*(2/(1+math.sqrt(r))**2)*(r*math.log(1+1/math.sqrt(r))+0.5-math.sqrt(r))
print('Garg SSQ_P: {}, SSQ_R: {}, ARD_R: {}, Tc: {}, Pc: {}, v*: {}'.format(SSQ_P_Garg,SSQ_R_Garg,ARD_R_Garg,Garg_Tc,Garg_Pc,Garg_vs))

SSQ_P_Xiong = calculateSSQ(P0,T0,R0,M0,I0,'P',Pc0,Tc0,Rc0,PE,TE,Pstar=Xiong_Pstar,Tstar=Xiong_Tstar,Rstar=Xiong_Rstar)
SSQ_R_Xiong = calculateSSQ(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Xiong_Pstar,Tstar=Xiong_Tstar,Rstar=Xiong_Rstar)
ARD_R_Xiong = calculateARD(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Xiong_Pstar,Tstar=Xiong_Tstar,Rstar=Xiong_Rstar,weight=weight)
result = scaledCurves(Xiong_Pstar,Xiong_Tstar,Xiong_Rstar,sP0,sT0,sR0,sM0,sI0)
GP_Xiong = result[0]
GR_Xiong = result[1]
Xiong_vs = calculateHoleVolume(Xiong_Pstar,Xiong_Tstar)
r = (Xiong_Pstar*M)/(8.31*Xiong_Tstar*Xiong_Rstar)
Xiong_Tc = Xiong_Tstar*(2*r/(1+math.sqrt(r))**2)
Xiong_Pc = Xiong_Pstar*(2/(1+math.sqrt(r))**2)*(r*math.log(1+1/math.sqrt(r))+0.5-math.sqrt(r))
print('Xiong SSQ_P: {}, SSQ_R: {}, ARD_R: {}, Tc: {}, Pc: {}, v*: {}'.format(SSQ_P_Xiong,SSQ_R_Xiong,ARD_R_Xiong,Xiong_Tc,Xiong_Pc,Xiong_vs))

SSQ_P_Cao = calculateSSQ(P0,T0,R0,M0,I0,'P',Pc0,Tc0,Rc0,PE,TE,Pstar=Cao_Pstar,Tstar=Cao_Tstar,Rstar=Cao_Rstar)
SSQ_R_Cao = calculateSSQ(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Cao_Pstar,Tstar=Cao_Tstar,Rstar=Cao_Rstar)
ARD_R_Cao = calculateARD(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Cao_Pstar,Tstar=Cao_Tstar,Rstar=Cao_Rstar,weight=weight)
result = scaledCurves(Cao_Pstar,Cao_Tstar,Cao_Rstar,sP0,sT0,sR0,sM0,sI0)
GP_Cao = result[0]
GR_Cao = result[1]
Cao_vs = calculateHoleVolume(Cao_Pstar,Cao_Tstar)
r = (Cao_Pstar*M)/(8.31*Cao_Tstar*Cao_Rstar)
Cao_Tc = Cao_Tstar*(2*r/(1+math.sqrt(r))**2)
Cao_Pc = Cao_Pstar*(2/(1+math.sqrt(r))**2)*(r*math.log(1+1/math.sqrt(r))+0.5-math.sqrt(r))
print('Cao SSQ_P: {}, SSQ_R: {}, ARD_R: {}, Tc: {}, Pc: {}, v*: {}'.format(SSQ_P_Cao,SSQ_R_Cao,ARD_R_Cao,Cao_Tc,Cao_Pc,Cao_vs))

SSQ_P_Nalawade = calculateSSQ(P0,T0,R0,M0,I0,'P',Pc0,Tc0,Rc0,PE,TE,Pstar=Nalawade_Pstar,Tstar=Nalawade_Tstar,Rstar=Nalawade_Rstar)
SSQ_R_Nalawade = calculateSSQ(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Nalawade_Pstar,Tstar=Nalawade_Tstar,Rstar=Nalawade_Rstar)
ARD_R_Nalawade = calculateARD(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Nalawade_Pstar,Tstar=Nalawade_Tstar,Rstar=Nalawade_Rstar,weight=weight)
result = scaledCurves(Nalawade_Pstar,Nalawade_Tstar,Nalawade_Rstar,sP0,sT0,sR0,sM0,sI0)
GP_Nalawade = result[0]
GR_Nalawade = result[1]
Nalawade_vs = calculateHoleVolume(Nalawade_Pstar,Nalawade_Tstar)
r = (Nalawade_Pstar*M)/(8.31*Nalawade_Tstar*Nalawade_Rstar)
Nalawade_Tc = Nalawade_Tstar*(2*r/(1+math.sqrt(r))**2)
Nalawade_Pc = Nalawade_Pstar*(2/(1+math.sqrt(r))**2)*(r*math.log(1+1/math.sqrt(r))+0.5-math.sqrt(r))
print('Nalawade SSQ_P: {}, SSQ_R: {}, ARD_R: {}, Tc: {}, Pc: {}, v*: {}'.format(SSQ_P_Nalawade,SSQ_R_Nalawade,ARD_R_Nalawade,Nalawade_Tc,Nalawade_Pc,Nalawade_vs))

SSQ_P_Self = calculateSSQ(P0,T0,R0,M0,I0,'P',Pc0,Tc0,Rc0,PE,TE,Pstar=Self_Pstar,Tstar=Self_Tstar,Rstar=Self_Rstar)
SSQ_R_Self = calculateSSQ(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Self_Pstar,Tstar=Self_Tstar,Rstar=Self_Rstar)
ARD_R_Self = calculateARD(P0,T0,R0,M0,I0,'R',Pc0,Tc0,Rc0,PE,TE,Pstar=Self_Pstar,Tstar=Self_Tstar,Rstar=Self_Rstar,weight=weight)
result = scaledCurves(Self_Pstar,Self_Tstar,Self_Rstar,sP0,sT0,sR0,sM0,sI0)
GP_Self = result[0]
GR_Self = result[1]
Self_vs = calculateHoleVolume(Self_Pstar,Self_Tstar)
r = (Self_Pstar*M)/(8.31*Self_Tstar*Self_Rstar)
Self_Tc = Self_Tstar*(2*r/(1+math.sqrt(r))**2)
Self_Pc = Self_Pstar*(2/(1+math.sqrt(r))**2)*(r*math.log(1+1/math.sqrt(r))+0.5-math.sqrt(r))
print('Our own SSQ_P: {}, SSQ_R: {}, ARD_R: {}, Tc: {}, Pc: {}, v*: {}'.format(SSQ_P_Self,SSQ_R_Self,ARD_R_Self,Self_Tc,Self_Pc,Self_vs))

#Sorting the SSQs for display.
def getKey(item):
    return item[0]
SSQ_P_values = [SSQ_P_Kilpatrick,SSQ_P_Pope,SSQ_P_Hariharan,SSQ_P_Kiszka,SSQ_P_Cao,SSQ_P_Garg,SSQ_P_Nalawade,SSQ_P_Xiong,SSQ_P_Self]
SSQ_R_values = [SSQ_R_Kilpatrick,SSQ_R_Pope,SSQ_R_Hariharan,SSQ_R_Kiszka,SSQ_R_Cao,SSQ_R_Garg,SSQ_R_Nalawade,SSQ_R_Xiong,SSQ_R_Self]
SSQ_names = ['Kilpatrick','Pope','Hariharan','Kiszka','Cao','Garg','Nalawade','Xiong','Present work']
SSQ_P_sValues = range(0,len(SSQ_P_values))
SSQ_R_sValues = range(0,len(SSQ_R_values))
SSQ_sNames = range(0,len(SSQ_P_values))
SSQ = [[0,1,2] for x in range(0,len(SSQ_P_values))]
for i in range(0,len(SSQ_P_values)):
    SSQ[i][0] = SSQ_P_values[i]
    SSQ[i][1] = SSQ_R_values[i]
    SSQ[i][2] = SSQ_names[i]
SSQ.sort(key=getKey,reverse=True)
for i in range(0,len(SSQ_P_values)):
    SSQ_P_sValues[i] = SSQ[i][0]
    SSQ_R_sValues[i] = SSQ[i][1]
    SSQ_sNames[i] = SSQ[i][2]

#Sorting the ARDs for display.
def getKey(item):
    return item[0]
ARD_R_values = [ARD_R_Kilpatrick,ARD_R_Pope,ARD_R_Hariharan,ARD_R_Kiszka,ARD_R_Cao,ARD_R_Garg,ARD_R_Nalawade,ARD_R_Xiong,ARD_R_Self]
ARD_names = ['Kilpatrick','Pope','Hariharan','Kiszka','Cao','Garg','Nalawade','Xiong','Present work']
ARD_R_sValues = range(0,len(ARD_R_values))
ARD_sNames = range(0,len(ARD_names))
ARD = [[0,1] for x in range(0,len(ARD_R_values))]
for i in range(0,len(ARD_R_values)):
    ARD[i][0] = ARD_R_values[i]
    ARD[i][1] = ARD_names[i]
ARD.sort(key=getKey,reverse=True)
for i in range(0,len(ARD_R_values)):
    ARD_R_sValues[i] = ARD[i][0]
    ARD_sNames[i] = ARD[i][1]

#plt.figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
#plt.plot(x0,x0,'-b')
#plt.plot(GP_Wang,GR_Wang,'>r')
#plt.plot(GP_Kilpatrick,GR_Kilpatrick,'og')
#plt.plot(GP_Kiszka,GR_Kiszka,'sb')
#plt.plot(GP_Pope,GR_Pope,'dc')
#plt.plot(GP_Hariharan,GR_Hariharan,'^m')
#plt.plot(GP_Cao,GR_Cao,'<',color='0.75')
#plt.plot(GP_Garg,GR_Garg,'vy')
#plt.plot(GP_Nalawade,GR_Nalawade,'h',color='0.5')
#plt.plot(GP_Xiong,GR_Xiong,'*k')
#plt.plot(GP_Self,GR_Self,'*r')
#plt.xlabel(r'f($\tilde{\rho}$)',fontsize=axis_size)
#plt.ylabel(r'$\tilde{P}$',fontsize=axis_size)
#plt.legend(('Reference','Wang','Kilpatrick','Pope','Hariharan','Kiszka','Cao','Garg','Nalawade','Xiong','Present Study'),loc=4,fontsize=size,numpoints=1)
#axes().set_aspect('equal')

#plt.figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
#plt.plot(x0,x0,'-b')
#plt.plot(GP_Wang,GR_Wang,'>r')
#plt.plot(GP_Kilpatrick,GR_Kilpatrick,'og')
#plt.plot(GP_Kiszka,GR_Kiszka,'sb')
#plt.plot(GP_Pope,GR_Pope,'dc')
#plt.plot(GP_Hariharan,GR_Hariharan,'^m')
#plt.plot(GP_Cao,GR_Cao,'<',color='0.75')
#plt.plot(GP_Garg,GR_Garg,'vy')
#plt.plot(GP_Nalawade,GR_Nalawade,'h',color='0.5')
#plt.plot(GP_Xiong,GR_Xiong,'*k')
#plt.plot(GP_Self,GR_Self,'*r')
#plt.xlabel(r'f($\tilde{\rho}$)',fontsize=axis_size)
#plt.ylabel(r'$\tilde{P}$',fontsize=axis_size)
#plt.legend(('Reference','Wang','Kilpatrick','Kiszka','Pope','Hariharan','Cao','Garg','Nalawade','Xiong','Present Study'),loc=4,fontsize=size,numpoints=1)
#plt.axis([0,0.03,0,0.03])
#axes().set_aspect('equal')

figSSQ = fig = plt.figure(num=None, figsize=(12, 14), dpi=img_dpi, facecolor='w', edgecolor='k')
ax = fig.add_subplot(111)
ind = npy.arange(len(SSQ_P_sValues))
width = 0.35
rects1 = ax.bar(ind,SSQ_P_sValues,width,color='gray',edgecolor='black')
rects2 = ax.bar(ind+width,SSQ_R_sValues,width,color='white',edgecolor='black', hatch="/")
ax.set_xlim(-width,len(ind)+width)
ax.set_ylabel(r'SSQ',fontsize=axis_size)
#ax.set_ylabel(r'SSQ$_\rho$',fontsize=axis_size)
xTickMarks = SSQ_sNames
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
#ax.set_yscale('log')
plt.setp(xtickNames, rotation=45, fontsize=label_size)
figSSQ.savefig('./'+output_folder+r'\pure_CO2_ssq'+img_extension,dpi=img_dpi)

figARD = fig = plt.figure(num=None, figsize=(12, 14), dpi=img_dpi, facecolor='w', edgecolor='k')
ax2 = fig.add_subplot(111)
ind = npy.arange(len(ARD_R_sValues))
width = 0.35
rects3 = ax2.bar(ind,ARD_R_sValues,width,color='gray',edgecolor='black')
ax2.set_xlim(-width,len(ind)+width)
ax2.set_ylabel(r'ARD %',fontsize=axis_size)
xTickMarks2 = ARD_sNames
ax2.set_xticks(ind+width)
xtickNames2 = ax2.set_xticklabels(xTickMarks2)
#ax.set_yscale('log')
plt.setp(xtickNames2, rotation=45, fontsize=label_size)
figARD.savefig('./'+output_folder+r'\pure_CO2_ard'+img_extension,dpi=img_dpi)

#fig, ax1 = plt.subplots()
#ax1.plot(t, s1, 'b-')
#ax1.set_xlabel('time (s)')
# Make the y-axis label and tick labels match the line color.
#ax1.set_ylabel('exp', color='b')
#for tl in ax1.get_yticklabels():
#    tl.set_color('b')


#ax2 = ax1.twinx()
#for tl in ax2.get_yticklabels():
#    tl.set_color('r')

#fig2 = plt.figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
#ax = fig2.add_subplot(111)
#ind = npy.arange(len(SSQ_LP_list))
#width = 0.35
#rects1 = ax.bar(ind,SSQ_LP_list,width,color='blue')
#ax.set_xlim(-width,len(ind)+width)
#ax.set_ylabel('SSQ',fontsize=axis_size)
#xTickMarks = ['Wang','Kilpatrick','Pope','Hariharan','Kiszka','Cao','Garg','Nalawade','Xiong']
#ax.set_xticks(ind+width)
#xtickNames = ax.set_xticklabels(xTickMarks)
#ax.set_yscale('log')
#plt.setp(xtickNames, rotation=45, fontsize=label_size)

#fig3 = plt.figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
#ax = fig3.add_subplot(111)
#ind = npy.arange(len(SSQ_HP_list))
#width = 0.35
#rects1 = ax.bar(ind,SSQ_HP_list,width,color='blue')
#ax.set_xlim(-width,len(ind)+width)
#ax.set_ylabel('SSQ',fontsize=axis_size)
#xTickMarks = ['Wang','Kilpatrick','Pope','Hariharan','Kiszka','Cao','Garg','Nalawade','Xiong']
#ax.set_xticks(ind+width)
#xtickNames = ax.set_xticklabels(xTickMarks)
#ax.set_yscale('log')
#plt.setp(xtickNames, rotation=45, fontsize=label_size)

#Show plot windows.
plt.show()