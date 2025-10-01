def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    else:
        pivot = arr[len(arr) // 2]   
        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + mid + quicksort(right)
    
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x<pivot]
        right = [x for x in arr if x>pivot]
        mid = [x for x in arr if x==pivot]
    return quicksort(left) + mid + quicksort(right)

def quickselect(arr, k):
    if len(arr)<=1:
        return arr
    
    else:
        pivot = arr[len(arr) // 2]
        if k == pivot:
            return pivot
        elif k<pivot:
            left = [x for x in arr if x<pivot]
            return quickselect(left)
        else:
            right = [x for x in arr if x>pivot]
            return quickselect(right)


def Quickselect(L, x):
    lo = 0
    high = len[L]
    mid = lo + (high-lo)//2

    if high>lo:
        pivot = L[lo]
        smaller, greater = Partition(L, pivot)
        if x < mid:
            return Quickselect(smaller, x)
        elif x > mid:
            return Quickselect(greater, x)
        else:
            return L[x]
    else:
        return L[x]
    
def Partition(ar, pivot):
    
        mid = len(ar)//2
        right = len(ar)
        left = 0
        pivot_value = ar[mid]

        lo, pivot = pivot, lo

        smaller, greater = [],[]

        for value in ar:
            if value <= pivot:
                left += 1
                smaller.append(value)
            if value > pivot:
                right -= 1
                greater.append(value)

            return smaller, greater