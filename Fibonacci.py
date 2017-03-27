# This program compute fibonnaci series using naive recursion algorithm (uses polynomial time complexity)
import time

start_time = time.clock()

def fib(n):
	if n <= 2:
		f = 1
	else:
		f = fib(n-1) + fib(n-2)
	return f

n = 100
time = time.clock() - start_time
print(time)
