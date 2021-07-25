# Uses python3
import sys
import itertools

# def partition3(A, mark):
#     # return len([c for c in itertools.product(range(3), repeat=len(A))])
#     for c in itertools.product(range(3), repeat=len(A)):
#         sums = [None] * 3
#         for i in range(3):
#             sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)
#             if not sums[i] == mark:
#                 break

#         if sums[0] == sums[1] and sums[1] == sums[2]:
#             return 1

#     return 0

def partition(even_divide, N, W):
    # def optimal_weight(capcity, N, W):
    count = 0
    results = [[0 for _ in range(even_divide + 1)] for _ in range(N + 1)]
    for r in range(1, N + 1):
        for c in range(1, even_divide + 1):
            w = W[r-1]
            results[r][c] = results[r-1][c]
            if w <= c:
                results[r][c] = max(results[r-1][c-w]+w, results[r-1][c])
            if results[r][c] == even_divide:
                count += 1
                if count == 3:
                    return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    if n < 3 or not sum(A)%3 == 0:
        print(0)
    else:
        print(partition(sum(A)//3, n, A))

