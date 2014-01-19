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
#import sys #uncomment for debug
####Define the Variables For Fun
num_1 = 0
opp_var="++"
num_2 = 0
raw_input = "?" #Used to store values until they are verified

####Print Manual on Screen for user
print()
print("Welcome to PyCalc (Python Calculator)")
print("PyCalc Supports the Following Operations")
print("-----------------------------------------")
print("Addition      (+)    Divide          (//)")
print("Add One      (++)    Remainder        (%)")
print("Subtract      (-)    Multiply         (*)")
print("Divide (Float)(/)    Exponent         (^)")
print("-----------------------------------------")
print("Type any Letter in 'First Number' to exit")
print("-----------------------------------------")
print("")
#######################################################################
####Loop
try: #Necessary for error message
	while True: #Allows program to repeat
		
####Get inputs from user
#What is First Number?
		raw_input=input("First Number ("+str(num_1)+"): ")
		#Test if Letter (Only First Character, Convert to upper-case)
		if raw_input == "": raw_input = str(num_1)
		if (ord(raw_input[0:1].upper()) >= 65 
				and ord(raw_input[0:1].upper()) <= 90): 
			break #Exit While Loop
		num_1=float(raw_input)
		
#What is Operator? (Automatically Convert to Upper Case if Not Already)
		raw_input=input("Operator ("+str(opp_var)+"): ").lower()
		if not raw_input == "": opp_var = raw_input #This allows reusing values

#What is Second Number?
		if not opp_var == "++": #No need if it is ++
			raw_input=input("Second Number ("+str(num_2)+"): ")
			if not raw_input == "": num_2 = float(raw_input) #This allows reusing values
		else:
			num_2=1 #"Clear" the Variable
#Print The Opperation to be Performed	
		print(str(num_1)+" "+str(opp_var)+" "+str(num_2)+"=")
		print("")
####If Statement of different Possible Operators
	#Addition                         Valid Values (+, plus, add)
		if any([opp_var == "+", opp_var == "plus", opp_var == "add"]):
			num_1=(num_1 + num_2)
			print(num_1)
	#Add One                          Valid Values (++)
		elif opp_var == "++":
			num_1=(num_1 + 1)
			print(num_1)
	#Subtraction                      Valid Values (-, minus, subtract)
		elif any([opp_var == "-", opp_var == "minus", opp_var == "subtract"]):
			num_1=(num_1 - num_2)
			print(num_1)
	#Divide into a float              Valid Values (/, \, divide)
		elif any([opp_var == "/", opp_var == "\\", opp_var == "Divide"]):
			if num_2==0: 
				print("Divide by Zero, I ain't falling for that")
				print("")
				num_2=3.14159265359
				print(str(num_1)+" "+str(opp_var)+" "+str(num_2)+"=")
			num_1=(num_1 / num_2)
			print(num_1)
	#Divide into integer              Valid Values (//, \\)
		elif any([opp_var == "//", opp_var == "\\\\"]):
			if num_2==0: 
				print("Divide by Zero, I ain't falling for that")
				print("")
				num_2=2.71828182846
				print(str(num_1)+" "+str(opp_var)+" "+str(num_2)+"=")
			num_1=(num_1 // num_2)
			print(num_1)
	#Multiply                         Valid Values (x, *, times, multiply)
		elif any([opp_var == "*", opp_var == "x", opp_var == "times", opp_var == "multiply"]):
			num_1=(num_1 * num_2)
			print(num_1)
	#Exponent                         Valid Values (^, **)
		elif any([opp_var == "^", opp_var == "**"]):
			if num_1==0 and num_2<0: 
				print("0 to the power of a negative number, No way")
				print("")
				num_2=1.41421356237
				print(str(num_1)+" "+str(opp_var)+" "+str(num_2)+"=")
			num_1=(num_1 ** num_2)
			print(num_1)
	#Remainder                        Valid Values (r, %)
		elif any([opp_var == "r", opp_var == "%"]):
			if num_2==0: 
				print("Divide by Zero, I ain't falling for that")
				print("")
				num_2=299792458
				print(str(num_1)+" "+str(opp_var)+" "+str(num_2)+"=")
			num_1=(num_1 % num_2)
			print(num_1)
	#Something Else? Explain Mistake
		else:
			print("That was not the Operator you were looking for")
		print("")
		print("Type any Letter in 'First Number' to exit")
		print("-----------------------------------------")
		print("")
####End Loop
#######################################################################

####Error Handler
except:
	print("Well, this is embarrassing, PyCalc had an error. One of us messed up.")
	#print(sys.exc_info()) #to use this import sys
else:
	print("")
	print("Goodbye, Thanks for using PyCalc")
