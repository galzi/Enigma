from abc import *
import string

class Substitutor(ABC):
	@staticmethod
	def letterToIndex(letter: str):
		return (ord(letter) - ord(string.ascii_uppercase[0])) % len(string.ascii_uppercase)

	@staticmethod
	def indexToLetter(index: int):
		return chr(index % len(string.ascii_uppercase) + ord(string.ascii_uppercase[0]))

	def shift(self, currentInd: str, amount: int) -> str:
		return self.indexToLetter((self.letterToIndex(currentInd) + amount) % len(string.ascii_uppercase)) if len(currentInd) == 1 else str()

	@abstractmethod
	def forward(self, letter, rev: bool = False):
		pass

	def reverse(self, letter):
		return self.forward(letter, True)
