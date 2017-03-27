A=[int(each) for each in input().strip().split()]

def quickSort(A,first,last):
    if first<last:
        splitPoint = partition(A,first,last)
        quickSort(A,first,splitPoint-1)
        quickSort(A,splitPoint+1,last)
    
def partition(A,first,last):
    pivotValue = A[first]
    leftMark = first+1
    rightMark = last

    done = False
    while not done:

        while leftMark <= rightMark and A[leftMark] <= pivotValue:
            leftMark = leftMark + 1

        while A[rightMark] >= pivotValue and rightMark >= leftMark:
            rightMark = rightMark -1

        if rightMark < leftMark:
            done = True

        else:
            temp = A[leftMark]
            A[leftMark] = A[rightMark]
            A[rightMark] = temp
ṇ
    temp = A[first]
    A[first] = A[rightMark]
    A[rightMark] = temp
    print(A)
    return rightMark

quickSort(A,0,len(A)-1)
print(A)
