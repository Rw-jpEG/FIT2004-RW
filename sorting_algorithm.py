def mergesort(x, lo, hi):

    if lo<hi:
        mid = lo + (hi-lo)//2
        mergesort(lo, x[:mid])
        mergesort(x[mid+1:], hi)
        merge(x, lo, mid, hi)

def merge(x, lo, mid, hi):
    n1 = mid - lo+1
    n2 = hi - mid

    Left = x[lo:mid+1]
    Right = x[mid+1:hi+1]

    i = 0
    j = 0
    k = lo

    while i<len(Left) and j<len(Right):
        if Left[i] < Right[j]:
            x[k] = Left[i]
            i += 1
        else:
            x[k] = Right[j]
            j += 1
        k += 1

    while i<len(Left):
        x[k] = Left[i]
        i += 1
        k+= 1

    while j<len:
        x[k] = Right[j]
        j+=1
        k+=1



def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        sorted = i-1

    while sorted >= 0 and key < arr[sorted]:
        #TODO
        pass