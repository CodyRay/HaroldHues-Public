/*##################################################################### 
# Program Filename: PyCalc.py
# Author: Cody Ray Freeman Hoeft
# Date: October 21, 2013
# Description: PyCalc is a powerful calculator that allows operations  
#      to be performed on the command line. Options Include: +, ++, -, 
#      /, //, *, **, and %.
# Input: Two Numbers and an operator
# Output: Resulting Calculation
#####################################################################*/
#include <iostream>
#include <string>
#include <cstdlib>
#include <istream>
#include <sstream>
#include <stdio.h>
#include <limits>
#include <climits>
#include <math.h>
using namespace std;
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
# Function: inputfloat(prompt, default)
# Description: This makes sure that the user entered a valid positive float 
# Parameters: prompt is the text that will prompt the user, default is the value that will be used if user presses enter
# Pre-Conditions: Both inputs are strings (default will be converted if needed)
# Post-Conditions: None
# Returns: positive float
# Variables: raw - temporary storage space for input 
#####################################################################*/
double inputfloat(string prompt, string default_value)
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
			return raw_double;
			}
		catch(...)
			{
			cout << "There was an error, please enter a Positive Integer\n";
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
			cout << "Number Cannot be Negative!";
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
int main()
	{
	float num_1 = 0;
	string opp_var = "++";
	float num_2 = 0;
	string raw_input = "?"; //Used to store values until they are verified
	bool repeatprogram = true;
	//####Print Manual on Screen for user
	cout<<"\nWelcome to PyCalc (Python Calculator)\nPyCalc Supports the Following Operations\n-----------------------------------------\nAddition      (+)    Divide          (//)\nAdd One      (++)    Remainder        (%)\nSubtract      (-)    Multiply         (*)\nDivide (Float)(/)    Exponent         (^)\n-----------------------------------------\n\n";
	//#######################################################################
	//####Loop
	try //#Necessary for error message
		{
		while(repeatprogram)//Allows program to repeat
			{
			
			
			//####Get inputs from user
			//#What is First Number?
			num_1=inputfloat("First Number", static_cast<ostringstream*>( &(ostringstream() << (num_1)) )->str());
			
	//#What is Operator? (Automatically Convert to Lower Case if Not Already)
			string raw;

			cout << "Operator [" << opp_var << "]: ";
			getline(cin, raw);
			if(!raw.empty()) opp_var=raw;

	//#What is Second Number?
			if(!(opp_var == "++"))// #No need if it is ++
				{
				num_2=inputfloat("Second Number", static_cast<ostringstream*>( &(ostringstream() << (num_2)) )->str());
				}
			else
				{
				num_2=1;// #"Clear" the Variable
				}
	//#Print The Opperation to be Performed	
			cout << num_1 << " " << opp_var << " " << num_2 << " " << "=\n\n";
	//####If Statement of different Possible Operators
		//#Addition                         Valid Values (+, plus, add)
			if(opp_var == "+" || opp_var == "plus" || opp_var == "add")
				{
				num_1=(num_1 + num_2);
				cout << num_1 << "\n";
				}
		//#Add One                          Valid Values (++)
			else if(opp_var == "++")
				{
				num_1=(num_1 + 1);
				cout << num_1 << "\n";
				}
		//Subtraction                      Valid Values (-, minus, subtract)
			else if(opp_var == "-" || opp_var == "minus" || opp_var == "subtract")
				{
				num_1=(num_1 - num_2);
				cout << num_1 << "\n";
				}
		//#Divide into a float              Valid Values (/, \, divide)
			else if(opp_var == "/" || opp_var == "\\" || opp_var == "Divide")
				{
				if(num_2==0)
					{
					cout << "Divide by Zero, I ain't falling for that\n\n";
					num_2=3.14159265359;
					cout << num_1 << " " << opp_var <<" " << num_2 << "=\n";
					}
				num_1=(num_1 / num_2);
				cout << num_1 << "\n";
				}
		//#Divide into integer              Valid Values (//, \\)
			else if(opp_var == "//" || opp_var == "\\\\")
				{
				if(num_2==0)
					{
					cout << "Divide by Zero, I ain't falling for that\n\n";
					num_2=3.14159265359;
					cout << int(num_1) << " " << opp_var <<" " << int(num_2) << "=\n";
					}
				num_1=(int(num_1) / int(num_2));
				cout << num_1 << "\n";
				}
		//#Multiply                         Valid Values (x, *, times, multiply)
			else if(opp_var == "*" || opp_var == "x" || opp_var == "times" || opp_var == "multiply")
				{
				num_1=(num_1 * num_2);
				cout << num_1 << "\n";
				}
		//#Exponent                         Valid Values (^, **)
			else if(opp_var == "^" || opp_var == "**")
				{
				if(num_1==0 && num_2<0)
					{
					cout << "0 to the power of a negative number, No way\n\n";
					num_2=1.41421356237;
					cout << num_1 << " " << opp_var << " " << num_2 << "=\n";
					}
				num_1=(pow(num_1, num_2));
				cout << num_1 << "\n";
				}
		//#Remainder                        Valid Values (r, %)
			else if(opp_var == "r" || opp_var == "%")
				{
				if(num_2==0)
					{
					cout << "Divide by Zero, I ain't falling for that\n\n";
					num_2=299792458;
					cout << num_1 << " " << opp_var << " " << num_2 << "=\n";
					}
				num_1=remainder(num_1, num_2);
				cout << num_1 << "\n";
				}
		//#Something Else? Explain Mistake
			else
				{
				cout << "That was not the Operator you were looking for\n";
				}
			repeatprogram = yonq("Would you like to go again?", "Y");
			}
		}
	//####End Loop
	//#######################################################################

	//####Error Handler
	catch(...)
		{
		cout<<"Well, this is embarrassing, PyCalc had an error. One of us messed up.";
		//#print(sys.exc_info()) #to use this import sys
		}
	cout << "\nGoodbye. Thanks for using PyCalc\n";
	return 0;
	}
	
