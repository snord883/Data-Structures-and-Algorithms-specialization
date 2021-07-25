# Uses python3
import sys

def optimal_weight(capcity, N, W):
    results = [[0 for _ in range(capcity + 1)] for _ in range(len(W) + 1)]
    for r in range(1, len(W) + 1):
        for c in range(1, capcity + 1):
            w = W[r-1]
            results[r][c] = results[r-1][c]
            if w <= c:
                results[r][c] = max(results[r-1][c-w]+w, results[r-1][c])

    return results[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    capcity, N, *W = list(map(int, input.split()))
    print(optimal_weight(capcity, N, W))
