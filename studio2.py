#fibonacci using Q2b
matrix = {0: 0, 1: 1}

def fib1 (n):
    """computes the nth fibonacci number using matrix multiplication which is faster than the naive fibonacci sequence"""

    if n < 0:
        raise ValueError('n must be a positive integer')
    if n in matrix:
        return matrix[n]
    
    if n%2 == 0:
        k = n//2
        fk = fib1(k)
        fk_plus_1 = fib1(k+1)
        result = fk*(2*(fk_plus_1)-(fk))
        matrix[n] = result
        return result
    
    else:
        k = (n-1)//2
        fk = fib1(k)
        fk_plus_1 = fib1(k+1)
        result = (fk_plus_1*fk_plus_1) + (fk*fk)
