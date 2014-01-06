class CommandString():
	def __init__(initiator, productions, step_size, angle_inc):
		''' Create a new command string.

		args
		----
			initiator: the initial command string
			production: the rules by which to generate subsequent command strings.
				Should be a list of tuples in the form `(prev, replacement)` - whenever
				a subsequent command string is generated the each instance of `prev` is
				replaced with it's corresponding `replacement`.
			step_size: the amount by which to move forward in a single step
			angle_inc: the amount by which to turn when directed to do so

		'''

