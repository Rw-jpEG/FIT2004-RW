import random

def Quickselect(arr, k, key=lambda x: x):
    if not arr:
        raise ValueError("Quickselect called with empty array")
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)

    lows = [x for x in arr if key(x) < key(pivot)]
    pivots = [x for x in arr if key(x) == key(pivot)]
    highs = [x for x in arr if key(x) > key(pivot)]

    if k < len(lows):
        return Quickselect(lows, k, key)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return Quickselect(highs, k - len(lows) - len(pivots), key)





def k_closest_median(arr, k):
    median_k = len(arr)//2

    median = Quickselect(arr, median_k)

    dist_from_med = [(x,abs(x-median)) for x in arr]

    kth_pair = Quickselect(dist_from_med, k-1, key=lambda t: t[1])
    threshold = kth_pair[1]

    result = [x for x, d in dist_from_med if d <= threshold]

    return result[:k]

arr = [1, 3, 7, 8, 2, 5, 10]
print(k_closest_median(arr, 3))