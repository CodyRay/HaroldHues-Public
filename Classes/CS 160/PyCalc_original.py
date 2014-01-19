####################################################################### 
# Program Filename: PyCalc.py
# Author: Cody Ray Freeman Hoeft
# Date: October 21, 2013
# Description: PyCalc is a powerful calculator that allows operations  
#      to be performed on the command line. Options Include: +, ++, -, 
#      /, //, *, **, and %.
# Input: Two Numbers and an operator
# Output: Resulting Calculation
####################################################################### 
import sys
####Define the Variables For Fun
Num_1 = 0
Opp="++"
Num_2 = 0
raw = "?" #Used to store values until they are verified

####Print Manual on Screen for user
#Welcome to PyCalc (Python Calculator)
#PyCalc Supports the Following Operations
#-----------------------------------------
#Addition      (+)    Divide          (//)
#Add One      (++)    Remainder (Mod)  (%)
#Subtract      (-)    Multiply         (*)
#Divide (Float)(/)    Exponent         (^)
#
#Press a Letter at any time to exit
print()
print("Welcome to PyCalc (Python Calculator)")
print("PyCalc Supports the Following Operations")
print("-----------------------------------------")
print("Addition      (+)    Divide          (//)")
print("Add One      (++)    Remainder        (%)")
print("Subtract      (-)    Multiply         (*)")
print("Divide (Float)(/)    Exponent         (^)")
print("-----------------------------------------")
print("Press a Letter at any time to exit")
print()
#######################################################################
####Loop
try:
	while True:
		
####Get inputs from user
#What is First Number?
		raw=input("First Number ("+str(Num_1)+"): ")
		#Test if Letter (Only First Character, Convert to upper-case)
		if raw == "": raw = str(Num_1)
		if (ord(raw[0:1].upper()) >= 65 and   
				ord(raw[0:1].upper()) <= 90): 
			break #Exit While Loop
		Num_1=float(raw)
		
#What is Operator? (Automatically Convert to Upper Case if Not Already)
		raw=input("Operator ("+str(Opp)+"): ")
		#Test if Letter (Only First Character, Convert to upper-case)
		if raw == "": raw = str(Opp)
		if (not any([
				raw[0:1].upper() == "P",
				raw[0:1].upper() == "A",
				raw[0:1].upper() == "M",
				raw[0:1].upper() == "R",
				raw[0:1].upper() == "S",
				raw[0:1].upper() == "D",
				raw[0:1].upper() == "T"]) and
				(ord(raw[0:1].upper()) >= 65 and 
				ord(raw[0:1].upper()) <= 90)): 
			break #Exit While Loop
		Opp=raw.lower()

#What is Second Number?
		if not Opp == "++":
			raw=input("Second Number ("+str(Num_2)+"): ")
			#Test if Letter (Only First Character, Convert to upper-case)
			if raw == "": raw = str(Num_2)
			if (ord(raw[0:1].upper()) >= 65 and   
					ord(raw[0:1].upper()) <= 90): 
				break #Exit While Loop
			Num_2=float(raw)
		else:
			Num_2="" #"Clear" the Variable
			
		print(str(Num_1)+" "+str(Opp)+" "+str(Num_2)+"=") #For Debug
	####If Statement of different Possible Operators
	#Addition                         Valid Values (+, plus, add)
		if any([Opp == "+", Opp == "plus", Opp == "add"]):
			Num_1=(Num_1 + Num_2)
			print(Num_1)
	#Add One                          Valid Values (++)
		elif Opp == "++":
			Num_1=(Num_1 + 1)
			print(Num_1)
	#Subtraction                      Valid Values (-, minus, subtract)
		elif any([Opp == "-", Opp == "minus", Opp == "subtract"]):
			Num_1=(Num_1 - Num_2)
			print(Num_1)
	#Divide into a float              Valid Values (/, \, divide)
		elif any([Opp == "/", Opp == "\\", Opp == "Divide"]):
			if Num_2==0: 
				print("Divide by Zero, I ain't falling for that")
				Num_2=3.14159265359
				print(str(Num_1)+" "+str(Opp)+" "+str(Num_2)+"=")
			Num_1=(Num_1 / Num_2)
			print(Num_1)
	#Divide into integer              Valid Values (//, \\)
		elif any([Opp == "//", Opp == "\\\\"]):
			if Num_2==0: 
				print("Divide by Zero, I ain't falling for that")
				Num_2=2.71828182846
				print(str(Num_1)+" "+str(Opp)+" "+str(Num_2)+"=")
			Num_1=(Num_1 // Num_2)
			print(Num_1)
	#Multiply                         Valid Values (x, *, times, multiply)
		elif any([Opp == "*", Opp == "x", Opp == "times", Opp == "multiply"]):
			Num_1=(Num_1 * Num_2)
			print(Num_1)
	#Exponent                         Valid Values (^, **)
		elif any([Opp == "^", Opp == "**"]):
			Num_1=(Num_1 ** Num_2)
			print(Num_1)
	#Remainder                        Valid Values (r, %)
		elif any([Opp == "r", Opp == "%"]):
			Num_1=(Num_1 % Num_2)
			print(Num_1)
	#Any Letter for Exit (Above Excluded)
		elif (ord(raw[0:1].upper()) >= 65 and   
				ord(raw[0:1].upper()) <= 90): 
			break
	#Something Else? Explain Mistake
		else:
			print("That was not the Operator you were looking for")
####Print Answer

####End Loop
#######################################################################

####Error Handler
except:
	print("Well, this is embarrassing, PyCalc had an error. One of us messed up.")
	#print(sys.exc_info())
else:
	print("Goodbye, Thanks for using PyCalc")
