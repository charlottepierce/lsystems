#!/usr/bin/python

import turtle
from turtle_command import CommandString

if __name__ == '__main__':
	win = turtle.Screen()
	win.title('L-Systems with turtle graphics')

	turtle = turtle.Turtle()
	turtle.setheading(90)
	turtle.pensize(1)
	turtle.hideturtle() # speeds up drawing significantly
	turtle.speed(0) # disable animation
	start_pos = turtle.pos()
	start_heading = turtle.heading()

	cmd = CommandString('F', {'F' : 'F[+F]F[-F]F'}, 5, 25.7)

	state_stack = []
	for x in range(7):
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
				turtle.penup()
				pos, heading = state_stack.pop()
				turtle.setpos(pos)
				turtle.setheading(heading)

		cmd.evolve()
		turtle.penup()
		turtle.setpos(start_pos)
		turtle.setheading(start_heading)

	print 'Done'

	win.exitonclick()

