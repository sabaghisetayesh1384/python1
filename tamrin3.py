def sort1(A):
    B = [] *len(A)
    for i in range(len(A)):
        for j in range(1 , len(A)):
            if A[j] < min:
                min = A[j]
                k = j
        B[i] = min
        A[k] = float("inf")
    return B 
def Bubble(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1] , A[j]

sort1: Selection sort variant. Finds min, moves to B, marks as inf in A.
Bubble: Bubble sort. Swaps adjacent items if out of order.