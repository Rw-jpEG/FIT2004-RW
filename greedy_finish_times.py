import heapq

def supercomputer(times):

    heapq.heapify(times[1])
    result = []

    for time in times:
        f = times.pop()
        if len(result) == 0:
            result.append(f)
        if f[0] > result[len(result)][0]:
            result.append(f)
        else:
            continue 
    
    return result 
