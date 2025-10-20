def countinversions(arr, l, r):
    if l is None:
        l = 0
    
    if r is None:
        r = len(arr) - 1

    res = 0
    if l<r:
        m = (l+r)//2
    
        res += countinversions(arr, l, m)
        res += countinversions(arr, m+1, r)

        res += countinginversionhelper(arr, l, r, m)
    
    return res


def countinginversionhelper(arr, l, r, mid):
    if mid is None:
        left = 0
        right = len(arr)
        mid = (left + right)//2

    n1 = mid - l + 1
    n2 = r - mid

    left = arr[l:mid + 1]
    right = arr[mid+1:r+1]

    res = 0
    i = 0
    j = 0
    k = l

    while i<n1 and j<n2:
        #if left has a smaller or equal element
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            #if right has a smaller element then add the inversions to count
            arr[k] = right[j]
            j += 1
            res += (n1-i)
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
    
    return res


