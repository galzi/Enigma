from Rotor import Rotor
from Reflector import Reflector
from Plugboard import Plugboard
from Enigma import Enigma

import string

def insert(amountChecker, amount, generator, msg, inputReq):
	inp = lambda: [input(i) for i in inputReq]

	while amountChecker() < amount:
		test = amountChecker()
		if generator(*(inp())) is not None:
			if amountChecker() == test:
				print('This {0} was already chosen. Try again.'.format(msg))


print('Choose Rotors (I, II, III, IV, V)')
insert(Rotor.amountOfRotors, 3, Rotor.generateRotor, 'rotor', ('Rotor name: ', 'Rotor offset: ', 'Rotor setting: '))

print('Choose Reflector (B)')
insert(Reflector.amountOfReflectors, 1, Reflector.generateReflector, 'reflector', ('Reflector name: ', ))

while True:
	try:
		pb = Plugboard(input('Plugboard Configuration: '))
		break
	except Exception as e:
		print('Invalid format. Try again.')

enigma = Enigma(Rotor.getRotors(), Reflector.getReflectors()[0], pb) # order of rotors is order of entrance

msg = str()
f = True
while f or not set(msg) <= set(string.ascii_uppercase):
	f = False
	msg = input('Enter message: ')
print(enigma.translate(msg))

print('Final Offset: {0}'.format('-'.join([i.offset for i in Rotor.getRotors()])))
