"""
Author: A Cup of Tea
Date: 07/012/2019
"""
import turtle 
import os

myPen=turtle.Turtle()

# take window
window = turtle.Screen()
window.title("Rag Day!!")
window.setup(800, 800)
window.bgcolor("black")

colors = ['blue','white','blue','blue', 'white']
image_name = "./40.gif"
# add the shape first then set the turtle shape
myPen.setposition(-170, 200)
window.addshape(image_name)
myPen.shape(image_name)
myPen.stamp()

myPen.penup()
myPen.setposition(130, 200)
myPen.pendown()
myPen.shape("turtle")
myPen.pensize(3)
myPen.speed(10)
n=-1
for angle in range(0,360,15):
    n=n+1
    if n==5:  n=-1
    myPen.color(colors[n])
    myPen.seth(angle)
    myPen.circle(70)

#stalk = turtle.Turtle()
myPen.width(7)
myPen.color("blue")
myPen.shape("turtle")
myPen.right(75)
myPen.forward(300)
myPen.begin_fill()
myPen.circle(10)
myPen.end_fill()

myPen.penup()
myPen.setposition(-15,-200)
myPen.pendown()
myPen.pencolor('#EC627F')
myPen.write("Happy Rag Day", False, "center", font=('Dynalight', 44,'italic'))

myPen.penup()
myPen.setpos(-20,-250)
myPen.pendown()
myPen.pencolor('#EC627F')
myPen.write("Wishing you all the best in this next phase of your career", 
            False, "center", font=('Arial', 16, 'italic'))

myPen.penup()
myPen.setpos(-40,-340)
myPen.pendown()
myPen.pencolor('#EC627F')
myPen.write("Presented By: Md. Mahedi Hasan", False, "center", font=('Arial', 17, 'normal'))
myPen.penup()
window.exitonclick()
