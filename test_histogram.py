import os,sys,math,numpy as npy,matplotlib.pyplot as plt
from loadExperimentalData import *
from operator import itemgetter, attrgetter

def sortByPressure(P0,T0,R0,I0):
    combined = [[0,1,2,3] for x in range(0,len(P0))]
    combined2 = [range(0,len(P0)) for x in range(0,4)]
    for i in range(0,len(P0)):
        combined[i][0] = P0[i]
        combined[i][1] = T0[i]
        combined[i][2] = R0[i]
        combined[i][3] = I0[i]
        #combined[i][4] = residual[i]
        combined.sort(key=itemgetter(0))
    for i in range(0,len(P0)):
        combined2[0][i] = combined[i][0]
        combined2[1][i] = combined[i][1]
        combined2[2][i] = combined[i][2]
        combined2[3][i] = combined[i][3]
        #residual[i] = combined[i][4]

    return combined

def createHistogram(x0,partition):
    cell_size = (max(x0)-min(x0))/partition
    hist = npy.zeros(partition)
    xpart = npy.zeros(partition)
    result = [range(0,len(xpart)) for x in range(0,2)]
    for i in range(0,len(xpart)):
        xpart[i] = (i+1)*cell_size
    for i in range(0,len(hist)):
        count = 0
        for j in range(0,len(x0)):
            if xpart[i]-cell_size <= x0[j] < xpart[i]:
                count = count + 1
        hist[i] = count
        
        result[0] = xpart
        result[1] = hist
    
    return result

part,number = createHistogram(P0,50)
coeff = npy.polyfit(part,number,5)
fit = range(0,len(P0))
for i in range(0,len(P0)):
    fit[i] = coeff[0]*P0[i]**5+coeff[1]*P0[i]**4+coeff[2]*P0[i]**3+coeff[3]*P0[i]**2+coeff[4]*P0[i]+coeff[5]

plt.plot(part,number,'.')
plt.plot(P0,fit,'rx')
plt.show()