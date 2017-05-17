import random


class NumberGame(object):
	def __init__(self,min,max):
		self.min = int(min)
		self.max = int(max)
		self.keptNumber = random.randint(self.min,self.max)

	def checkComplianceWithKeptNumber(self,number):
		if self.keptNumber == int(number):
			return 'True'
		else:
			if self.keptNumber > int(number):
				return "Passed number is too small. "
			else:
				return "Passed number is too big. "


