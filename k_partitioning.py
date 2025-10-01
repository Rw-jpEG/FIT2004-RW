from quicksort import quicksort

def k_partitioning(arr, pivot_list):
    quicksort(pivot_list)

    j = 1

    for i in range(0, len(pivot_list)):
        j = hoare_partition(arr[j:], pivot_list[i]) + 1




def hoare_partition(arr, pivot):
    pivot = (len(arr))//2
    i = 0
    j = len(arr)

    arr[i], arr[pivot] = arr[pivot], arr[i]

    for i in arr:
        while arr[i] < pivot:
            i += 1
        
        while arr[j] > pivot:
            j += 1

        if i >= j:
            arr[pivot], arr[j] = arr[j], arr[pivot]
        arr[i], arr[j] = arr[j], arr[i]


