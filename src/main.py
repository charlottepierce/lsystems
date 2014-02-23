#!/usr/bin/python

import random
import turtle as t
from turtle_command import CommandString

class LSystemDemo:
	def __init__(self, win, turtle, cmd):
		self.win = win
		self.turtle = turtle
		self.cmd = cmd
		self.overwrite = False
		self.state_stack = []
		# set up key bindings
		self.win.onkey(self.reset, "r")
		self.win.onkey(self.next_evolution, "n")
		self.win.onkey(self.clear, "c")
		self.win.onkey(self.toggle_overwrite, "o")
		self.win.onkey(self.close, "Escape")
		# store initial turtle position
		self.init_pos, self.init_heading = self.turtle.pos(), self.turtle.heading()

		self.draw()
		t.listen()
		t.mainloop()

	def next_evolution(self):
		# reset turtle position, change pen colour if necessary
		self.turtle.penup()
		self.turtle.setpos(self.init_pos)
		self.turtle.setheading(self.init_heading)
		if not self.overwrite:
			self.random_pen()
		else:
			self.clear()

		print 'Evolving command string ...',
		cmd.evolve()
		print 'done'

		print 'Drawing ...',
		self.draw()
		print 'done'

	def clear(self):
		self.turtle.clear()
		print "[canvas cleared]"

	def toggle_overwrite(self):
		self.overwrite = not self.overwrite
		print "Clearing after evolution:", self.overwrite

	def random_pen(self):
		r, g, b = random.random(), random.random(), random.random()
		self.turtle.pencolor(r, g, b)

	def close(self):
		self.win.bye()

	def draw(self):
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

	def reset(self):
		self.cmd.reset()

		self.clear()
		self.turtle.penup()
		self.turtle.setpos(self.init_pos)
		self.turtle.setheading(self.init_heading)

		self.turtle.pencolor("black")
		self.draw()
		print "[demo reset]"

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
	cmd = CommandString('F-F-F-F', {'F' : 'F-F+F+FF-F-F+F'}, 10, 90)
#  	cmd = CommandString('F', {'F' : 'F[+F]F[-F]F'}, 5, 25.7)
# 	cmd = CommandString('F', {'F' : 'F[+F]F[-F][F]'}, 5, 30)
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

