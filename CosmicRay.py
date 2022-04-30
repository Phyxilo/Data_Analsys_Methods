#!/usr/bin/python

import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

Data = open(r"Data.txt", "r")

eventNum = []
intervalNum = []
expectedArray = []
DOF = 0

count = 0

for line in Data:	#Adds data from the Data.txt into "eventNum" and "intervalNum" arrays

    splittedLine = line.split()

    eventNum.append(int(splittedLine[0]))
    intervalNum.append(int(splittedLine[1]))
	
    count = count + 1
Data.close()

def drawGraph(x, y, expct):	#Function that draws measured points
	
	plt.plot(x, expct, "r")
	plt.bar(x, y, 1)

	plt.xlabel("Number of Events")
	plt.ylabel("Number of Intervals")

	plt.show()

def factorial(Num):	#Function that calculates factorial
	
	fact = 1

	for i in range(1, Num + 1):
		fact = fact * i

	return (fact)

def Lambda(event, inter):	#Function that calculates Lambda and total events

	count1 = 0
	count2 = 0
	Sum = 0	
	lmbd = 0
	
	for len in event:
		
		Sum = Sum + inter[count1]

		count1 = count1 + 1

	for len in event:

		lmbd = lmbd + (event[count2] * inter[count2])/Sum 
		
		count2 = count2 + 1


	return(lmbd, Sum)


def findExpct(event, lmbd, total):	#Function that find expected values for Poisson's Distribution

	Output = []
	count = 0

	for len in event:

		x = event[count]

		Output.append((total * math.exp(-lmbd) * pow(lmbd, event[count]))/(factorial(event[count])))
		
		count = count + 1
	
	return(Output)

expectedArray = findExpct(eventNum, Lambda(eventNum, intervalNum)[0], Lambda(eventNum, intervalNum)[1])

def chiSquare(event):	#Function that calculates Chi Square
	
	chi = []
	count = 0
	Sum = 0	
	
	for len in event:
	
		chi.append(((expectedArray[count] - event[count])**2)/(event[count]))
		Sum = Sum + chi[count]
		count = count + 1

	return(Sum)

DOF = len(eventNum) - 1	#Equation that find Degrees of Freedom. Only Lambda value calculated so we have only one -1

print("Expected Array : " , expectedArray)
print("Chi-Square : " , chiSquare(intervalNum))
print("Chi-Square / Degrees of Freedom : " , chiSquare(intervalNum) / DOF)
print("From the Table for Chi-Square: ", chiSquare(intervalNum), " and for DOF: ", DOF, " values probability is 70%, so this process is poisson ")

drawGraph(eventNum, intervalNum, expectedArray)
