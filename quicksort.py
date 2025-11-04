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

def weighted_median(arr):
    lo = 0
    hi = len(arr)
    mid = lo + (hi-lo)//2

    pivot = quickselect(arr, mid)
    pivot_val, pivot_weight = pivot

    lt_pivot, gt_pivot = Partition(arr, pivot_val)
    lt_sum = 0
    gt_sum = 0

    for _, weight in lt_pivot:
        lt_sum += weight
    if lt_sum < 0.5:
        return weighted_median(gt_pivot)
    elif lt_sum > 0.5:
        return weighted_median(lt_pivot)
    else:
        return pivot_val





    

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