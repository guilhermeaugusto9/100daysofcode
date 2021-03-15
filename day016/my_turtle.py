
# Import lib turtle

#import turtle   # not otimized way if you are using this, you will have to use turtle.funct in every time
from turtle import Turtle,Screen

# creating the object Turtle
timmy = Turtle()      # timmy is the name of the turtle haha
print(timmy)


# aplying methods , see documentation
timmy.shape("turtle")
timmy.color("red","green")

timmy.forward(100)

# Creating a new object  screen to show a screen with the turtle inside
my_screen = Screen()

# appling methods for this screen
print(my_screen.canvheight)
my_screen.exitonclick()