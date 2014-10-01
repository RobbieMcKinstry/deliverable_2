from fold_math import add
from fold_math import subtract
from fold_math import divide
from fold_math import multiply

class Fold:

	def __init__(self, core):
		self.cores = core
		
	def __add__(self):
		return add([18,31,27,2], self.cores)

	def __truediv__(self):
		return divide([72,3,4], self.cores)

	def __sub__(self):
		return subtract([14,3,7,2], self.cores)

	def __mult__(self):
		return multiply([3,2,8,10], self.cores)