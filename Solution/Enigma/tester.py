from Rotor import Rotor
from Reflector import Reflector
from Plugboard import Plugboard
from Enigma import Enigma

import cProfile

def test():
	for i in range(1000):
		Enigma([Rotor.generateRotor('II', 'C', 'S'), Rotor.generateRotor('V', 'O', 'I'), Rotor.generateRotor('IV', 'N', 'X')], Reflector.generateReflector('B'), Plugboard('ZU HL CQ WM OA PY EB TR DN VI')).translate('DOR')

cProfile.run('test()')
