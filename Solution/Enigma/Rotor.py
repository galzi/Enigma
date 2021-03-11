from Translator import Translator

import string, memoize

class Rotor(Translator):
	@staticmethod
	def rotate(l, n):
	    return l[n:] + l[:n]

	def __init__(self, permutation: str, turnover: str, offset: str, setting: str):
		super().__init__(permutation)
		self.turnover = turnover
		self.offset = offset
		self.setting = setting

	@property
	def notch(self):
		return self.turnover == self.offset

	def advance(self):
		self.offset = super().shift(self.offset, 1)

	def forward(self, letter, rev = False):
		return super().indexToLetter(super().letterToIndex(super().forward(super().indexToLetter(super().letterToIndex(letter) + super().letterToIndex(self.offset) - super().letterToIndex(self.setting)), rev)) - super().letterToIndex(self.offset) + super().letterToIndex(self.setting))

	@staticmethod
	def update(obj, offset: str, setting: str):
		obj.offset = offset
		obj.setting = setting
		
	@staticmethod
	def generateRotor(name: str, offset: str, setting: str):
		if name == 'I':
			return Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q', offset, setting)
		elif name == 'II':
			return Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E', offset, setting)
		elif name == 'III':
			return Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V', offset, setting)
		elif name == 'IV':
			return Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J', offset, setting)
		elif name == 'V':
			return Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z', offset, setting)
		else:
			print('Invalid rotor. Try again.')

	generateRotor, amountOfRotors, getRotors = memoize.memoize(generateRotor.__func__, update.__func__)
