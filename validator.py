__author__ = 'ja'

import abc
import os

class AbstractValidator(object):
    __metaclass__  = abc.ABCMeta
    @abc.abstractmethod
    def validate(self, to_be_validated):
        """validate the input"""

class BadNumberChoosen(Exception):
	pass

class BadNumberOfGamePassed(Exception):
	pass

class BadIndexPassed(Exception):
	pass

class NotANumber(Exception):
	pass

class BadSizeOfBoardError(Exception):
	pass

class TakenPlaceInBoardError(Exception):
	pass

class PassedIndexValidator(AbstractValidator):
	"""validates the passed index"""
	def __init__(self,to_be_validated,size):
		self.index = to_be_validated
		self.size = int(size)
	def validate(self):
		if isinstance(self.index,(int,float)):
			if self.index not in range(self.size**2+1):
				raise BadIndexPassed()
		else:
			if not self.index.isdigit() or int(self.index) not in range(self.size**2+1):
				raise BadIndexPassed()


class GameChooseValidator(AbstractValidator):
	def __init__(self,to_be_validated):
		self.number = to_be_validated

	def validate(self):
		if self.number != 1 and self.number != 2:
			raise BadNumberOfGamePassed()


class NumberChooseValidator(AbstractValidator):
	def __init__(self,to_be_validated):
		self.number = to_be_validated

	def validate(self):
		if not self.number.isdigit() or int(self.number) not in range(0,101):
			raise BadNumberChoosen()

class SizeOfBoardValidator(AbstractValidator):
	def __init__(self,to_be_validated):
		self.number = to_be_validated

	def validate(self):
		if not self.number.isdigit() or int(self.number) < 3:
			raise BadSizeOfBoardError()
