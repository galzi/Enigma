from Substitutor import Substitutor
from Rotor import Rotor
from Reflector import Reflector
from Plugboard import Plugboard

from typing import Tuple
from enum import Enum
import string

class Enigma(Substitutor):
	Side = Enum('Side', [('LEFT', 0), ('MIDDLE', 1), ('RIGHT', 2)])

	def __init__(self, rotors: Tuple[Rotor, Rotor, Rotor], reflector: Reflector, plugboard: Plugboard):
		self.rotors = rotors
		self.reflector = reflector
		self.plugboard = plugboard

	def rotorStep(self):
		if self.rotors[Enigma.Side.RIGHT.value].notch or self.rotors[Enigma.Side.MIDDLE.value].notch:
			if self.rotors[Enigma.Side.MIDDLE.value].notch:
				self.rotors[Enigma.Side.LEFT.value].advance()
			self.rotors[Enigma.Side.MIDDLE.value].advance()
		self.rotors[Enigma.Side.RIGHT.value].advance()

	def translate(self, msg: str):
		translated = str()
		for letter in msg:
			self.rotorStep()
			translated += self.forward(letter)
		return translated

	def forward(self, letter, rev: bool = False):
		letter = self.plugboard.forward(letter)

		for i in list(Enigma.Side)[::-1]:
			letter = self.rotors[i.value].forward(letter)

		letter = self.reflector.forward(letter)

		for i in Enigma.Side:
			letter = self.rotors[i.value].reverse(letter)

		letter = self.plugboard.reverse(letter)
		return letter;
