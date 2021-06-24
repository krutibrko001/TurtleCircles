from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()
screen.title("Circles")
my_turtle = Turtle()
#screen.tracer(0)
my_turtle.speed(0)
screen.setup(width = 1000, height= 1000)
screen.colormode(255)

lst_heading = [0, 90, 180, 270]
lst_size = [10, 15, 25, 30, 7, 3, 35,50,100]
lst_pen_size = [1,2,3,4,5,10]


for i in range(1000):
  # Setting up the Colors.
  r = randint(1,255)
  g = randint(1,255)
  b = randint(1,255)
  my_turtle.color(r,g,b)

  # Chosing random heading and size of the Circle
  my_heading = choice(lst_heading)
  my_size = choice(lst_size)
  pns = choice(lst_pen_size)

  my_turtle.setheading(my_heading)
  my_turtle.circle(my_size)
  my_turtle.forward(my_size)

  # Checking if my turtle if out of bounded screen. 
  if my_turtle.xcor() > 300 or my_turtle.ycor() > 300:
    my_turtle.goto(0,0)



screen.exitonclick()
screen.mainloop()
