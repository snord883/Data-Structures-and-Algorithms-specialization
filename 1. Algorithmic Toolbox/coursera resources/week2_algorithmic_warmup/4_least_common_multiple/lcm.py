# Uses python3
import sys

# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l

#     return a*b

def lcm_euclid(a, b):
    return a*b // gcd_euclid(a, b)

def gcd_euclid(a, b):
    while b > 0:
        a, b = b, a % b

    return a

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_euclid(a, b))

