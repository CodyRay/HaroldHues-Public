####################################################################### 
# Program Filename:  GradeCalcualator.py
# Author: Cody Ray Hoeft
# Date: November 2013
# Description: Program is designed to calculate a user’s grade in a class
# Input: User data
# Output: A percentage grade and positive/negative feedback
#######################################################################

#######################################################################
# Function: printmanual()
# Description: Prints the Manual for the program
# Parameters: None
# Pre-Conditions: None
# Post-Conditions: None
#######################################################################
def printmanual():
	print("This utility will help you calculate your grades in a class.")
	print("Grades are calculated by the following formula")
	print("  Average score of assignments X Weight of assignments")
	print("+       Average score of tests X Weight of tests")
	print("+        Average score of labs X Weight of labs")
	print("+     Average score of quizzes X Weight of quizzes")
	print("+      Score of weighted final X Weight of final")
	print("-----------------------------------------------------")
	print("                    Grade in Class")
	print()
	print("   This is the general process for using this program")
	print("1. Enter the Number of assignments for each of the preset")
	print("   categories test, assignments, quizzes, and labs (0 OK)")
	print("2. Enter the scores for each assignment as prompted")
	print("3. If you have a set of tests that are weighted outside")
	print("   of the assignments you have already entered you can")
	print("   enter it now")
	print("4. Program will print your grade, and ask you if you have")
	print("   another grade to calculate.")

#######################################################################
# Function: get_initial_input(title, counts, weight)
# Description: Asks user about how many assignments per category and the weight of each category
# Parameters: title is a list of titles for each count, count is the count of assignments in each category, weight is a preset array that will be changed
# Pre-Conditions: title, counts, and weight must have same length
# Post-Conditions: Values in weight have changed
#######################################################################
def get_initial_input(title, counts, weight):
	#for each category
	for cat in range(len(title)):	
		#Ask the user how many assignments they have
		#Store the response in counts
		counts[cat] = inputposint("How many "+title[cat]+" do you have?", "0")
#################There is no reason to ask this if they enter 0 for count, and it should be set to 0
		if counts[cat] == 0:
			weight[cat] = 0
		else:
			#Ask the user the weight of category
			#Store the response in weight
			weight[cat] = inputpercentage("What is the weight of "+title[cat]+" as a percentage?", "25")
		print()

#######################################################################
# Function: get_scores(title, counts, average)
# Description: Asks user thier scores on all assignments in each category
# Parameters: title is a list of titles for each count, count is the count of assignments in each category, average is a preset array that will be changed
# Pre-Conditions: title, counts, and average must be same length
# Post-Conditions: Values in average have changed
# Variables: cur_points - current points for assignment
#            cur_prec - current percentage for assignment
#	     recieved_points - rolling total of points recieved
#	     possible_points - rolling total op points possible
#######################################################################
def get_scores(title, counts, average):
	#for each count in counts
	for cat in range(len(title)):
		#set possible_points and recieved_points equal to 0
		possible_points = 0
		recieved_points = 0
		for assign in range(counts[cat]):
		#for each assignment (based on numbers in counts)
			if assign == 0:
				print(title[cat].upper())
				print("----------------------------------------------------------------")
			#Get points possible for this assignment
			cur_points = inputposint("How many points were possible for #"+str(assign +1)+" in category "+title[cat]+"?", "20")
			#Store as cur_points
			#Get users percentage for assignment
			cur_prec = inputpercentage("What percent of the points for #"+str(assign + 1)+" in category "+title[cat]+" did you recieve?", "100")
			print()
			#Store as cur_prec
			#Add cur_points to possible_points
			possible_points+=cur_points
			#Add cur_points*cur_prec to recieved_points
			recieved_points+=cur_points*cur_prec
		#divide recieved_points by possible_points
#################Changed to prevent devide by zero for categories with no assignments
		if possible_points != 0: average[cat] = recieved_points/possible_points
		#store in average

#######################################################################
# Function: get_special_assignment(title, counts, average, weight, weighted_average)
# Description: Asks user thier scores on all assignments in each category
# Parameters: title is a list of titles to be appended, count is the count of assignments to be appended, average is a preset array that will be appended with the score of the special assignment, weight is the weight appended to a list, weighted_average is an array that will be appended with a 0 to insure all arrays are the same length
# Pre-Conditions: title, counts, average, and weighted_average must be same length
# Post-Conditions: A new category with a count of one, user imput for score, and an appended weighted_average list
# Variables: wants_input - Variable for while loop
#            prec - percentage for assignment
#	     recieved_points - rolling total of points recieved
#	     possible_points - rolling total op points possible
#######################################################################
def get_special_assignment(title, counts, average, weight, weighted_average):
	#yonq("Do you have any Special Assignments?", "Yes")
	#Store as a variable for while loop
	wants_input = yonq("Do you have any Special Assignments like a Weighted Final?", "Yes")
	#While loop to support multiple special assignments
	while(wants_input):
		#Append and prompt for the appropreate input
		title.append("Special")
		counts.append(1)
		average.append(inputpercentage("What was your score for this Assignment/Test? (percentage)", "100"))
		weight.append(inputpercentage("What is the weight of this Assignment/Test? (percentage)", "20"))
		weighted_average.append(0)
		print()
		wants_input = yonq("Do you have another Special Assignments?", "No")
		
#######################################################################
# Function: calculate_weighted_avg(title, weight, average, weighted_average)
# Description: Calculates the weighted average for each category
# Parameters: title is a list of titles for each count, count is the count of assignments in each category, average is the average score for each category, weighted_average is the value to be changed
# Pre-Conditions: All lists must be the same length
# Post-Conditions: weighted_average values have been calculated
#######################################################################
def calculate_weighted_avg(title, weight, average, weighted_average):
#for each category
	for cat in range(len(title)):
		#multiply weight times average
		weighted_average[cat] = weight[cat] * average[cat]
		#store as weighted_average

#######################################################################
# Function: calculate_class_grade(category_weighted_average)
# Description: sums the weighted averages to get a class grade
# Parameters: category_weighted_average is the list of the values to be sumed
# Pre-Conditions: category_weighted_average is a valid list
# Post-Conditions: None
# Return: Class grade (sum)
# Variables: current_sum
#######################################################################
def calculate_class_grade(weighted_average):
	#set current_sum equal to 0
	current_sum = 0
	#for each category
	for average in weighted_average:
		#Added weighted average to current_sum
		current_sum += average 
	#multiply current_sum by 100 so it looks like a percent 
	current_sum*=100
	return current_sum

#######################################################################
# Function: yonq(prompt, default)
# Description: Asks the user a  Y es  O r  N o  Q uestion and converts the answer to a boolean
# Parameters: prompt is the text that will prompt the user, default is the value that will be used if user presses enter
# Pre-Conditions: both parameters are strings
# Post-Conditions: None
# Returns: Boolean
# Variables: raw - temporary storage space for input 
#######################################################################
def yonq(prompt, default):
	while(True): 
		#Ask the user for input in format (prompt+” [“+default+”]: “)
		raw = input(prompt+" ["+default+"]: ")
		#Store as raw
		#if raw is “” set raw = to default
		if raw == "" : raw=default
		#if raw’s first letter (capitalized) is Y
		if raw[0:1].upper() == 'Y':
			#return true
			return True
		#elif raw’s first letter (capitalized) is N
		elif raw[0:1].upper() == 'N':
			#return false
			return False
		else:
			#print error message (loops again)
			print("There was an error, please enter Y or N")
#######################################################################
# Function: inputpercentage(prompt, default)
# Description: This test whether the user input percentages as .5,etc. or 50,etc. and converts them to the former scale
# Parameters: prompt is the text that will prompt the user, default is the value that will be used if user presses enter
# Pre-Conditions: Both inputs are strings (default will be converted if needed)
# Post-Conditions: None
# Returns: percentage in decimal form
# Variables: raw - temporary storage space for input 
# 		 perc - percentage value picked by user
#######################################################################
def inputpercentage(prompt, default):
	while(True):
		#Ask the user for input in format (prompt+” [“+default+”]: “)
		raw = input(prompt+" ["+default+"]: ")
		#Store as raw
		#if raw is “” set raw = to default
		if raw == "": raw = default
		#try the following
		try:
			#perc = float(raw)
			perc = float(raw)
			#if perc is less than 3 (it is probably not more than 300%)
			if perc < 3.0:
				return perc
			#elif perc is more than or equal to 3 (probably a mistake or 3%)
			elif perc >= 3.0:
				perc /= 100
				return perc
		except:
			#print error message about valid number (loops again)	
			print("There was an error, please enter a Percentage as integer or float (Do not type %)")

#######################################################################
# Function: inputposint(prompt, default)
# Description: This makes sure that the user entered a valid positive integer 
# Parameters: prompt is the text that will prompt the user, default is the value that will be used if user presses enter
# Pre-Conditions: Both inputs are strings (default will be converted if needed)
# Post-Conditions: None
# Returns: positive float
# Variables: raw - temporary storage space for input 
#######################################################################
def inputposint(prompt, default):
	while(True):
		#Ask the user for input in format (prompt+” [“+default+”]: “)
		raw = input(prompt + " ["+default+"]: ")
		#Store as raw
		#if raw is “” set raw = to default
		if raw == "": raw = default
		#try the following
		try:
			#raw = int(raw)
			raw = int(raw)
			#if raw >= 0 then
			if raw >= 0:
				return raw
		except:		
			print("There was an error, please enter a Positive Integer")	
##This Else Statment was in the wrong place in my pseudo
		else:
			if raw < 0 :print("Number Cannot be Negative!")
#######################################################################
# Function: inputposfloat(prompt, default)
# Description: This makes sure that the user entered a valid positive float 
# Parameters: prompt is the text that will prompt the user, default is the value that will be used if user presses enter
# Pre-Conditions: Both inputs are strings (default will be converted if needed)
# Post-Conditions: None
# Returns: positive float
# Variables: raw - temporary storage space for input 
#######################################################################
def inputposfloat(prompt, default):
	while(True):
		#Ask the user for input in format (prompt+” [“+default+”]: “)
		raw = input(prompt + " ["+default+"]: ")
		#Store as raw
		#if raw is “” set raw = to default
		if raw == "": raw = default
		#try the following
		try:
			#raw = float(raw)
			raw = float(raw)
			#if raw >= 0 then
			if raw >= 0:
				return raw
		except:		
			print("There was an error, please enter a Positive Integer")	
##Likewize Was in the wrong place
		else:
			if raw < 0 :print("Number Cannot be Negative!")

#######################################################################
# Function: check_total_percentage(weight)
# Description: sums the weights to check if they add up to 100
# Parameters: weight is the list of the values to be sumed
# Pre-Conditions: weight is a valid list
# Post-Conditions: None
# Variables: current_sum
#######################################################################
def check_total_percentage(weight):
	#set current_sum equal to 0
	current_sum = 0
	#for each category
	for w in weight:
		#Added weight to current_sum
		current_sum += w 
	if current_sum != 1:
		print()
		print("WARNING: Your weights add up to "+str(int(current_sum*100))+"%")
		print("They should add up to 100%. This means that")
		print("The answer is most likely incorrect. Please")
		print("check the numbers and calculate a new grade")
		print()
#######################################################################
# Function: main()
# Description: Function that calls all other function
# Parameters: None
# Pre-Conditions: None
# Post-Conditions: Program Complete
# Variables: repeat - variable controls whether program repeats
#            category_counts - List of 4 categories Which will contain the
#                              number of assignments for each category 
#            category_title - List of 4 titles which will be used to identify 
#                             current categories to users
#            category_weight - List of the percentage values of weight for 
#                              each category
#	     category_average_score - calculated average score for each 
#                                     category
#	     category_weighted_average - weighted average
#######################################################################
def main():
	printmanual()
	#set repeat as true
	repeat = True
	#loop the following while repeat is true
	while(repeat):
#################Had to move this into the while loop
		#set category_title as a list of titles (tests, assignments, quizzes, and labs)
		category_title = ["tests", "assignments", "quizzes", "labs"]
		#initialize category_counts as a list with 4 values
		#initialize category_weight as a list with 4 values
		#initialize category_average_score as a list with 4 values
		#initialize category_weighted_average as a list with 4 values
		category_counts = [0]*len(category_title)
		category_weight = [0]*len(category_title)
		category_average_score = [0]*len(category_title)
		category_weighted_average = [0]*len(category_title)		
		get_initial_input(category_title, category_counts, category_weight)
		get_scores(category_title, category_counts, category_average_score)
#################Get Special Assignment - New Function
#(title, counts, average, weight, weighted_average)
		get_special_assignment(category_title, category_counts, category_average_score, category_weight, category_weighted_average)
		calculate_weighted_avg(category_title, category_weight, category_average_score, category_weighted_average)
		class_grade = calculate_class_grade(category_weighted_average)
		check_total_percentage(category_weight)
		print("Your Grade is "+str(class_grade)+"%")
		print(category_counts, category_title, category_weight, category_average_score, category_weighted_average)
		repeat = yonq("Do you want to calculate another grade?", "Y")
main()
