#!/usr/bin/python

import turtle
from turtle_command import CommandString

if __name__ == '__main__':
	win = turtle.Screen()
	win.title('L-Systems with turtle graphics')

	turtle = turtle.Turtle()
	turtle.pensize(1)
	turtle.hideturtle() # speeds up drawing significantly
	turtle.speed(0) # disable animation
	start_pos = turtle.pos()
	start_heading = turtle.heading()

	cmd = CommandString('F-F-F-F', {'F' : 'F-F+F+FF-F-F+F'}, 20, 90)

	state_stack = []
	for x in range(5):
		print 'Command:', cmd.command_string, '(' + str(cmd.step_size) + ')'
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
			elif c == '[':
				state_stack.append((turtle.pos(), turtle.heading()))
			elif c == ']':
				pos, heading = state_stack.pop()
				turtle.setpos(pos)
				turtle.setheading(heading)

		cmd.evolve()
		turtle.penup()
		turtle.home()

	print 'Done'

	win.exitonclick()

