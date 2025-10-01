def merge_k (k) -> list:
    result = []
    mid = len(k)//2

    if len(k) == 1:
        return k[0]

    if len(k) == 2:
        return merge(k[0], k[1])

    left = k[:mid]
    right = k[mid+1:]

    merge_k(left)
    merge_k(right)

    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    
    Parameters:
        left (list): Sorted list
        right (list): Sorted list

    Returns:
        list: Merged sorted list
    """
    merged = []
    i = 0  # pointer for left
    j = 0  # pointer for right

    # Merge while both lists have elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged
    
    

#Q8

def insertion_sort(list1):
    for i in range(1, len(list1)-1):
        temp = list1[i]
        j = i-1
        while j >= 0 and temp < list1[i]:
            list1[j + 1] = list1[j]
            j-=1
            list1[j+1] = temp
        return list1



def find_max(x):
    for i in x:
        max = x[i]
        if x[i+1]>max:
            max = x[i+1]
        else:
            max = x[i]


#Q9
def binary_search(arr, x):
    lo = 0
    hi = len(arr) - 1 
    while lo<= hi:
        mid = lo + (hi-lo)//2

        if arr[mid] == x:
            retval = mid
        
        elif arr[mid] > x:
            lo = mid + 1

        elif arr[mid] < x:
            hi = mid
        else:
            return ValueError('item not in array')
    return retval

def binary_search(arr, x):
    lo = 0
    hi = len(arr) - 1 
    while lo<= hi:
        mid = lo + (hi-lo)//2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            lo = mid + 1

        elif arr[mid] < x:
            hi = mid
        else:
            return ValueError('item not in array')

#Q10

def find_a_of_i(arr):
    lo = 0
    hi = len(arr) - 1 
    while lo<= hi:
        mid = lo + (hi-lo)//2

        if arr[mid] == mid:
            return mid
        
        elif arr[mid] > mid:
            lo = mid + 1

        elif arr[mid] < mid:
            hi = mid
        else:
            return ValueError('item not in array')   