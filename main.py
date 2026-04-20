from turtle import *
import random


def create_player():
    global player
    player = Turtle()
    player.speed(0)
    player.color("black")
    player.shape("turtle")


def up():
    global player
    player.setheading(90)
    player.sety(player.ycor()+10)

def down():
    global player
    player.setheading(-90)
    player.sety(player.ycor()-10)

def right():
    global player
    player.right(10)
    # player.setheading(0)
    # player.setx(player.xcor()+10)

def left():
    global player
    player.left(10)
    # player.setheading(180)
    # player.setx(player.xcor()-10)

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"
    pass

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

def create_turtle():
    turts = Turtle()
    turts.color(generate_color())
    turts.speed(0)
    turts.shape("circle")
    turts.setheading(random.randint(0,360))
    return turts

def move_with_heading(t, turtles):
    t.forward(5)
    if t.xcor()>260 or t.xcor()<-260:
        t.setheading(180-t.heading())
        t.forward(10)
        new=create_turtle()
        turtles.append(new)
    if t.ycor()>260 or t.ycor()<-260:
        t.setheading(-t.heading())
        t.forward(10)
        new=create_turtle()
        turtles.append(new)
    return turtles

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

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 560, height = 560)
screen.listen()
screen.onkey(create_player, "space")
screen.onkeypress(up, "w")
screen.onkeypress(down,"s")
screen.onkeypress(right,"d")
screen.onkeypress(left,"a")



yertle = Turtle()
yertle.color("pink")
yertle.speed(0)
yertle.shape("circle")
yertle.setheading(random.randint(0,360))
deltax = random.randint(-10,10)
deltay = random.randint(-10,10)
alive = True
# yertle.setheading(random.randint(0,360))
turtles = [yertle]

playing_area()
player = None

while alive:
    if player!= None:
        move_with_heading(player,turtles)
    for obj in turtles:
        turtles = move_with_heading(obj,turtles)
        if player != None and player.distance(obj) < 20:
            obj.hideturtle()
            turtles.remove(obj)
        

    # deltax,deltay = move_with_deltas(yertle,deltax,deltay)
    # for turt in turtles:
    #     move_with_heading(turt)
    




screen.exitonclick()