import os,sys,math,csv,numpy as npy
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
from loadData import loadPVTData

# 311K_Rho_Hariharan1993.csv
# 320K_Rho_Duschek1990.csv
# 323K_Rho_Garg1994.csv
# 340K_Rho_Angus1976.csv
# 340K_Rho_Duschek1990.csv
# 355K_Rho_Gokmenoglu1996.csv
# 373K_Rho_Garg1994.csv
# 380K_Rho_Angus1976.csv
# 380K_Rho_Xiong1995_Bl.csv
# 400K_Rho_Xiong1995_Bl.csv
# 410K_Rho_Angus1976.csv
# 420K_Rho_Xiong1995_Bl.csv
# 430K_Rho_Angus1976.csv
# 490K_Rho_Angus1976.csv
# 520K_Rho_Angus1976.csv
# 660K_Rho_Angus1976.csv
# 1100K_Rho_Angus1976.csv
# 
# Coexistence_Angus1976.csv
# Coexistence_Duschek1990.csv
# Coexistence_Newitt1947.csv

#======================================================
#Critical Point and Molecular Weight
#======================================================

Pc0 = 7.38
Tc0 = 304.25
Rc0 = 0.468

#======================================================
#Isotherm PVT Data
#======================================================

with open('Data/220K_Rho_Duschek1990.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_220 = range(0,numpts)
			T0_220 = range(0,numpts)
			R0_220 = range(0,numpts)
			M0_220 = range(0,numpts)
			I0_220 = range(0,numpts)
		if index1 >= 6:
			P0_220[index2] = float(row[0])
			T0_220[index2] = float(row[1])
			R0_220[index2] = float(row[2])
			M0_220[index2] = float(row[3])
			I0_220[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
#P0 = npy.concatenate((P0,P0_220),axis=0)
#T0 = npy.concatenate((T0,T0_220),axis=0)
#R0 = npy.concatenate((R0,R0_220),axis=0)
#M0 = npy.concatenate((M0,M0_220),axis=0)
#I0 = npy.concatenate((I0,I0_220),axis=0)

with open('Data/240K_Rho_Duschek1990.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_240 = range(0,numpts)
			T0_240 = range(0,numpts)
			R0_240 = range(0,numpts)
			M0_240 = range(0,numpts)
			I0_240 = range(0,numpts)
		if index1 >= 6:
			P0_240[index2] = float(row[0])
			T0_240[index2] = float(row[1])
			R0_240[index2] = float(row[2])
			M0_240[index2] = float(row[3])
			I0_240[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
#P0 = npy.concatenate((P0,P0_240),axis=0)
#T0 = npy.concatenate((T0,T0_240),axis=0)
#R0 = npy.concatenate((R0,R0_240),axis=0)
#M0 = npy.concatenate((M0,M0_240),axis=0)
#I0 = npy.concatenate((I0,I0_240),axis=0)

with open('Data/260K_Rho_Duschek1990.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_260 = range(0,numpts)
			T0_260 = range(0,numpts)
			R0_260 = range(0,numpts)
			M0_260 = range(0,numpts)
			I0_260 = range(0,numpts)
		if index1 >= 6:
			P0_260[index2] = float(row[0])
			T0_260[index2] = float(row[1])
			R0_260[index2] = float(row[2])
			M0_260[index2] = float(row[3])
			I0_260[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
#P0 = npy.concatenate((P0,P0_260),axis=0)
#T0 = npy.concatenate((T0,T0_260),axis=0)
#R0 = npy.concatenate((R0,R0_260),axis=0)
#M0 = npy.concatenate((M0,M0_260),axis=0)
#I0 = npy.concatenate((I0,I0_260),axis=0)

with open('Data/280K_Rho_Duschek1990.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_280 = range(0,numpts)
			T0_280 = range(0,numpts)
			R0_280 = range(0,numpts)
			M0_280 = range(0,numpts)
			I0_280 = range(0,numpts)
		if index1 >= 6:
			P0_280[index2] = float(row[0])
			T0_280[index2] = float(row[1])
			R0_280[index2] = float(row[2])
			M0_280[index2] = float(row[3])
			I0_280[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
#P0 = npy.concatenate((P0,P0_280),axis=0)
#T0 = npy.concatenate((T0,T0_280),axis=0)
#R0 = npy.concatenate((R0,R0_280),axis=0)
#M0 = npy.concatenate((M0,M0_280),axis=0)
#I0 = npy.concatenate((I0,I0_280),axis=0)

with open('Data/290K_Rho_Duschek1990.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_290 = range(0,numpts)
			T0_290 = range(0,numpts)
			R0_290 = range(0,numpts)
			M0_290 = range(0,numpts)
			I0_290 = range(0,numpts)
		if index1 >= 6:
			P0_290[index2] = float(row[0])
			T0_290[index2] = float(row[1])
			R0_290[index2] = float(row[2])
			M0_290[index2] = float(row[3])
			I0_290[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
#P0 = npy.concatenate((P0,P0_290),axis=0)
#T0 = npy.concatenate((T0,T0_290),axis=0)
#R0 = npy.concatenate((R0,R0_290),axis=0)
#M0 = npy.concatenate((M0,M0_290),axis=0)
#I0 = npy.concatenate((I0,I0_290),axis=0)

with open('Data/300K_Rho_Duschek1990.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_300 = range(0,numpts)
			T0_300 = range(0,numpts)
			R0_300 = range(0,numpts)
			M0_300 = range(0,numpts)
			I0_300 = range(0,numpts)
		if index1 >= 6:
			P0_300[index2] = float(row[0])
			T0_300[index2] = float(row[1])
			R0_300[index2] = float(row[2])
			M0_300[index2] = float(row[3])
			I0_300[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
#P0 = npy.concatenate((P0,P0_300),axis=0)
#T0 = npy.concatenate((T0,T0_300),axis=0)
#R0 = npy.concatenate((R0,R0_300),axis=0)
#M0 = npy.concatenate((M0,M0_300),axis=0)
#I0 = npy.concatenate((I0,I0_300),axis=0)

with open('Data/303K_Rho_Duschek1990.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_303 = range(0,numpts)
			T0_303 = range(0,numpts)
			R0_303 = range(0,numpts)
			M0_303 = range(0,numpts)
			I0_303 = range(0,numpts)
		if index1 >= 6:
			P0_303[index2] = float(row[0])
			T0_303[index2] = float(row[1])
			R0_303[index2] = float(row[2])
			M0_303[index2] = float(row[3])
			I0_303[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
#P0 = npy.concatenate((P0,P0_303),axis=0)
#T0 = npy.concatenate((T0,T0_303),axis=0)
#R0 = npy.concatenate((R0,R0_303),axis=0)
#M0 = npy.concatenate((M0,M0_303),axis=0)
#I0 = npy.concatenate((I0,I0_303),axis=0)

with open('Data/305K_Rho_Duschek1990.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_305 = range(0,numpts)
			T0_305 = range(0,numpts)
			R0_305 = range(0,numpts)
			M0_305 = range(0,numpts)
			I0_305 = range(0,numpts)
		if index1 >= 6:
			P0_305[index2] = float(row[0])
			T0_305[index2] = float(row[1])
			R0_305[index2] = float(row[2])
			M0_305[index2] = float(row[3])
			I0_305[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
#P0 = npy.concatenate((P0,P0_305),axis=0)
#T0 = npy.concatenate((T0,T0_305),axis=0)
#R0 = npy.concatenate((R0,R0_305),axis=0)
#M0 = npy.concatenate((M0,M0_305),axis=0)
#I0 = npy.concatenate((I0,I0_305),axis=0)

with open('Data/307K_Rho_Duschek1990.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_307 = range(0,numpts)
			T0_307 = range(0,numpts)
			R0_307 = range(0,numpts)
			M0_307 = range(0,numpts)
			I0_307 = range(0,numpts)
		if index1 >= 6:
			P0_307[index2] = float(row[0])
			T0_307[index2] = float(row[1])
			R0_307[index2] = float(row[2])
			M0_307[index2] = float(row[3])
			I0_307[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
#P0 = npy.concatenate((P0,P0_307),axis=0)
#T0 = npy.concatenate((T0,T0_307),axis=0)
#R0 = npy.concatenate((R0,R0_307),axis=0)
#M0 = npy.concatenate((M0,M0_307),axis=0)
#I0 = npy.concatenate((I0,I0_307),axis=0)

with open('Data/310K_Rho_Duschek1990.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_310 = range(0,numpts)
			T0_310 = range(0,numpts)
			R0_310 = range(0,numpts)
			M0_310 = range(0,numpts)
			I0_310 = range(0,numpts)
		if index1 >= 6:
			P0_310[index2] = float(row[0])
			T0_310[index2] = float(row[1])
			R0_310[index2] = float(row[2])
			M0_310[index2] = float(row[3])
			I0_310[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
#P0 = npy.concatenate((P0,P0_310),axis=0)
#T0 = npy.concatenate((T0,T0_310),axis=0)
#R0 = npy.concatenate((R0,R0_310),axis=0)
#M0 = npy.concatenate((M0,M0_310),axis=0)
#I0 = npy.concatenate((I0,I0_310),axis=0)

with open('Data/311K_Rho_Hariharan1993.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_311 = range(0,numpts)
			T0_311 = range(0,numpts)
			R0_311 = range(0,numpts)
			M0_311 = range(0,numpts)
			I0_311 = range(0,numpts)
		if index1 >= 6:
			P0_311[index2] = float(row[0])
			T0_311[index2] = float(row[1])
			R0_311[index2] = float(row[2])
			M0_311[index2] = float(row[3])
			I0_311[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = P0_311
T0 = T0_311
R0 = R0_311
M0 = M0_311
I0 = I0_311

with open('Data/313K_Rho_Duschek1990.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_313 = range(0,numpts)
			T0_313 = range(0,numpts)
			R0_313 = range(0,numpts)
			M0_313 = range(0,numpts)
			I0_313 = range(0,numpts)
		if index1 >= 6:
			P0_313[index2] = float(row[0])
			T0_313[index2] = float(row[1])
			R0_313[index2] = float(row[2])
			M0_313[index2] = float(row[3])
			I0_313[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
#P0 = npy.concatenate((P0,P0_313),axis=0)
#T0 = npy.concatenate((T0,T0_313),axis=0)
#R0 = npy.concatenate((R0,R0_313),axis=0)
#M0 = npy.concatenate((M0,M0_313),axis=0)
#I0 = npy.concatenate((I0,I0_313),axis=0)

with open('Data/320K_Rho_Duschek1990.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_320 = range(0,numpts)
			T0_320 = range(0,numpts)
			R0_320 = range(0,numpts)
			M0_320 = range(0,numpts)
			I0_320 = range(0,numpts)
		if index1 >= 6:
			P0_320[index2] = float(row[0])
			T0_320[index2] = float(row[1])
			R0_320[index2] = float(row[2])
			M0_320[index2] = float(row[3])
			I0_320[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_320),axis=0)
T0 = npy.concatenate((T0,T0_320),axis=0)
R0 = npy.concatenate((R0,R0_320),axis=0)
M0 = npy.concatenate((M0,M0_320),axis=0)
I0 = npy.concatenate((I0,I0_320),axis=0)

# with open('Data/323K_Rho_Garg1994.csv','rb') as csvfile:
# 	datareader = csv.reader(csvfile)
# 	#x0 = (float(column[1]) for column in datareader)
# 	index1 = 0
# 	index2 = 0
# 	for row in datareader:
# 		if index1 == 4:
# 			numpts = int(row[0])
# 			P0_323 = range(0,numpts)
# 			T0_323 = range(0,numpts)
# 			R0_323 = range(0,numpts)
# 			M0_323 = range(0,numpts)
# 			I0_323 = range(0,numpts)
# 		if index1 >= 6:
# 			P0_323[index2] = float(row[0])
# 			T0_323[index2] = float(row[1])
# 			R0_323[index2] = float(row[2])
# 			M0_323[index2] = float(row[3])
# 			I0_323[index2] = 'isotherm'
# 			index2 = index2 + 1
# 		index1 = index1 + 1
P0_323,T0_323,R0_323,M0_323,I0_323 = loadPVTData('Data/323K_Rho_Garg1994.csv','isotherm')
P0 = npy.concatenate((P0,P0_323),axis=0)
T0 = npy.concatenate((T0,T0_323),axis=0)
R0 = npy.concatenate((R0,R0_323),axis=0)
M0 = npy.concatenate((M0,M0_323),axis=0)
I0 = npy.concatenate((I0,I0_323),axis=0)

P0_dev = P0_323
T0_dev = T0_323
R0_dev = R0_323
M0_dev = M0_323
I0_dev = I0_323

with open('Data/340K_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_340A = range(0,numpts)
			T0_340A = range(0,numpts)
			R0_340A = range(0,numpts)
			M0_340A = range(0,numpts)
			I0_340A = range(0,numpts)
		if index1 >= 6:
			P0_340A[index2] = float(row[0])
			T0_340A[index2] = float(row[1])
			R0_340A[index2] = float(row[2])
			M0_340A[index2] = float(row[3])
			I0_340A[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_340A),axis=0)
T0 = npy.concatenate((T0,T0_340A),axis=0)
R0 = npy.concatenate((R0,R0_340A),axis=0)
M0 = npy.concatenate((M0,M0_340A),axis=0)
I0 = npy.concatenate((I0,I0_340A),axis=0)

with open('Data/340K_Rho_Duschek1990.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_340 = range(0,numpts)
			T0_340 = range(0,numpts)
			R0_340 = range(0,numpts)
			M0_340 = range(0,numpts)
			I0_340 = range(0,numpts)
		if index1 >= 6:
			P0_340[index2] = float(row[0])
			T0_340[index2] = float(row[1])
			R0_340[index2] = float(row[2])
			M0_340[index2] = float(row[3])
			I0_340[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_340),axis=0)
T0 = npy.concatenate((T0,T0_340),axis=0)
R0 = npy.concatenate((R0,R0_340),axis=0)
M0 = npy.concatenate((M0,M0_340),axis=0)
I0 = npy.concatenate((I0,I0_340),axis=0)

with open('Data/355K_Rho_Gokmenoglu1996.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_355 = range(0,numpts)
			T0_355 = range(0,numpts)
			R0_355 = range(0,numpts)
			M0_355 = range(0,numpts)
			I0_355 = range(0,numpts)
		if index1 >= 6:
			P0_355[index2] = float(row[0])
			T0_355[index2] = float(row[1])
			R0_355[index2] = float(row[2])
			M0_355[index2] = float(row[3])
			I0_355[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_355),axis=0)
T0 = npy.concatenate((T0,T0_355),axis=0)
R0 = npy.concatenate((R0,R0_355),axis=0)
M0 = npy.concatenate((M0,M0_355),axis=0)
I0 = npy.concatenate((I0,I0_355),axis=0)

with open('Data/373K_Rho_Garg1994.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_373 = range(0,numpts)
			T0_373 = range(0,numpts)
			R0_373 = range(0,numpts)
			M0_373 = range(0,numpts)
			B0_373 = range(0,numpts)
			I0_373 = range(0,numpts)
		if index1 >= 6:
			P0_373[index2] = float(row[0])
			T0_373[index2] = float(row[1])
			R0_373[index2] = float(row[2])
			M0_373[index2] = float(row[3])
			B0_373[index2] = float(row[4])
			I0_373[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_373),axis=0)
T0 = npy.concatenate((T0,T0_373),axis=0)
R0 = npy.concatenate((R0,R0_373),axis=0)
M0 = npy.concatenate((M0,M0_373),axis=0)
I0 = npy.concatenate((I0,I0_373),axis=0)

P0_dev = npy.concatenate((P0_dev,P0_373),axis=0)
T0_dev = npy.concatenate((T0_dev,T0_373),axis=0)
R0_dev = npy.concatenate((R0_dev,R0_373),axis=0)
M0_dev = npy.concatenate((M0_dev,M0_373),axis=0)
I0_dev = npy.concatenate((I0_dev,I0_373),axis=0)

with open('Data/380K_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_380A = range(0,numpts)
			T0_380A = range(0,numpts)
			R0_380A = range(0,numpts)
			M0_380A = range(0,numpts)
			B0_380A = range(0,numpts)
			I0_380A = range(0,numpts)
		if index1 >= 6:
			P0_380A[index2] = float(row[0])
			T0_380A[index2] = float(row[1])
			R0_380A[index2] = float(row[2])
			M0_380A[index2] = float(row[3])
			B0_380A[index2] = float(row[4])
			I0_380A[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_380A),axis=0)
T0 = npy.concatenate((T0,T0_380A),axis=0)
R0 = npy.concatenate((R0,R0_380A),axis=0)
M0 = npy.concatenate((M0,M0_380A),axis=0)
I0 = npy.concatenate((I0,I0_380A),axis=0)

P0_dev = npy.concatenate((P0_dev,P0_380A),axis=0)
T0_dev = npy.concatenate((T0_dev,T0_380A),axis=0)
R0_dev = npy.concatenate((R0_dev,R0_380A),axis=0)
M0_dev = npy.concatenate((M0_dev,M0_380A),axis=0)
I0_dev = npy.concatenate((I0_dev,I0_380A),axis=0)

with open('Data/380K_Rho_Xiong1995_Bl.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_380 = range(0,numpts)
			T0_380 = range(0,numpts)
			R0_380 = range(0,numpts)
			M0_380 = range(0,numpts)
			B0_380 = range(0,numpts)
			I0_380 = range(0,numpts)
		if index1 >= 6:
			P0_380[index2] = float(row[0])
			T0_380[index2] = float(row[1])
			R0_380[index2] = float(row[2])
			M0_380[index2] = float(row[3])
			B0_380[index2] = float(row[4])
			I0_380[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_380),axis=0)
T0 = npy.concatenate((T0,T0_380),axis=0)
R0 = npy.concatenate((R0,R0_380),axis=0)
M0 = npy.concatenate((M0,M0_380),axis=0)
I0 = npy.concatenate((I0,I0_380),axis=0)

with open('Data/400K_Rho_Xiong1995_Bl.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_400 = range(0,numpts)
			T0_400 = range(0,numpts)
			R0_400 = range(0,numpts)
			M0_400 = range(0,numpts)
			I0_400 = range(0,numpts)
		if index1 >= 6:
			P0_400[index2] = float(row[0])
			T0_400[index2] = float(row[1])
			R0_400[index2] = float(row[2])
			M0_400[index2] = float(row[3])
			I0_400[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_400),axis=0)
T0 = npy.concatenate((T0,T0_400),axis=0)
R0 = npy.concatenate((R0,R0_400),axis=0)
M0 = npy.concatenate((M0,M0_400),axis=0)
I0 = npy.concatenate((I0,I0_400),axis=0)

with open('Data/410K_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_410 = range(0,numpts)
			T0_410 = range(0,numpts)
			R0_410 = range(0,numpts)
			M0_410 = range(0,numpts)
			I0_410 = range(0,numpts)
		if index1 >= 6:
			P0_410[index2] = float(row[0])
			T0_410[index2] = float(row[1])
			R0_410[index2] = float(row[2])
			M0_410[index2] = float(row[3])
			I0_410[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_410),axis=0)
T0 = npy.concatenate((T0,T0_410),axis=0)
R0 = npy.concatenate((R0,R0_410),axis=0)
M0 = npy.concatenate((M0,M0_410),axis=0)
I0 = npy.concatenate((I0,I0_410),axis=0)

P0_dev = npy.concatenate((P0_dev,P0_410),axis=0)
T0_dev = npy.concatenate((T0_dev,T0_410),axis=0)
R0_dev = npy.concatenate((R0_dev,R0_410),axis=0)
M0_dev = npy.concatenate((M0_dev,M0_410),axis=0)
I0_dev = npy.concatenate((I0_dev,I0_410),axis=0)

with open('Data/420K_Rho_Xiong1995_Bl.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_420 = range(0,numpts)
			T0_420 = range(0,numpts)
			R0_420 = range(0,numpts)
			M0_420 = range(0,numpts)
			I0_420 = range(0,numpts)
		if index1 >= 6:
			P0_420[index2] = float(row[0])
			T0_420[index2] = float(row[1])
			R0_420[index2] = float(row[2])
			M0_420[index2] = float(row[3])
			I0_420[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_420),axis=0)
T0 = npy.concatenate((T0,T0_420),axis=0)
R0 = npy.concatenate((R0,R0_420),axis=0)
M0 = npy.concatenate((M0,M0_420),axis=0)
I0 = npy.concatenate((I0,I0_420),axis=0)

with open('Data/430K_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_430 = range(0,numpts)
			T0_430 = range(0,numpts)
			R0_430 = range(0,numpts)
			M0_430 = range(0,numpts)
			B0_430 = range(0,numpts)
			I0_430 = range(0,numpts)
		if index1 >= 6:
			P0_430[index2] = float(row[0])
			T0_430[index2] = float(row[1])
			R0_430[index2] = float(row[2])
			M0_430[index2] = float(row[3])
			B0_430[index2] = float(row[4])
			I0_430[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_430),axis=0)
T0 = npy.concatenate((T0,T0_430),axis=0)
R0 = npy.concatenate((R0,R0_430),axis=0)
M0 = npy.concatenate((M0,M0_430),axis=0)
I0 = npy.concatenate((I0,I0_430),axis=0)

with open('Data/490K_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_490 = range(0,numpts)
			T0_490 = range(0,numpts)
			R0_490 = range(0,numpts)
			M0_490 = range(0,numpts)
			B0_490 = range(0,numpts)
			I0_490 = range(0,numpts)
		if index1 >= 6:
			P0_490[index2] = float(row[0])
			T0_490[index2] = float(row[1])
			R0_490[index2] = float(row[2])
			M0_490[index2] = float(row[3])
			B0_490[index2] = float(row[4])
			I0_490[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_490),axis=0)
T0 = npy.concatenate((T0,T0_490),axis=0)
R0 = npy.concatenate((R0,R0_490),axis=0)
M0 = npy.concatenate((M0,M0_490),axis=0)
I0 = npy.concatenate((I0,I0_490),axis=0)

with open('Data/520K_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_520 = range(0,numpts)
			T0_520 = range(0,numpts)
			R0_520 = range(0,numpts)
			M0_520 = range(0,numpts)
			B0_520 = range(0,numpts)
			I0_520 = range(0,numpts)
		if index1 >= 6:
			P0_520[index2] = float(row[0])
			T0_520[index2] = float(row[1])
			R0_520[index2] = float(row[2])
			M0_520[index2] = float(row[3])
			B0_520[index2] = float(row[4])
			I0_520[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_520),axis=0)
T0 = npy.concatenate((T0,T0_520),axis=0)
R0 = npy.concatenate((R0,R0_520),axis=0)
M0 = npy.concatenate((M0,M0_520),axis=0)
I0 = npy.concatenate((I0,I0_520),axis=0)

with open('Data/660K_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_660 = range(0,numpts)
			T0_660 = range(0,numpts)
			R0_660 = range(0,numpts)
			M0_660 = range(0,numpts)
			B0_660 = range(0,numpts)
			I0_660 = range(0,numpts)
		if index1 >= 6:
			P0_660[index2] = float(row[0])
			T0_660[index2] = float(row[1])
			R0_660[index2] = float(row[2])
			M0_660[index2] = float(row[3])
			B0_660[index2] = float(row[4])
			I0_660[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_660),axis=0)
T0 = npy.concatenate((T0,T0_660),axis=0)
R0 = npy.concatenate((R0,R0_660),axis=0)
M0 = npy.concatenate((M0,M0_660),axis=0)
I0 = npy.concatenate((I0,I0_660),axis=0)

with open('Data/1100K_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_1100 = range(0,numpts)
			T0_1100 = range(0,numpts)
			R0_1100 = range(0,numpts)
			M0_1100 = range(0,numpts)
			B0_1100 = range(0,numpts)
			I0_1100 = range(0,numpts)
		if index1 >= 6:
			P0_1100[index2] = float(row[0])
			T0_1100[index2] = float(row[1])
			R0_1100[index2] = float(row[2])
			M0_1100[index2] = float(row[3])
			B0_1100[index2] = float(row[4])
			I0_1100[index2] = 'isotherm'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_1100),axis=0)
T0 = npy.concatenate((T0,T0_1100),axis=0)
R0 = npy.concatenate((R0,R0_1100),axis=0)
M0 = npy.concatenate((M0,M0_1100),axis=0)
I0 = npy.concatenate((I0,I0_1100),axis=0)

#======================================================
#Isobar PVT Data
#======================================================

with open('Data/0MPa_B_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_0MPa = range(0,numpts)
			T0_0MPa = range(0,numpts)
			BC_0MPa = range(0,numpts)
			W0_0MPa = range(0,numpts)
			M0_0MPa = range(0,numpts)
			I0_0MPa = range(0,numpts)
		if index1 >= 6:
			P0_0MPa[index2] = float(row[0])
			T0_0MPa[index2] = float(row[1])
			BC_0MPa[index2] = float(row[2])
			W0_0MPa[index2] = float(row[3])
			M0_0MPa[index2] = float(row[4])
			I0_0MPa[index2] = 'isobar'
			index2 = index2 + 1
		index1 = index1 + 1

with open('Data/0pt5MPa_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_0pt5MPa = range(0,numpts)
			T0_0pt5MPa = range(0,numpts)
			R0_0pt5MPa = range(0,numpts)
			M0_0pt5MPa = range(0,numpts)
			B0_0pt5MPa = range(0,numpts)
			I0_0pt5MPa = range(0,numpts)
		if index1 >= 6:
			P0_0pt5MPa[index2] = float(row[0])
			T0_0pt5MPa[index2] = float(row[1])
			R0_0pt5MPa[index2] = float(row[2])
			M0_0pt5MPa[index2] = float(row[3])
			B0_0pt5MPa[index2] = float(row[4])
			I0_0pt5MPa[index2] = 'isobar'
			index2 = index2 + 1
		index1 = index1 + 1

with open('Data/1MPa_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_1MPa = range(0,numpts)
			T0_1MPa = range(0,numpts)
			R0_1MPa = range(0,numpts)
			M0_1MPa = range(0,numpts)
			I0_1MPa = range(0,numpts)
		if index1 >= 6:
			P0_1MPa[index2] = float(row[0])
			T0_1MPa[index2] = float(row[1])
			R0_1MPa[index2] = float(row[2])
			M0_1MPa[index2] = float(row[3])
			I0_1MPa[index2] = 'isobar'
			index2 = index2 + 1
		index1 = index1 + 1

with open('Data/6MPa_Rho_Vargaftik1975.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_6MPa = range(0,numpts)
			T0_6MPa = range(0,numpts)
			R0_6MPa = range(0,numpts)
			M0_6MPa = range(0,numpts)
			I0_6MPa = range(0,numpts)
		if index1 >= 6:
			P0_6MPa[index2] = float(row[0])
			T0_6MPa[index2] = float(row[1])
			R0_6MPa[index2] = float(row[2])
			M0_6MPa[index2] = float(row[3])
			I0_6MPa[index2] = 'isobar'
			index2 = index2 + 1
		index1 = index1 + 1

with open('Data/6MPaG_Rho_Vargaftik1975.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_6MPaG = range(0,numpts)
			T0_6MPaG = range(0,numpts)
			R0_6MPaG = range(0,numpts)
			M0_6MPaG = range(0,numpts)
			I0_6MPaG = range(0,numpts)
		if index1 >= 6:
			P0_6MPaG[index2] = float(row[0])
			T0_6MPaG[index2] = float(row[1])
			R0_6MPaG[index2] = float(row[2])
			M0_6MPaG[index2] = float(row[3])
			I0_6MPaG[index2] = 'isobar'
			index2 = index2 + 1
		index1 = index1 + 1

with open('Data/12MPa_Rho_Vargaftik1975.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_12MPa = range(0,numpts)
			T0_12MPa = range(0,numpts)
			R0_12MPa = range(0,numpts)
			M0_12MPa = range(0,numpts)
			I0_12MPa = range(0,numpts)
		if index1 >= 6:
			P0_12MPa[index2] = float(row[0])
			T0_12MPa[index2] = float(row[1])
			R0_12MPa[index2] = float(row[2])
			M0_12MPa[index2] = float(row[3])
			I0_12MPa[index2] = 'isobar'
			index2 = index2 + 1
		index1 = index1 + 1

with open('Data/16MPa_Rho_Vargaftik1975.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_16MPa = range(0,numpts)
			T0_16MPa = range(0,numpts)
			R0_16MPa = range(0,numpts)
			M0_16MPa = range(0,numpts)
			A0_16MPa = range(0,numpts)
			I0_16MPa = range(0,numpts)
		if index1 >= 6:
			P0_16MPa[index2] = float(row[0])
			T0_16MPa[index2] = float(row[1])
			R0_16MPa[index2] = float(row[2])
			M0_16MPa[index2] = float(row[3])
			A0_16MPa[index2] = float(row[4])
			I0_16MPa[index2] = 'isobar'
			index2 = index2 + 1
		index1 = index1 + 1

with open('Data/30MPa_Rho_Vargaftik1975.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_30MPa = range(0,numpts)
			T0_30MPa = range(0,numpts)
			R0_30MPa = range(0,numpts)
			M0_30MPa = range(0,numpts)
			A0_30MPa = range(0,numpts)
			I0_30MPa = range(0,numpts)
		if index1 >= 6:
			P0_30MPa[index2] = float(row[0])
			T0_30MPa[index2] = float(row[1])
			R0_30MPa[index2] = float(row[2])
			M0_30MPa[index2] = float(row[3])
			A0_30MPa[index2] = float(row[4])
			I0_30MPa[index2] = 'isobar'
			index2 = index2 + 1
		index1 = index1 + 1

with open('Data/50MPa_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_50MPa = range(0,numpts)
			T0_50MPa = range(0,numpts)
			R0_50MPa = range(0,numpts)
			M0_50MPa = range(0,numpts)
			A0_50MPa = range(0,numpts)
			CP_50MPa = range(0,numpts)
			S0_50MPa = range(0,numpts)
			I0_50MPa = range(0,numpts)
		if index1 >= 6:
			P0_50MPa[index2] = float(row[0])
			T0_50MPa[index2] = float(row[1])
			R0_50MPa[index2] = float(row[2])
			M0_50MPa[index2] = float(row[3])
			A0_50MPa[index2] = float(row[4])
			CP_50MPa[index2] = float(row[5])
			S0_50MPa[index2] = float(row[6])
			I0_50MPa[index2] = 'isobar'
			index2 = index2 + 1
		index1 = index1 + 1

with open('Data/65MPa_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_65MPa = range(0,numpts)
			T0_65MPa = range(0,numpts)
			R0_65MPa = range(0,numpts)
			M0_65MPa = range(0,numpts)
			A0_65MPa = range(0,numpts)
			CP_65MPa = range(0,numpts)
			S0_65MPa = range(0,numpts)
			I0_65MPa = range(0,numpts)
		if index1 >= 6:
			P0_65MPa[index2] = float(row[0])
			T0_65MPa[index2] = float(row[1])
			R0_65MPa[index2] = float(row[2])
			M0_65MPa[index2] = float(row[3])
			A0_65MPa[index2] = float(row[4])
			CP_65MPa[index2] = float(row[5])
			S0_65MPa[index2] = float(row[6])
			I0_65MPa[index2] = 'isobar'
			index2 = index2 + 1
		index1 = index1 + 1

#======================================================
#Coexistence Data
#======================================================

with open('Data/Coexistence_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_Coex_Angus = range(0,numpts)
			T0_Coex_Angus = range(0,numpts)
			R0_CoeL_Angus = range(0,numpts)
			R0_CoeG_Angus = range(0,numpts)
			M0_Coex_Angus = range(0,numpts)
			H0_Coex_Angus = range(0,numpts)
			S0_Coex_Angus = range(0,numpts)
			I0_Coex_Angus = range(0,numpts)
		if index1 >= 6:
			P0_Coex_Angus[index2] = float(row[0])
			T0_Coex_Angus[index2] = float(row[1])
			R0_CoeL_Angus[index2] = float(row[2])
			R0_CoeG_Angus[index2] = float(row[3])
			M0_Coex_Angus[index2] = float(row[4])
			H0_Coex_Angus[index2] = float(row[5])
			S0_Coex_Angus[index2] = float(row[6])
			I0_Coex_Angus[index2] = 'coexistence'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_Coex_Angus),axis=0)
T0 = npy.concatenate((T0,T0_Coex_Angus),axis=0)
R0 = npy.concatenate((R0,R0_CoeL_Angus),axis=0)
M0 = npy.concatenate((M0,M0_Coex_Angus),axis=0)
I0 = npy.concatenate((I0,I0_Coex_Angus),axis=0)

P0 = npy.concatenate((P0,P0_Coex_Angus),axis=0)
T0 = npy.concatenate((T0,T0_Coex_Angus),axis=0)
R0 = npy.concatenate((R0,R0_CoeG_Angus),axis=0)
M0 = npy.concatenate((M0,M0_Coex_Angus),axis=0)
I0 = npy.concatenate((I0,I0_Coex_Angus),axis=0)

with open('Data/Coexistence_Duschek1990.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_Coex_Duschek = range(0,numpts)
			T0_Coex_Duschek = range(0,numpts)
			R0_CoeL_Duschek = range(0,numpts)
			R0_CoeG_Duschek = range(0,numpts)
			M0_Coex_Duschek = range(0,numpts)
			I0_Coex_Duschek = range(0,numpts)
		if index1 >= 6:
			P0_Coex_Duschek[index2] = float(row[0])
			T0_Coex_Duschek[index2] = float(row[1])
			R0_CoeL_Duschek[index2] = float(row[2])
			R0_CoeG_Duschek[index2] = float(row[3])
			M0_Coex_Duschek[index2] = float(row[4])
			I0_Coex_Duschek[index2] = 'coexistence'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_Coex_Duschek),axis=0)
T0 = npy.concatenate((T0,T0_Coex_Duschek),axis=0)
R0 = npy.concatenate((R0,R0_CoeL_Duschek),axis=0)
M0 = npy.concatenate((M0,M0_Coex_Duschek),axis=0)
I0 = npy.concatenate((I0,I0_Coex_Duschek),axis=0)

P0 = npy.concatenate((P0,P0_Coex_Duschek),axis=0)
T0 = npy.concatenate((T0,T0_Coex_Duschek),axis=0)
R0 = npy.concatenate((R0,R0_CoeG_Duschek),axis=0)
M0 = npy.concatenate((M0,M0_Coex_Duschek),axis=0)
I0 = npy.concatenate((I0,I0_Coex_Duschek),axis=0)

with open('Data/Coexistence_Newitt1947.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_Coex_Newitt = range(0,numpts)
			T0_Coex_Newitt = range(0,numpts)
			R0_CoeL_Newitt = range(0,numpts)
			R0_CoeG_Newitt = range(0,numpts)
			M0_Coex_Newitt = range(0,numpts)
			H0_Coex_Newitt = range(0,numpts)
			S0_Coex_Newitt = range(0,numpts)
			I0_Coex_Newitt = range(0,numpts)
		if index1 >= 6:
			P0_Coex_Newitt[index2] = float(row[0])
			T0_Coex_Newitt[index2] = float(row[1])
			R0_CoeL_Newitt[index2] = float(row[2])
			R0_CoeG_Newitt[index2] = float(row[3])
			M0_Coex_Newitt[index2] = float(row[4])
			H0_Coex_Newitt[index2] = float(row[5])
			S0_Coex_Newitt[index2] = float(row[6])
			I0_Coex_Newitt[index2] = 'coexistence'
			index2 = index2 + 1
		index1 = index1 + 1
P0 = npy.concatenate((P0,P0_Coex_Newitt),axis=0)
T0 = npy.concatenate((T0,T0_Coex_Newitt),axis=0)
R0 = npy.concatenate((R0,R0_CoeL_Newitt),axis=0)
M0 = npy.concatenate((M0,M0_Coex_Newitt),axis=0)
I0 = npy.concatenate((I0,I0_Coex_Newitt),axis=0)

P0 = npy.concatenate((P0,P0_Coex_Newitt),axis=0)
T0 = npy.concatenate((T0,T0_Coex_Newitt),axis=0)
R0 = npy.concatenate((R0,R0_CoeG_Newitt),axis=0)
M0 = npy.concatenate((M0,M0_Coex_Newitt),axis=0)
I0 = npy.concatenate((I0,I0_Coex_Newitt),axis=0)

#======================================================
#Response Function Data
#======================================================

with open('Data/CV1_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_CV1 = range(0,numpts)
			T0_CV1 = range(0,numpts)
			R0_CV1 = range(0,numpts)
			M0_CV1 = range(0,numpts)
			CV_CV1 = range(0,numpts)
			I0_CV1 = range(0,numpts)
		if index1 >= 6:
			P0_CV1[index2] = float(row[0])
			T0_CV1[index2] = float(row[1])
			R0_CV1[index2] = float(row[2])
			M0_CV1[index2] = float(row[3])
			CV_CV1[index2] = float(row[4])
			I0_CV1[index2] = 'response'
			index2 = index2 + 1
		index1 = index1 + 1

with open('Data/CV2_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_CV2 = range(0,numpts)
			T0_CV2 = range(0,numpts)
			R0_CV2 = range(0,numpts)
			M0_CV2 = range(0,numpts)
			CV_CV2 = range(0,numpts)
			I0_CV2 = range(0,numpts)
		if index1 >= 6:
			P0_CV2[index2] = float(row[0])
			T0_CV2[index2] = float(row[1])
			R0_CV2[index2] = float(row[2])
			M0_CV2[index2] = float(row[3])
			CV_CV2[index2] = float(row[4])
			I0_CV2[index2] = 'response'
			index2 = index2 + 1
		index1 = index1 + 1

with open('Data/CV3_Rho_Angus1976.csv','rb') as csvfile:
	datareader = csv.reader(csvfile)
	#x0 = (float(column[1]) for column in datareader)
	index1 = 0
	index2 = 0
	for row in datareader:
		if index1 == 4:
			numpts = int(row[0])
			P0_CV3 = range(0,numpts)
			T0_CV3 = range(0,numpts)
			R0_CV3 = range(0,numpts)
			M0_CV3 = range(0,numpts)
			CV_CV3 = range(0,numpts)
			I0_CV3 = range(0,numpts)
		if index1 >= 6:
			P0_CV3[index2] = float(row[0])
			T0_CV3[index2] = float(row[1])
			R0_CV3[index2] = float(row[2])
			M0_CV3[index2] = float(row[3])
			CV_CV3[index2] = float(row[4])
			I0_CV3[index2] = 'response'
			index2 = index2 + 1
		index1 = index1 + 1

#Ncoex = 0
#Nsp = 0
#for i in range(0,len(P0)):
#	if I0[i] == 'coexistence':
#		Ncoex = Ncoex+1
#	elif I0[i] == 'isotherm':
#		Nsp = Nsp+1
#total = Ncoex+Nsp
#print('len(P0) = {}, Ncoex = {}, Nsp = {}, sum = {}.'.format(len(P0),Ncoex,Nsp,total))