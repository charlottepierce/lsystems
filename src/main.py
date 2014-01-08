#!/usr/bin/python

import turtle
from turtle_command import CommandString

if __name__ == '__main__':
	win = turtle.Screen()
	win.title('L-Systems with turtle graphics')

	turtle = turtle.Turtle()
	turtle.pensize(3)
	start_pos = turtle.pos()
	start_heading = turtle.heading()

	cmd = CommandString('F', {'F' : 'F-F+F+F-F'}, 100, 90)

	for x in range(2):
		print 'Command:', cmd.command_string
		for c in cmd.command_string:
			if c == 'F':
				turtle.pendown()
				turtle.forward(cmd.step_size)
			elif c == 'f':
				turtle.penup()
				turtle.forward(cmd.step_size)
			elif c == '+':
				turtle.right(cmd.angle_increment)
			elif c == '-':
				turtle.left(cmd.angle_increment)

		cmd.evolve()
		turtle.penup()
		turtle.home()

	win.exitonclick()

