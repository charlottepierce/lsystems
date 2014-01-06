#!/usr/bin/python

import turtle

if __name__ == '__main__':
	win = turtle.Screen()
	win.title('L-Systems with turtle graphics')

	turtle = turtle.Turtle()
	turtle.pensize(3)

	turtle.left(90)
	turtle.forward(75)

	win.exitonclick()

