from heapq import heapify


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    
    L = [0] * n1
    R = [0] * n2

    
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = left  

    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)
    return arr



def heap_sort(arr):

    for i in range(len(arr)-1, -1, -1):
        heapify(arr)

    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr)

    return arr
    


def remove_duplicates(arr):
    if not arr:
        return arr
    
    j = 0  
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    return arr[:j+1]



def remove_duplicate(arr):
    sorted_array = heap_sort(arr)

    if not arr:
        return arr
    
    j = 1
    for i in range(2, len(sorted_array)):
        if sorted_array[i] != sorted_array[i-1]:
            j += 1
            sorted_array[j] = sorted_array[i]

    del sorted_array[j:len(sorted_array)]
    return sorted_array
            



if __name__ == "__main__":
    my_list = [0,0,5,7,4,3,6,5,8,32,45,6,4,3,2,3]
    sorted_list = heap_sort(my_list)
    unique_list = remove_duplicates(sorted_list)
    print("Sorted:", sorted_list)
    print("Unique:", unique_list)