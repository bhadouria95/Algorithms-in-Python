# Dynamic approach for Palindrome Partitioning Problem
import pprint
pp = pprint.PrettyPrinter()

def minPalPartition(A):
	n = len(A)

	#min number of cuts needed for the palindrome pattitioning of substring str[i:j]
	C = [n]*n
	
	#true if substring str[i:j] is palindrome, else false
	P = [[True for i in range(n)] for j in range(n)]    
	
	# Note that C[i][j] is 0 if P[i][j] is true
	for L in range(2,n+1):
		
		for i in range(n-L+1):
			
			j = i + L - 1
			
			if L == 2:
				P[i][j] = (A[i] == A[j])

			else:
				P[i][j] = ((A[i] == A[j]) and P[i+1][j-1])			
	
	for i in range(n):
		if P[0][i] == True:
			C[i] = 0
		else:
			C[i] = n
			for j in range(i):
				if P[j+1][i] == True and (1 + C[j]) < C[i]:
					C[i] = 1 + C[j]
					
	#pp.pprint(P)
	#pp.pprint(C)
	return C[n-1]

A = "civicacaramanamaracacammacdeified"
print("Min Cuts : "+str(minPalPartition(A)))