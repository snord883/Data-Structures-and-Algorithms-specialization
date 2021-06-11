# Uses python3
import sys
import numpy as np

def get_fibonacci(n):
    # print(n)
    i_matrix = np.array([[1, 1], [1, 0]], dtype=object).reshape(2,2)
    matrix_n = np.linalg.matrix_power(i_matrix,n)

    return matrix_n[1][0]

def get_last_digit_of_sum_of_fibonaccis_squared(n):
    sum = 0
    mods = []
    for i in range(n):
        sum += get_fibonacci(i)**2
        mods.append(sum%10)

    return mods

def get_solution(n):
    last_digit_pattern = [
        0, 1, 2, 6, 5, 0, 4, 3, 4, 0,
        5, 6, 2, 1, 0, 0, 9, 8, 4, 5,
        0, 6, 7, 6, 0, 5, 4, 8, 9, 0
    ]
    
    return last_digit_pattern[n % 30]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_solution(n))
