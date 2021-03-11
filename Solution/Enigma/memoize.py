def memoize(f, update = None):
	memo = dict()
	def helper(key, *args):
		if key not in memo:
			res = f(key, *args)
			if res is not None:
				memo[key] = res
		else:
			if update is not None:
				memo[key].update(*args)
		if key in memo.keys(): return memo[key]
	return helper, lambda: len(memo), lambda: list(memo.values())
