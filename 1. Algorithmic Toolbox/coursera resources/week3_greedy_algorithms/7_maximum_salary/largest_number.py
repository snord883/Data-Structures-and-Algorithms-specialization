#Uses python3
import functools

import sys

def compare(x, y):
    xy = "".join([x,y])
    yx = "".join([y,x])
    if xy < yx:
        return -1
    elif xy > yx:
        return 1
    else:
        return 0

def largest_number(A):
    A.sort(key=functools.cmp_to_key(compare), reverse=True)
                
    return "".join(A)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
