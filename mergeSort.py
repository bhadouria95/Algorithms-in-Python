# -*- coding: utf-8 -*-
from __future__ import unicode_literals
def mergeSort(A):
    
    if len(A)>1:
        mid = len(A)//2
        leftA = A[:mid]
        rightA = A[mid:]

        mergeSort(leftA)
        mergeSort(rightA)

        i,j,k=0,0,0
        
        while i < len(leftA) and j < len(rightA):
            if leftA[i] < rightA[j]:
                A[k] = leftA[i]
                i += 1
            else:
                A[k] = rightA[j]
                j += 1
            k += 1

        while i < len(leftA):
            A[k] = leftA[i]
            i += 1
            k += 1 

        while j < len(rightA):
            A[k] = rightA[j]
            j += 1
            k += 1

A = [int(each) for each in input().strip().split(' ')]
mergeSort(A)
print(A)
