from Translator import Translator

import string, memoize

class Reflector(Translator):
	def __init__(self, permutation: str):
		super().__init__(permutation)

	@staticmethod
	def generateReflector(name: str):
		if name == 'B':
			return Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
		else:
			print('Invalid reflector. Try again.')

	generateReflector, amountOfReflectors, getReflectors = memoize.memoize(generateReflector.__func__)
