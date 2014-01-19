####################################################################### 
# Program Filename: Turtlename.py
# Author: Cody Ray Hoeft
# Date: November 4, 2013
# Description: This program opens up a turtle gui and draws my first
#			   name when clicked
# Input: Click
# Output: My Name Drawn out
#######################################################################
import turtle
wind = turtle.Screen()
pointer = turtle.Turtle()

SCALE = 150 #This value manipulates the size of the drawing

wind.setup(.95,.95,None,None)
wind.title("Cody Ray Freeman Hoeft")
wind.bgcolor("orange") #Go Beavers

pointer.shape("circle")
pointer.color("darkblue")
pointer.ht() #Hide Pointer for cleaner look

####################################################################### 
# Function: spellcody
# Description: Routine that draws my name
# Parameters: X and Y are location of click
# Pre-Conditions: Screen in unknown condition
# Post-Conditions: Name is drawn on the screen
#######################################################################
def spellcody(x, y):
	pointer.st() #Show Pointer
	pointer.clear()	
	pointer.pu() #Turn the pen off

	pointer.pencolor("grey")
	pointer.width(10)

	drawlines() #Draw lines on top and bottom of words

	pointer.pencolor("black") #Contrast with the lines
	pointer.width(5)
	
	pointer.goto(-(SCALE*8//2),0) #moves pointer to left corner of letter
	draw_c()
	pointer.goto(-(SCALE*8//2)+SCALE,0)
	draw_o()
	pointer.goto(-(SCALE*8//2)+2*SCALE,0)
	draw_d()
	pointer.goto(-(SCALE*8//2)+3*SCALE,0)
	draw_y()
	pointer.goto(-(SCALE*8//2)+5*SCALE,0)
	draw_r()
	pointer.goto(-(SCALE*8//2)+6*SCALE,0)
	draw_a()
	pointer.goto(-(SCALE*8//2)+7*SCALE,0)
	draw_y()
	pointer.ht()  #Hide the pointer
	resetpointer()
	pointer.speed(20) #Draw it faster next time

####################################################################### 
# Function: drawlines
# Description: Routine that creates a line to draw on.
# Parameters: None
# Pre-Conditions: Screen in blank, pointer is up
# Post-Conditions: Lines are drawn, pointer is up
#######################################################################
def drawlines():
	pointer.goto(-(SCALE*8//2),0)
	pointer.pd()
	pointer.seth(0)
	pointer.fd(SCALE*8)
	pointer.pu()
	pointer.goto(-(SCALE*8//2),SCALE*5//4)
	pointer.pd()
	pointer.seth(0)
	pointer.fd(SCALE*8)
	pointer.pu()
	
####################################################################### 
# Function: resetpointer
# Description: Moves the pointer home
# Parameters: None
# Pre-Conditions: Pointer is not at the origin
# Post-Conditions: Pointer is on the origin
#######################################################################
def resetpointer():
	pointer.home()
	
####################################################################### 
# Function: draw_c
# Description: Draws a capital C
# Parameters: None
# Pre-Conditions: Pointer is at bottom left corner of the origin
# Post-Conditions: Letter is drawn
#######################################################################
def draw_c():
	pointer.pu()
	x = pointer.xcor() + SCALE//2
	y = pointer.ycor() + SCALE//2
	pointer.goto(x,y) #Go to center of C
	pointer.right(45) 
	pointer.fd(SCALE//2) #Navigate to start of C
	pointer.right(90)
	pointer.pd()
	pointer.circle(-SCALE//2,270) #Draw 270 degree's of a circle
	pointer.pu()
####################################################################### 
# Function: draw_o
# Description: Draws a o
# Parameters: None
# Pre-Conditions: Pointer is at bottom left corner of the origin
# Post-Conditions: Letter is drawn
#######################################################################
def draw_o():
	pointer.pu()
	x = pointer.xcor() + SCALE//2 
	y = pointer.ycor()
	pointer.goto(x,y) #Move to bottom Center
	pointer.seth(0)
	pointer.pd()
	pointer.circle(SCALE//4) #Draw a half sized circle
	pointer.pu()
####################################################################### 
# Function: draw_d
# Description: Draws a d
# Parameters: None
# Pre-Conditions: Pointer is at bottom left corner of the origin
# Post-Conditions: Letter is drawn
#######################################################################
def draw_d():
	pointer.pu()
	x = pointer.xcor() + SCALE*3//4
	y = pointer.ycor()
	pointer.goto(x,y) #Go three quarters of the way along the bottom
	pointer.seth(90)
	pointer.pd()
	pointer.fd(SCALE) #Up to top
	pointer.left(180) #Turn arround
	pointer.fd(SCALE//2) #Back down half way
	pointer.right(90) #Turn to the circular part
	pointer.fd(SCALE//4) #Go out a little
	pointer.circle(SCALE//4,180) #Draw a half circle
	pointer.fd(SCALE*3//8) #Go out to make the tail
	
	pointer.pu()
####################################################################### 
# Function: draw_y
# Description: Draws a y
# Parameters: None
# Pre-Conditions: Pointer is at bottom left corner of the origin
# Post-Conditions: Letter is drawn
#######################################################################
def draw_y():
	pointer.pu()
	x = pointer.xcor() + SCALE//2 #Go to the center-bottom
	y = pointer.ycor()
	pointer.goto(x,y)
	pointer.seth(0)
	pointer.pd()
	pointer.left(55) #Turn to upper right for first stroke
	pointer.fd(1.3*SCALE//2) #Go up and turn around
	pointer.left(180)
	pointer.fd(1.3*SCALE) # Draw to bottom
	pointer.left(180)
	pointer.fd(1.3*SCALE//2)# Go Back to center-bottom
	pointer.left(70)
	pointer.fd(1.3*SCALE//2) #Turn and make last stroke
	pointer.pu()
####################################################################### 
# Function: draw_r
# Description: Draws a r
# Parameters: None
# Pre-Conditions: Pointer is at bottom left corner of the origin
# Post-Conditions: Letter is drawn
#######################################################################
def draw_r():
	pointer.pu()
	pointer.seth(0) #point right
	pointer.pd()
	pointer.left(90) #Point Up
	pointer.fd(SCALE) #Up to top
	pointer.right(90) #Turn to the hump
	pointer.fd(SCALE//2)#Forward a little bit
	pointer.circle(-SCALE//4,180)#Half Circle
	pointer.fd(SCALE//2)#Back a little bit
	pointer.left(135)#Turn down for the final stroke
	x = pointer.xcor() + SCALE*3//4
	y = pointer.ycor() - SCALE//2
	pointer.goto(x,y)#Goto the endpoint
	pointer.pu()
####################################################################### 
# Function: draw_a
# Description: Draws an a
# Parameters: None
# Pre-Conditions: Pointer is at bottom left corner of the origin
# Post-Conditions: Letter is drawn
#######################################################################
def draw_a():
	pointer.pu()
	x = pointer.xcor() + SCALE*3//4
	y = pointer.ycor()
	pointer.goto(x,y) #Go three quarters of the way along the bottom
	pointer.seth(90)
	pointer.pd()
	pointer.fd(SCALE//2) #up to top of a
	pointer.left(90) #Turn Left
	pointer.fd(SCALE//4) #Forward a little bit
	pointer.circle(SCALE//4,180) #Half Circle
	pointer.fd(SCALE*3//8) #Make tail
	pointer.pu()

wind.onscreenclick(spellcody) #Start the main function when clicked
wind.mainloop()
