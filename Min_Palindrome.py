# Python program to find the minimum number of palindrome in the given string,
a = "ababbbabbababa"

def splitRecursion(x):
	if len(x) <= 1 or isPalindrome(x) :
		print(x)
		return 0
	else:
		cuts = len(x);
		for i in range(len(x)):
			cuts = min(1 + splitRecursion(x[0:i]) + splitRecursion(x[i:len(x)]))
		return cuts

def isPalindrome(s):
	n = len(s)
	if n % 2 == 0:
		if a[0:(n/2)] == a[(n/2)+1:len(s)]:
			return True
		else:
			return False
	else:
		if a[0:(n-1)/2] == a[((n+1)/2)+1:len(s)]:
			return True
		else:
			return False
sol_list = []
sol_list.append(splitRecursion(a))
print(sol_list)
