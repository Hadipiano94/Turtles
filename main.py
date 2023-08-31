import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)


def go_forward():
    tim.forward(3)


def go_backward():
    tim.backward(2)


def turn_right():
    tim.right(2)


def turn_left():
    tim.left(2)


def circle():
    tim.circle(100)


def go_up():
    if tim.heading() != 90:
        tim.setheading(90)
    tim.forward(2)


def go_down():
    if tim.heading() != 270:
        tim.setheading(270)
    tim.forward(2)


def go_left():
    if tim.heading() != 180:
        tim.setheading(180)
    tim.forward(2)


def go_right():
    if tim.heading() != 0:
        tim.setheading(0)
    tim.forward(2)


def black_dot():
    tim.dot(10)


def red_dot():
    tim.dot(10, (255, 0, 0))


def reset():
    screen.reset()


def stamp():
    tim.stamp()


screen = Screen()
screen.setup(width=800, height=500)
screen.title('Turtle Race')
tim = Turtle()
tim.penup()
tim.color('black')
tim.shape('turtle')
jon = Turtle()
jon.penup()
jon.color('red')
jon.shape('turtle')
bet_color = None
while bet_color is None or bet_color == "":
    bet_color = turtle.textinput('Bet!', 'Pick a Color: ')

tim.setposition(-380, 50)
jon.setposition(-380, -50)
moves = [3, 5, 10, 0, 0, 0]
while (tim.position()[0] < 380) and (jon.position()[0] < 380):
    jon.forward(random.choice(moves))
    tim.forward(random.choice(moves))
print('done')
if tim.position()[0] > jon.position()[0]:
    winner = tim
else:
    winner = jon

if winner.color()[0] == bet_color:
    print('Nice bet!')
else:
    print('loooooser!')


screen.exitonclick()
