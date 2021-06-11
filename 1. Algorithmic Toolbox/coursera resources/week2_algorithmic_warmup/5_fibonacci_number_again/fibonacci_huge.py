# Uses python3
import numpy as np
import sys
from functools import lru_cache
# from numpy.lib.shape_base import tile
# import pandas as pd
# import timeit

# from numpy.lib.function_base import average

@lru_cache(maxsize=1000)
def get_fibonacci_mod(n, m):
    # print(n)
    i_matrix = np.array([[1, 1], [1, 0]], dtype=object).reshape(2,2)
    matrix_n = np.linalg.matrix_power(i_matrix,n)

    return matrix_n[1][0] % m

def get_mod_pattern(n, m):
    mod_pattern = {
        0: 0,
        1: 1,
        2: 1
    }
    if n<3:
        return mod_pattern
    else:
        for f in range(3,n):
            mod_pattern[f] = get_fibonacci_mod(f, m)
            if mod_pattern[f-1]==0 and mod_pattern[f]==1:
                mod_pattern.pop(f)
                mod_pattern.pop(f-1)
                return mod_pattern
        return mod_pattern

def time_function():
    SETUP_CODE = '''
from __main__ import get_fibonacci_huge
import numpy as np'''
    for n in [1,10,100,1000,10000,100000]:
        my_code =f'get_fibonacci_huge({n}, 239)'
        times = timeit.repeat(setup=SETUP_CODE, stmt=my_code, number=10)
        print('{}: {}'.format(n,average(times)))  

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    # time_function()
    if m>=n:
        print(get_fibonacci_mod(n,m))
    else:
        mod_pattern = get_mod_pattern(n, m)
        print(mod_pattern[n % len(mod_pattern)])
        # print(mod_pattern)
        # print(len(mod_pattern))
    # print("done")
    

# def get_fib_mod_table(n, m):
#     inds = range(2, m+1)
#     fibs = [get_fibonacci_huge(fib) for fib in range(n+1)]
#     mods = [get_mods(fibs, mod) for mod in inds] 
#     df = pd.DataFrame(data=mods, columns=fibs, index=inds)
#     return df


# def get_mods(fibs, m):
#     return [f%m for f in fibs]