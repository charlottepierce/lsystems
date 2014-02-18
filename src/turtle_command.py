class CommandString():
	''' A command string describing the movement pattern of a turtle.

	Consists of an initial movement pattern - where each character indicates
	a single movement - and a series of rules by which the movement pattern
	evolves over time.

	There are four possible commands for a turtle:
		'F': move forward one step whilst drawing a line
		'f': move forward one step without drawing a line
		'+': turn one angle increment right
		'-': turn one angle increment left
		'[': push current turtle state onto stack
		']': pop turtle state from the stack

	'''

	def __init__(self, initiator, productions, step_size, angle_inc):
		''' Create a new command string.

		args
		----
			initiator: the initial command string
			production: the rules by which to generate subsequent command strings.
				Should be a dictionary with entires in the form `prev : replacement` where `prev`
				is a single character. Whenever a subsequent command string is generated each
				instance of `prev` is replaced with it's corresponding `replacement`.
				Productions are applied in parallel, and it is assumed that each `prev` in
				the set of productions is unique (i.e., that productions are mutually
				exclusive).
			step_size: the amount by which to move forward in a single step
			angle_inc: the amount - in degrees - by which to turn when directed to do so

		'''

		self.initiator = initiator
		self.command_string = initiator
		self.productions = productions
		self.step_size = step_size
		self.angle_increment = angle_inc

	def evolve(self):
		''' Evolve the command string to its next version, according to the productions.

		Productions are applied in parallel (i.e., all at once) to avoid infinite looping
		of production applications, hence incorrect evolutions. This works on under the
		assumption that productions are mutually exclusive, with single-character predicates.

		'''

		# create new command string
		prev = self.command_string
		self.command_string = ''.join([self.productions[char] if char in self.productions.keys() else char for char in self.command_string])

	def reset(self):
		''' Reset the command string to describe the base shape. '''

		self.command_string = self.initiator

