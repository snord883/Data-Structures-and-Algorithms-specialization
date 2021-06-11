# Uses python3
import sys
import numpy as np

def get_fibonacci(n):
    # print(n)
    i_matrix = np.array([[1, 1], [1, 0]], dtype=object).reshape(2,2)
    matrix_n = np.linalg.matrix_power(i_matrix,n)

    return matrix_n[1][0]

def get_last_digit_of_sum_of_fibonaccis(n):
    sum = 0
    mods = []
    for i in range(n):
        sum += get_fibonacci(i)
        mods.append(sum%10)

    return mods

def get_mod_of_sum(n):
    last_digit_pattern = [
        0, 1, 2, 4, 7, 2, 0, 3, 4, 8,
        3, 2, 6, 9, 6, 6, 3, 0, 4, 5,
        0, 6, 7, 4, 2, 7, 0, 8, 9, 8,
        8, 7, 6, 4, 1, 6, 8, 5, 4, 0,
        5, 6, 2, 9, 2, 2, 5, 8, 4, 3,
        8, 2, 1, 4, 6, 1, 8, 0, 9, 0
    ]
    
    return last_digit_pattern[n % 60]

def get_solution(m, n):
    n_mod = get_mod_of_sum(n)
    m_mod = get_mod_of_sum(m - 1) if m>0 else 0

    diff_mod = n_mod - m_mod
    if diff_mod>=0:
        return n_mod - m_mod
    else:
        return 10 + diff_mod

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_solution(n, m))
