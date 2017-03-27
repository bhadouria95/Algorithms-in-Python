# This program will print the matrix in spiral order

spiral = []
def printSpiral(matrix, r, c):

	lt_col = 0
	rt_col = c - 1
	up_row = 0
	dn_row = r - 1
	
	while len(spiral) != r*c:

		#Prints uper row in serial corder
		for i in range(lt_col,rt_col+1):
			spiral.append(matrix[up_row][i])
		up_row += 1

		#Prints the last column in downword order
		for i in range(up_row,dn_row+1):
			spiral.append(matrix[i][rt_col])
		rt_col -= 1

		#Prints the last row in reverse order	
		for i in range(rt_col,lt_col-1,-1):
			spiral.append(matrix[dn_row][i])
		dn_row -= 1

		#Prints the first column in upper rising order
		for i in range(dn_row,up_row-1,-1):
			spiral.append(matrix[i][lt_col])
		lt_col += 1
	
	return spiral

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
R = 5 #Number of rows
C = 5 #Number of columns 
print(printSpiral(matrix,R,C))