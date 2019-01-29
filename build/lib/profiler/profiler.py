import cProfile, pstats, io

def profiler(func):
	def wrapper(*args, **kwargs):
		pr = cProfile.Profile()
		pr.enable()
		res = func(*args, **kwargs)
		pr.disable()
		s = io.StringIO()
		sortby = 'cumulative'
		ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
		ps.print_stats()
		pr.print_stats()
		print(s.getvalue())
		return res

	return wrapper

