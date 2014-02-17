#!/usr/bin/python

import turtle as t
from turtle_command import CommandString

class LSystemDemo:
	def __init__(self, win, turtle, cmd):
		self.win = win
		self.turtle = turtle
		self.cmd = cmd
		self.state_stack = []
		# set up key bindings
		self.win.onkey(self.next_evolution, "n")
		self.win.onkey(self.close, "Escape")
		t.listen()

		t.mainloop()

	def next_evolution(self):
		print 'Evolving command string ...',
		cmd.evolve()
		print 'done'

		print 'Drawing ...',
		self.draw_shape()
		print 'done'

	def close(self):
		self.win.bye()

	def draw_shape(self):
		for c in self.cmd.command_string:
			if c == 'F':
				self.turtle.pendown()
				self.turtle.forward(cmd.step_size)
			elif c == 'f':
				self.turtle.penup()
				self.turtle.forward(cmd.step_size)
			elif c == '+':
				self.turtle.right(cmd.angle_increment)
			elif c == '-':
				self.turtle.left(cmd.angle_increment)
			elif c == '[':
				self.state_stack.append((self.turtle.pos(), self.turtle.heading()))
			elif c == ']':
				self.turtle.penup()
				pos, heading = self.state_stack.pop()
				self.turtle.setpos(pos)
				self.turtle.setheading(heading)

if __name__ == '__main__':
	# initialise window
	win = t.Screen()
	win.title('L-Systems with turtle graphics')
	win.delay(0) # do not delay drawing at all

	# initialise turtle
	turtle = t.Turtle()
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
		print ' *', prev, '->', replacement

	demo = LSystemDemo(win, turtle, cmd)

