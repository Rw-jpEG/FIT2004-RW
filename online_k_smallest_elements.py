from max_heap import MaxHeap

def smallest_k_online(arr, k, e):
    #assume e is some new element to be added to arr
    heap = MaxHeap()
    
    for element in arr:
        heap.insert(element)

    for element in range(1, len(heap)-k):
        heap.extractMax()

    if e:
        if len(heap)<k:
            heap.push(e)
        elif e<heap.getMax():
            heap.extractMax()
            heap.insert(e)
    return heap

    

