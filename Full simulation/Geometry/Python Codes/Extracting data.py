# -*- coding: utf-8 -*-
"""
Extracting Information from OPERA file 
"""
import numpy as np
import xlwt
from xlwt import Workbook

f = open('datafile.txt','r')
wb = Workbook()
sheet1 = wb.add_sheet('Magnets')

sheet1.write(0, 0, 'Name') 
sheet1.write(0, 1, 'Coordinates of local coordinate system') 
sheet1.write(0, 2, 'Coordinates of local coordinate system') 
sheet1.write(0, 3, 'Coordinates of local coordinate system') 
sheet1.write(0, 4, 'Coordinates of local coordinate system') 
sheet1.write(0, 5, 'Coordinates of local coordinate system') 
sheet1.write(0, 6, 'Coordinates of local coordinate system') 
sheet1.write(0, 7, 'Coordinates of object in local coordinate system') 
sheet1.write(0, 8, 'Coordinates of object in local coordinate system') 
sheet1.write(0, 9, 'Coordinates of object in local coordinate system') 
sheet1.write(0, 10, 'Coordinates of object in local coordinate system') 
sheet1.write(0, 11, 'Coordinates of object in local coordinate system') 
sheet1.write(0, 12, 'Coordinates of object in local coordinate system') 
sheet1.write(0, 13, 'Length') 
sheet1.write(0, 14, 'Thickness') 

sheet1.write(1, 0, '') 
sheet1.write(1, 1, 'X') 
sheet1.write(1, 2, 'Y') 
sheet1.write(1, 3, 'Z') 
sheet1.write(1, 4, 'Theta') 
sheet1.write(1, 5, 'Phi') 
sheet1.write(1, 6, 'Psi') 
sheet1.write(1, 7, 'X') 
sheet1.write(1, 8, 'Y') 
sheet1.write(1, 9, 'Z') 
sheet1.write(1, 10, 'Theta') 
sheet1.write(1, 11, 'Phi') 
sheet1.write(1, 12, 'Psi')  
sheet1.write(1, 13, '') 
sheet1.write(1, 14, '') 


f1 = f.readlines()
i=0
j=2
for x in f1:
    if ( np.mod(i,10)==1 ):
        X,Y,Z,Theta,Phi,Psi = x.split()
        
    if ( np.mod(i,10)==2 ):
        X2,Y2,Z2= x.split()
        
    if ( np.mod(i,10)==3):
       Theta2,Phi2,Psi2= x.split()
      
    if(np.mod(i,10)==7):
        name = x.split()[2]
        
    if(np.mod(i,10)==4):
        dim = x.split()
        length = float(dim[3]) - float(dim[1])
        R1 = float(dim[0])
        
    if(np.mod(i,10)==5):
        dim = x.split()
        R2 = float(dim[0])
        radius = R2 - R1
        
    i+=1 
    if(np.mod(i,10)==0 and i != 0):
      
        sheet1.write(j, 0, name) 
        #sheet1.write(j, 1, 'X={}, Y={}, Z={}, Theta={}, Phi={}, Psi={}'.format(X,Y,Z,Theta,Phi,Psi)) 
        #sheet1.write(j, 2, 'X={},  Y={},  Z={},  Theta={},  Phi={}, Psi={}'.format(X2,Y2,Z2,Theta2, Phi2, Psi2)) 
        #sheet1.write(j, 3, '%3.2f'%length) 
        #sheet1.write(j, 4,  '%3.2f '%(radius)) 
        sheet1.write(j, 1, float(X))
        sheet1.write(j, 2, float(Y) )
        sheet1.write(j, 3, float(Z ))
        sheet1.write(j, 4, float(Theta)) 
        sheet1.write(j, 5, float(Phi) )
        sheet1.write(j, 6, float(Psi) )
        sheet1.write(j, 7, float(X2) )
        sheet1.write(j, 8, float(Y2) )
        sheet1.write(j, 9, float(Z2) )
        sheet1.write(j, 10, float(Theta2)) 
        sheet1.write(j, 11, float(Phi2) )
        sheet1.write(j, 12, float(Psi2))  
        sheet1.write(j, 13, float('%3.2f'%length) )
        sheet1.write(j, 14,  float('%3.2f '%(radius)) )
        j+=1
    

wb.save('magnets.xls')