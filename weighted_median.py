
from k_closest_median import Quickselect


def weighted_median(arr):
    if len(arr)==1:
        return arr[0]
    
    Pivot = Quickselect(arr, len(arr)//2, key = lambda t: t[0]) #should be approximate median
    pivot_val, pivot_weight = Pivot 

    lt_pivot = []
    gt_pivot = []
    left_sum = 0
    right_sum = 0

    for val, weight in arr:
        if val < pivot_val:
            lt_pivot.append((val, weight))
            left_sum += weight
        elif val > pivot_val:
            gt_pivot.append((val, weight))
            right_sum += weight
    
    if left_sum < 0.5 <= left_sum + pivot_weight:
        return Pivot
    elif left_sum >= 0.5:
        return weighted_median(lt_pivot)
    else:
        return weighted_median(gt_pivot)

arr = [(1, 0.1), (2, 0.2), (3, 0.4), (4, 0.3)]
print(weighted_median(arr))

