#!/usr/bin/python

import turtle
from turtle_command import CommandString

def draw_shape(turtle, command_string):
	''' Draw the shape described by the given command string and turtle. '''

	for c in command_string:
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

if __name__ == '__main__':
	win = turtle.Screen()
	win.title('L-Systems with turtle graphics')
	win.delay(0) # do not delay drawing at all
	print 'Win height:', win.window_height()

	turtle = turtle.Turtle()
	turtle.setheading(90)
	turtle.pensize(1)
	turtle.hideturtle() # speeds up drawing significantly
	turtle.speed(0) # disable animation

	# move turtle down the screen for more drawing space
	turtle.penup()
	turtle.backward((win.window_height() / 3.0))

	# Edge rewriting
	cmd = CommandString('F-F-F-F', {'F' : 'F-F+F+FF-F-F+F'}, 2, 90)
# 	cmd = CommandString('F', {'F' : 'F[+F]F[-F]F'}, 5, 25.7)
# 	cmd = CommandString('F', {'F' : 'F[+F]F[-F][F]'}, 5, 20)
# 	cmd = CommandString('F', {'F' : 'FF-[-F+F+]+[+F-F-F]'}, 5, 22.5)

	# Node rewriting
# 	cmd = CommandString('X', {'X' : 'F[+X]F[-X]+X', 'F' : 'FF'}, 5, 20)
# 	cmd = CommandString('X', {'X' : 'F[+X][-X]FX', 'F' : 'FF'}, 5, 25.7)
# 	cmd = CommandString('X', {'X' : 'F-[[X]+X]+F[+FX]-X', 'F' : 'FF'}, 5, 22.5)

	print 'Initiator: ', cmd.command_string
	print 'Productions:'
	for prev, replacement in cmd.productions.iteritems():
		print ' -', prev, ' -> ', replacement

	state_stack = []
	for x in range(5):
		print 'Evolving command string', str(x), '...',
		cmd.evolve()
		print 'done'

	print 'Drawing...',
	draw_shape(turtle, cmd.command_string)
	print 'done'

