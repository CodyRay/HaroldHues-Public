/*####################################################################### 
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
#######################################################################*/
#include <iostream>
#include <string>
#include <cstdlib>
#include <istream>
#include <sstream>
#include <stdio.h>
#include <limits>
#include <climits>
using namespace std;
bool yonq(string prompt, string default_str);
double inputposfloat(string prompt, string default_value);
double inputposint(string prompt, string default_value);
/*#####################################################################
# Function: yonq(prompt, default)
# Description: Asks the user a  Y es  O r  N o  Q uestion and converts the answer to a boolean
# Parameters: prompt is the text that will prompt the user, default is the value that will be used if user presses enter
# Pre-Conditions: both parameters are strings
# Post-Conditions: None
# Returns: Boolean
# Variables: raw - temporary storage space for input 
#####################################################################*/
bool yonq(string prompt, string default_str)
	{
	string raw;
	while(1<2)
		{
		//Ask the user for input in format (prompt+” [“+default+”]: “)
	cout << prompt << " [" << default_str << "]: ";
	//cin.ignore(1);
	getline(cin, raw);
	if(raw.empty()) raw=default_str;
	//cin.ignore(1000);
		//raw = raw_line.at(0);
		//Store as raw
		//if raw’s first letter (capitalized) is 
		if(toupper(raw.at(0)) == 'Y') //Need first char of raw[0:1].upper() == 'Y':
			{
			//return true
			return true;
			}
		//elif raw’s first letter (capitalized) is N
		else if(toupper(raw.at(0)) == 'N')//Need first caricture raw[0:1].upper() == 'N':
			{
			//return false
			return false;
			}
		else
			{
			//print error message (loops again)
			//print("There was an error, please enter Y or N")
			cout << "There was an error, please enter Y or N\n";
			}
		}
	}
/*#####################################################################
# Function: inputposfloat(prompt, default)
# Description: This makes sure that the user entered a valid positive float 
# Parameters: prompt is the text that will prompt the user, default is the value that will be used if user presses enter
# Pre-Conditions: Both inputs are strings (default will be converted if needed)
# Post-Conditions: None
# Returns: positive float
# Variables: raw - temporary storage space for input 
#####################################################################*/
double inputposfloat(string prompt, string default_value)
	{
	string raw; double raw_double;
	while(true)
		{
		//Ask input in format prompt? [def]: 
		cout << prompt << " [" << default_value << "]: ";
		getline(cin, raw);
		if(raw.empty()) raw=default_value;
		//If raw is "" set raw to default
		try
			{
			raw_double = atof(raw.c_str());
			//raw_double = raw;
			if(raw_double >= 0)
				{
				return raw_double;
				}
			}
		catch(...)
			{
			cout << "There was an error, please enter a Positive Integer\n";
			}
		if(raw_double < 0)
			{
			cout << "Number Cannot be Negative!\n";
			}
		}
	}
/*#####################################################################
# Function: inputposint(prompt, default)
# Description: This makes sure that the user entered a valid positive float 
# Parameters: prompt is the text that will prompt the user, default is the value that will be used if user presses enter
# Pre-Conditions: Both inputs are strings (default will be converted if needed)
# Post-Conditions: None
# Returns: positive int
# Variables: raw - temporary storage space for input 
#####################################################################*/
double inputposint(string prompt, string default_value)
	{
	string raw; int raw_int;
	while(true)
		{
		//Ask input in format prompt? [def]: 
		cout << prompt << " [" << default_value << "]: ";
		getline(cin, raw);
		if(raw.empty()) raw=default_value;
		//If raw is "" set raw to default
		try
			{
			raw_int = atoi(raw.c_str()); 
			if(raw_int >= 0)
				{
				return raw_int;
				}
			}
		catch(...)
			{
			cout << "There was an error, please enter a Positive Integer\n";
			}
		if(raw_int < 0)
			{
			cout << "Number Cannot be Negative!\n";
			}
		}
	}
/*#####################################################################
# Function: printmanual()
# Description: Prints the Manual for the program
# Parameters: None
# Pre-Conditions: None
# Post-Conditions: None
#####################################################################*/
void printmanual(){
cout << "\nWelcome to BabyRoot (Babylonian Root Calculator)\nBabyRoot Will find the Square Root of numbers for you\n-----------------------------------------------------\n   New Guess = (Guess+(Number/Guess))/2); Repeated\n   until an accurate result is achieved. Google:\n   'Babylonian Algorithm' for more information.\n-----------------------------------------------------\n          See Advanced Options to:\n          1. Set your own Start Guess\n          2. Set the number of Iterations\n          3. Show Intermediate Steps\n-----------------------------------------------------\n";
}

int main()
	{
	double sqnum; double rootguess; int loopnum; string strverb; bool printverb; bool repeatprogram;
	sqnum = 4; //Number that we will find the square root of
	rootguess = sqnum/2; //Variable that we will use to store the current 'guess'
	loopnum = 100; //Number of times the loop will run, higher numbers increase accuracy
	strverb = ""; //Mostly for debug this feature will collect a 'log' of the itterations
	printverb = false; //Turns on 'Print Verbose
	repeatprogram = true; //Variable controlling while loop
	printmanual();
	while(repeatprogram)
		{
		strverb = "Intermediate Steps\n\n";
		cout << "\n";
		sqnum = inputposfloat("What number would you like to find the square root of?", static_cast<ostringstream*>( &(ostringstream() << sqnum) )->str());
		if(yonq("Would you like to change Advanced Settings?", "N"))
			{
			rootguess = inputposfloat("What is your initial guess for the square root", static_cast<ostringstream*>( &(ostringstream() << (sqnum/2.0)) )->str());
			loopnum = inputposint("How many iterations?", static_cast<ostringstream*>( &(ostringstream() << (loopnum)) )->str());
			printverb = yonq("Would you like to show intermediate steps?", "N");
			}
		else
			{
			rootguess = sqnum/2;
			}
		cout << "\n";
		if(!(rootguess==0 || sqnum==0))
			{
			for(int x = loopnum; x>0; x--)
				{
				strverb = strverb +static_cast<ostringstream*>( &(ostringstream() << (x)) )->str()+": "+static_cast<ostringstream*>( &(ostringstream() << (rootguess)) )->str()+"\n";
				rootguess = (rootguess+(sqnum/rootguess))/2;
				}
			}
		else if(sqnum==0)
			{
			rootguess = 0;
			}
		else if(rootguess == 0)
			{
			rootguess = float(sqnum/2);
			for(int x = loopnum; x>0; x--)
				{
				strverb = strverb +static_cast<ostringstream*>( &(ostringstream() << (x)) )->str()+": "+static_cast<ostringstream*>( &(ostringstream() << (rootguess)) )->str()+"\n";
				rootguess = (rootguess+(sqnum/rootguess))/2;
				}
			}
		if(printverb)
			{
			cout << strverb << "\n\n";
			}
		cout << "The Square Root of " << sqnum << " is approximately\n" << rootguess << endl;
		repeatprogram = yonq("Do you want to restart?", "N");
		}
	cout << "Thanks for using BabyCalc\n";
	return 0;
	
	}
