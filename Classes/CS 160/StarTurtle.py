####################################################################### 
# Program Filename: StarTurtle.py
# Author: Cody Ray Hoeft
# Date: November 4, 2013
# Description: This program opens up a turtle gui and draws a star
# Input: Click
# Output: A Star
#######################################################################import turtle
#Setup the evironment
import turtle
wind = turtle.Screen()
wind.bgcolor("black")
wind.title("Hello World")
wind.setup(width=.95, height=.95, startx=None, starty=None)

tur1 = turtle.Turtle()
tur1.color("yellow")
tur1.pensize(5)
tur1.shape("turtle")

####################################################################### 
# Function: star
# Description: program makes a star
# Parameters: X and Y are location of click
# Pre-Conditions: Screen in unknown condition
# Post-Conditions: Star on screen
#######################################################################
def star(x, y):
	tur1.clear()
	for x in range(5): #Draw once for each tip of the star
		tur1.forward(200) #Draw 1 Length
		tur1.right(144) #Turn Right 144 degrees for next side then repeat
wind.onscreenclick(star)
wind.mainloop()

