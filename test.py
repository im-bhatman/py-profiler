from profiler.profiler import profiler


@profiler
def main():
	total_sum = 0
	for i in range(0, 100000000):
		total_sum
	print("total :: ", total_sum)
	return total_sum


if __name__ == '__main__':
	main()
