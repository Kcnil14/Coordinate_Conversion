#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv 
import re
from os import path

#Global Variables 
degree_sign = u"\N{DEGREE SIGN}"
min_sign = u"\u0027"




def response():

    #Providing acceptable responses for user input. 
    choices = ("DMS","DD")

    #Gathering user input.
    #While loop used to reiterate if incorrect values are given.'''
    while True:
        uInput = input("Are you converting from DMS or DD?")
        conversion = uInput.upper()

        #loops back to beginning of while loop
        if conversion not in choices:
            print("Choose either DMS or DD.")
        else:
            break

    #if the user input is DMS if not then DD is handled in else statement
    if conversion == choices[0]:
        print("You've selected DMS")
    else:
        print("You've selected DD")

    
def addUTF():
    try: 
        fileNameRes = input("Enter file name.")
        filePathRes = input("Enter file path.")
        fullPath = filePathRes + "\\" + fileNameRes

        myFile = open(fullPath, "r", encoding = "utf-8")

        coords = myFile.read()

        dms2dd(coords)
        
        myFile.close()
            
            
    except:
        pass

    
def findDeg(latlon):

    degList = []

    for myLatLons in latlon.splitlines():
        for dms in myLatLons.split():
            
            degreeLoc = dms.find(degree_sign)

            if "-" in dms[:degreeLoc]:
                negPosit = dms.find("-")
                myCoord = dms[negPosit+1:degreeLoc]
                
            else:
                myCoord = dms[0:degreeLoc]

            degList.append(myCoord)

            
        ''' thought this might be a solution, but couldn't consitently
        get it to work
        if start_posit != 'N' or start_posit !='E' or start_posit !='W' or start_posit !='S':
                deg = (latlon[degree.start()-2:degree.end()])
        elif start_posit == 'N' or start_posit =='E' or start_posit =='W' or start_posit =='S' or start_posit=='-':
                deg = latlon[degree.start()-3:degree.end()]
        else:
                print("Error in parsing degrees.")

        rmvDegSgn = deg.replace(degree_sign," ")
        D = rmvDegSgn.strip()

        degList.append(D)
        
    print(degList)'''

def findMin(latlon):

    minSymbol = "'"

    minList = []

    for mins in re.finditer(minSymbol,latlon):
        start_posit = latlon[mins.start()+2]
        print(start_posit)




def dms2dd(latlon):
    c1 = 0
    c2 = 0 

    findDeg(latlon)

    findMin(latlon)

    while c1 < len(degList):
        print(degList[c1])
        c1+=1
        while c2 <len(degList):
            print(degList[c2])
            c2+=1

    

    

        

    
        
