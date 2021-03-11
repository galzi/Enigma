from Substitutor import Substitutor

import string

class Translator(Substitutor):
	def __init__(self, permutation: str):
		if set(permutation) == set(string.ascii_uppercase) and len(permutation) == len(string.ascii_uppercase):
			self.alphabet = [None] * len(string.ascii_uppercase)
			for i, j in zip(string.ascii_uppercase, range(0, len(string.ascii_uppercase))):
				self.alphabet[super().letterToIndex(i)] = permutation[j]

			self.revalphabet = [None] * len(self.alphabet)
			for i in range(len(self.alphabet)):
				self.revalphabet[super().letterToIndex(self.alphabet[i])] = super().indexToLetter(i)
		else:
			raise Exception()

	def forward(self, letter, rev: bool = False):
		return self.alphabet[super().letterToIndex(letter)] if not rev else self.revalphabet[super().letterToIndex(letter)]
