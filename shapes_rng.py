#Shape Generator by Nihaal Sangha

import turtle #Loads up turtle
import os, sys #Loads up for 68:5
import random #Random num gen

def Restart():
	os.execl(sys.executable, sys.executable, *sys.argv)

def RandomPenCode():

	R=random.randrange(1, 256)
	G=random.randrange(1, 256)
	B=random.randrange(1, 256)

	turtle.colormode(255) # 1 - Colour string, 255 - RGB
	turtle.pensize(4)
	turtle.pencolor(R, G, B) #Sets the pen colour

def RandomFillCode():

	R=random.randrange(1, 256)
	G=random.randrange(1, 256)
	B=random.randrange(1, 256)

	turtle.colormode(255)
	turtle.fillcolor(R, G, B) #Sets the Fill Colour
	turtle.begin_fill() #Starts Fill

#turtle.colormode(255) # 1 - Colour string, 255 - RGB
#Times=5 #Choose the amount of times it makes the shape
#Sides=10 #Choose how many sides each shape has (not star)
#Star=1 #Star Yes or No
#Star_Points=5 #Amount of points on star

#Length=2 #Choose how long each side is
#Star_Length=59 #Choose length of each side of star (Length var is used - 22:5)
#Fill="Red" #Choose colour of the inside of the shape
#Pen="Red" #Choose pen colour
Random=input("Do you want a random shape?")
if Random=="Yes" or Random =="yes" or Random=="Y" or Random=="y": #Random
	RandomNum=random.randrange(1, 3)

	if RandomNum==1: #Star
		Star_Points=random.randrange(5, 11)
		#if Star_Points<=7:
			#Length=
		Length=50
		Times=random.randrange(1, 11)
		#turtle.colormode(255)
		RandomPenCode()
		FillT=input("Do you want to fill your shape?")
		if FillT=="Yes" or FillT=="yes" or FillT=="Y" or FillT=="y":
			#turtle.colormode(255)
			RandomFillCode()
		Star_Angle=360/Star_Points
		Star_Alt_Angle=Star_Angle * 2
		Star_Length=Length
		for i in range(Times): #Loops...
			turtle.right(360/Times) #Turns for next itteration of shape
			for i in range(Star_Points):
				turtle.forward(Star_Length)
				turtle.right(Star_Angle)
				turtle.forward(Star_Length)
				turtle.left(Star_Alt_Angle)

	elif RandomNum==2: #Shape
		Sides=random.randrange(3, 10)
		#if Sides<= :
			#Length=
		Length=100
		Times=random.randrange(1, 9)
		#turtle.colormode(255)
		RandomPenCode()
		FillT=input("Do you want to fill your shape?")
		if FillT=="Yes" or FillT=="yes" or FillT=="Y" or FillT=="y":
			#turtle.colormode(255)
			RandomFillCode()
		for i in range(Times): #Loops...
			turtle.right(360/Times) #Turns for next itteration of shape
			for i in range(Sides): #Loops...
				turtle.forward (Length) #Moves turtle forward the length specified
				turtle.right (360/Sides) #Turns angle needed to make one shape

else:

	Star=input("Do you want a star?")

	if Star=="Yes" or Star=="yes" or Star=="Y" or Star=="y": #Star
		Star_Points=int(input("How many points do you want each star?"))
		if Star_Points<5:
			print("It must be at least five. Try again.")
			Star_Points=int(input("How many points do you want each star?"))
		Length=int(input("How long do you want each side of the star to be?"))
		Times=int(input("How many stars do you want?"))
		Pen=input("What colour do you want your lines to be? Leave blank for black")
		if Pen=="":
			Pen="Black"
		turtle.colormode(1)
		turtle.pencolor(Pen) #Sets the pen colour
		FillT=input("Do you want to fill your star?")
		if FillT=="Yes" or FillT=="yes" or FillT=="Y" or FillT=="y":
			Fill=input("What colour do you want it to be filled in?")
			turtle.fillcolor(Fill) #Sets the Fill Colour
			turtle.begin_fill() #Starts Fill
		Star_Angle=360/Star_Points
		Star_Alt_Angle=Star_Angle * 2
		Star_Length=Length #22:5, 39:28
		for i in range(Times): #Loops...
			turtle.right(360/Times) #Turns for next itteration of shape
			for i in range(Star_Points):
				turtle.forward(Star_Length)
				turtle.right(Star_Angle)
				turtle.forward(Star_Length)
				turtle.left(Star_Alt_Angle)

	elif Star=="No" or Star=="no" or Star=="N" or Star=="n": #Shape
		Sides=int(input("How many sides do you want on each shape?"))
		if Sides<3:
			print("It must be at least three. Try again.")
			Sides=int(input("How many sides do you want on each shape?"))
		Length=int(input("How long do you want each side of the shape to be?"))
		Times=int(input("How many shapes do you want?"))
		Pen=input("What colour do you want your lines to be? Leave blank for black")
		if Pen=="":
			Pen="Black"
		turtle.colormode(1)
		turtle.pencolor(Pen) #Sets the pen colour
		FillT=input("Do you want to fill your shape?")
		if FillT=="Yes" or FillT=="yes" or FillT=="Y" or FillT=="y":
			Fill=input("What colour do you want it to be filled in?")
			turtle.fillcolor(Fill) #Sets the Fill Colour
			turtle.begin_fill() #Starts Fill
		for i in range(Times): #Loops...
			turtle.right(360/Times) #Turns for next itteration of shape
			for i in range(Sides): #Loops...
				turtle.forward (Length) #Moves turtle forward the length specified
				turtle.right (360/Sides) #Turns angle needed to make one shape

	else:
		print("Type Yes or No. Try again.")
		Restart()

turtle.end_fill() #Stops fill
turtle.done() #End
