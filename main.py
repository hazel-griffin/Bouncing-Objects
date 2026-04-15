from turtle import *
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 560, height = 560)

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"
    pass


# Creates the rectangular game boundary
def playing_area():
    t = Turtle()
    t.speed(0)
    t.color("white")
    t.begin_fill()
    t.hideturtle()
    t.up()
    t.goto(-260,-260)
    t.down()
    t.goto(-260,260)
    t.goto(260,260)
    t.goto(260,-260)
    t.goto(-260,-260)
    t.end_fill()

print(playing_area())

def move_with_heading(t):
    t.forward(5)
    if t.xcor()>260 or t.xcor()<-260:
        t.setheading(180-t.heading())
        t.forward(10)
    if t.ycor()>260 or t.ycor()<-260:
        t.setheading(-t.heading())
        t.forward(10)
    


def move_with_deltas(turtle, deltax, deltay):
    newx = turtle.xcor() +deltax
    newy = turtle.ycor()+deltay

    if newx > 260 or newx<-260:
        newx = turtle.xcor()
        deltax *= -1
    if newy> 260 or newy<-260:
        newy = turtle.ycor()
        deltay *= -1
    turtle.goto(newx,newy)

    return deltax, deltay
        

yertle = Turtle()
yertle.color("pink")
yertle.speed(0)
yertle.shape("circle")
deltax = random.randint(-10,10)
deltay = random.randint(-10,10)
alive = True
# yertle.setheading(random.randint(0,360))

# turtles = [yertle]
# for i in range(10):
#     t = Turtle()
#     t.color(generate_color())
#     t.speed(0)
#     t.setheading(random.randint(0,360))
#     turtles.append(t)

while alive:
    deltax,deltay = move_with_deltas(yertle,deltax,deltay)
    # for turt in turtles:
    #     move_with_heading(turt)
    pass




screen.exitonclick()