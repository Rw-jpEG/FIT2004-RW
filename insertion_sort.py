def insertion_sort(arr):
    #loop over all elements
    for i in range (len(arr)):
        key = arr[i]
        j = i-1
        #check each element in the sorted section and if arr[i] < current element, then move element forward 
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

def rev_insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = j-1
        while j>=0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        #at the end of iteration i arr[1...i] is sorted in non-increasing order

    return key