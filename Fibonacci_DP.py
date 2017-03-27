# This program computes Fibonacci series using Dynamic Programming (uses linear time complexity)
import time

start_time = time.clock()

f = 0
memo = {}
def fib(n):
	if n in memo:
		return memo[n]
	elif n <=2:
		f = 1
	else:
		f = fib(n-1) + fib(n-2)
	memo[n] = f
	return f
n = 100
fib(n)
time = time.clock() - start_time
print(time)
