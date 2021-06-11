# Uses python3
import sys
import numpy as np

def get_fibonacci_last_digit_naive(n):
    i_matrix = np.array([[1, 1], [1, 0]], dtype=object)
    matrix_n = np.linalg.matrix_power(i_matrix,n)

    return matrix_n[1][0] % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
