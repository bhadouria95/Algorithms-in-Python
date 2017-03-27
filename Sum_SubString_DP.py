# This code will find length of subarray whose sum is equal to n in an array
# There is only one sum is possible. If the sum is possible with more then one subarray then alter the solution

def findLen(arr,num):

	for i in range(len(arr)):
		matrix[i][i] = arr[i]

	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			matrix[i][j] = matrix[i][j-1] + arr[j]

	# loc is a list that will store the location of the starting and end of subarry as a tuple
	loc = [(row, item.index(num)) for row, item in enumerate(matrix) if num in item] 
	print(loc) 
	length = loc[0][1] - loc[0][0] + 1
	
	return length

arr = [23,67,89,87,65,43,21,2,3,4,6,8]
num=9

matrix = [[0 for x in range(len(arr))] for y in range(len(arr))]

print(findLen(arr,num))