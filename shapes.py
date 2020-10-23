import turtle #Loads up turtle
import os
import sys
Star=input("Do you want a star?")
# Times=5 # Choose the amount of times it makes the shape
Sides=10 # Choose how many sides each shape has (not star)
# Star=1
# Star_Points=5

# Length=2 # Choose how long each side is
Star_Length=59 # Choose length of each side of star
Fill="Red" # Choose colour of the inside of the shape
Pen="Red" # Choose pen colour



if Star.lower() == "yes":
    Star_Points=int(input("How many points do you want each star?"))
    if Star_Points<5:
        print("It must be at least five. Try again.")
        Star_Points=int(input("How many points do you want each star?"))
    Length=int(input("How long do you want each side of the star to be?"))
    Times=int(input("How many stars do you want?"))
    Pen=input("What colour do you want your lines to be? Leave blank for black")
    if Pen=="":
        Pen="Black"

    FillT=input("Do you want to fill your shape?")
    if FillT.lower() == "yes":
        Fill=input("What colour do you want it to be filled in?")
        turtle.fillcolor(Fill) # Sets the Fill Colour
        turtle.begin_fill() # Starts Fill
    Star_Angle=360/Star_Points
    Star_Alt_Angle=Star_Angle * 2
    turtle.pencolor(Pen) # Sets the pen colour
    turtle.speed = 0
    turtle.tracer(0, 0)
    for i in range(Times): # Loops...
        turtle.right(360/Times) # Turns for next itteration of shape
        for i in range(Star_Points):
            turtle.forward(Star_Length)
            turtle.right(Star_Angle)
            turtle.forward(Star_Length)
            turtle.left(Star_Alt_Angle)
    turtle.update()

elif Star.lower() == "no":
    Sides=int(input("How many sides do you want on each shape?"))
    if Sides<3:
        print("It must be at least three. Try again.")
        Sides=int(input("How many sides do you want on each shape?"))
    Length=int(input("How long do you want each side of the shape to be?"))
    Times=int(input("How many shapes do you want?"))
    Pen=input("What colour do you want your lines to be? Leave blank for black")
    if Pen=="":
        Pen="Black"

    FillT=input("Do you want to fill your shape?")
    if FillT.lower() == "yes":
        Fill=input("What colour do you want it to be filled in?")
        turtle.fillcolor(Fill) # Sets the Fill Colour
        turtle.begin_fill() # Starts Fill
    turtle.pencolor(Pen) # Sets the pen colour
    turtle.speed = 0
    turtle.tracer(0, 0)
    for i in range(Times): # Loops...
        turtle.right(360/Times) # Turns for next itteration of shape
        for i in range(Sides): # Loops...
            turtle.forward (Length) # Moves turtle forward the length specified
            turtle.right (360/Sides) # Turns angle needed to make one shape
    turtle.update()

else:
    print("Type Yes or No. Try again.")
    os.execl(sys.executable, sys.executable, *sys.argv)

turtle.end_fill() # Stops fill
turtle.done() # End
