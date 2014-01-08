#!/usr/bin/python

import turtle
from turtle_command import CommandString

if __name__ == '__main__':
# 	win = turtle.Screen()
# 	win.title('L-Systems with turtle graphics')
#
# 	turtle = turtle.Turtle()
# 	turtle.pensize(3)
#
# 	turtle.left(90)
# 	turtle.forward(75)
#
# 	win.exitonclick()

	cmd = CommandString('F-F-F-F', {'F' : 'F-F+F+FF-F-F+F'}, 1, 1)

	print 'Intial:', cmd.command_string, cmd.step_size
	for x in range(5):
		cmd.evolve()
		print 'Next:', cmd.command_string, cmd.step_size

