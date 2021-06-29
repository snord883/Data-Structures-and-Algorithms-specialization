import numpy as np

# Uses python3
def edit_distance(s, t):
    a = np.zeros(shape=(len(s)+1,len(t)+1))
    a[0:] = range(len(t)+1)
    for r in range(1, len(s)+1):
        for c in range(len(t)+1):
            if c == 0:
                a[r][c] = a[r - 1][c] + 1
            elif s[r-1] == t[c-1]:
                a[r][c] = a[r - 1][c - 1]
            else:
                a[r][c] = min(a[r][c - 1], a[r-1][c], a[r-1][c-1]) + 1


    return int(a[-1][-1])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
