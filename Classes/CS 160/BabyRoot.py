####################################################################### 
# Program Filename: BabyRoot.py
# Author: Cody Ray Freeman Hoeft
# Date: October 28, 2013
# Description: This program takes a users input and runs through the 
#              Babylonian method of approximating the square root:
#              1. Make a guess at the answer. 
#              2. Compute r = number / guess 
#              3. Set guess = (guess + r) / 2 
#              4. Go back to step 2 for as many iterations as necessary. 
#                 The more steps 2 and 3 are repeated, the closer guess  
#			      will become to the square root of n.
#			   Source of Above Algorithm: Assignment 3, CS 160,  
#              Oregon State University, Jennifer Parham-Mocello 
# Input: A real positive number
# Output: Approximation Based on the Babylonian Algorithm
#######################################################################

#Variables
raw = "foo" #Temp storage variable
sqnum = 4 #Number that we will find the square root of
rootguess = sqnum/2 #Variable that we will use to store the current 'guess'
loopnum = 100 #Number of times the loop will run, higher numbers increase accuracy
strverb = "Intermediate Steps"+chr(10) #Mostly for debug this feature will collect a 'log' of the itterations
printverb = "N" #Turns on 'Print Verbose
repeatprogram = "Y" #Variable controlling while loop
#progressbar = "Y" #Probably will not turn into real feature

#Manual
print()
print("Welcome to BabyRoot (Babylonian Root Calculator)  ")
# print("BabyRoot Will find the Square Root of numbers for you")
# print("-----------------------------------------------------")
# print("   New Guess = (Guess+(Number/Guess))/2); Repeated")
# print("   until an accurate result is achieved. Google:") 
# print("   'Babylonian Algorithm' for more information.")
# print("-----------------------------------------------------")
# print("          See Advanced Options to:")
# print("          1. Set your own Start Guess")
# print("          2. Set the number of Iterations")
# print("          3. Show Intermediate Steps")
# print("-----------------------------------------------------")
# print("")
#######################################################################
####Start of While Loop
while(repeatprogram == "Y"):
	strverb = "Intermediate Steps"+chr(10)+chr(10) #Reset if user runs again
	print()
	#Input
	raw = input("What number would you like to find the square root of? ("+str(sqnum)+"): ")
	if raw != "": sqnum = float(raw)
	if sqnum < 0: sqnum = -sqnum
	##Advanced Setting
	if input("Would you like to change Advanced Setting?(N): ")[0:1].upper() == "Y":
		
		###User's Guess
		rootguess = input("What is your initial guess for the square root? ("+str(sqnum/2)+"): ")
		if rootguess == "": 
			rootguess = float(sqnum/2)
		else:
			rootguess = float(rootguess)
			if rootguess < 0: rootguess = -rootguess
		###User's Iterations
		raw = input("How many iterations? ("+str(loopnum)+"): ")
		if raw != "": loopnum = int(raw)
		
		###Show Intermediate Steps
		raw = input("Would you like to show intermediate steps? ("+str(printverb)+"): ")
		if raw != "": printverb = raw[0:1].upper()
	
	else:
		rootguess = float(sqnum/2)
	
	print("")
	
	#Processing
	if(not(rootguess==0 or sqnum==0)):
		for i in range(loopnum):
			strverb = strverb+str(i)+": "+str(rootguess)+chr(10)
			rootguess = (rootguess +(sqnum/rootguess))/2
	elif(sqnum==0):
		rootguess = 0
	elif(rootguess==0):
		rootguess = float(sqnum/2)
		print("Your Guess was incorrect, changed to default " + str(rootguess))
		for i in range(loopnum):
			strverb = strverb+str(i)+": "+str(rootguess)+chr(10)
			rootguess = (rootguess +(sqnum/rootguess))/2
	#Output
	if printverb == "Y": print(strverb)
	
	print("The Square Root of "+str(sqnum)+" is approximately")
	print(str(rootguess))
	
	#Ask to Repeat
	if input("Do you you want to restart?(Y): ")[0:1].upper() == "N": repeatprogram = "N"
####End While Loop
#######################################################################
print("Thanks for using BabyCalc")
