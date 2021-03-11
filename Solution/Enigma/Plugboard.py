from Translator import Translator

from collections import Counter
import string, re

class Plugboard(Translator): # singleton
	def __init__(self, setting: str):
		if re.search(r'^(([A-Z]{2} )*[A-Z]{2})?$', setting) and list(filter(lambda x: x[1] != 1, Counter(setting).items())) in ([], [' ']):
			alphabet = [None] * len(string.ascii_uppercase)
			tick = [False] * len(string.ascii_uppercase)
			conf = dict((i[0], i[1]) for i in setting.split())

			if len(conf) <= 10:
				for i in string.ascii_uppercase:
					if i in conf.keys():
						alphabet[super().letterToIndex(i)], alphabet[super().letterToIndex(conf[i])] = conf[i], i
						tick[super().letterToIndex(i)], tick[super().letterToIndex(conf[i])] = True, True
					elif tick[super().letterToIndex(i)] == False:
						alphabet[super().letterToIndex(i)] = i
			super().__init__(''.join(alphabet))
		else:
			raise Exception()
