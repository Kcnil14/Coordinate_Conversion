#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv 
import re
from os import path

#Global Variables 
degree_sign = u"\N{DEGREE SIGN}"


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


def dms2dd(latlon):

    for letter in re.finditer(degree_sign, latlon):

        start_posit = latlon[letter.start()]
            
        if start_posit != 'N' or start_posit !='E' or start_posit !='W' or start_posit !='S':
                deg = (latlon[letter.start()-2:letter.end()])
        elif start_posit == 'N' or start_posit =='E' or start_posit =='W' or start_posit =='S':
                deg = latlon[letter.start()-3:letter.end()]
        else:
                print("Error in parsing degrees.")

        rmvDegSgn = deg.replace(degree_sign," ")
        D = rmvDegSgn.strip()
        print(D)
