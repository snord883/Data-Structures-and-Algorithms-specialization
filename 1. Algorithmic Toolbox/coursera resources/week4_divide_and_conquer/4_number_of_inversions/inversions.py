# Uses python3
import sys

number_of_inversions = 0

def merge_sort(arr):
    global number_of_inversions
    if len(arr) > 1:
        mid = len(arr)//2
        B = arr[:mid]
        C = arr[mid:]
        merge_sort(B) 
        merge_sort(C)

        b = c = i = 0
        # B [9, 8, 7]
        # C [3, 2, 1]
        while b < len(B) and c < len(C):
            if B[b] <= C[c]:
                arr[i] = B[b]
                b += 1
            else:
                arr[i] = C[c]
                c += 1
                number_of_inversions += len(B) - b
            i += 1

        while b < len(B):
            arr[i] = B[b]
            b += 1
            i += 1

        while c < len(C):
            arr[i] = C[c]
            c += 1
            i += 1

    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(merge_sort(a))

