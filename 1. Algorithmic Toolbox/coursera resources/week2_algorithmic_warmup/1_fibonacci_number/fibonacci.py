# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        f0 = 0
        f1 = 1
        for _ in range(1,n):
            f0, f1 = f1, f0 + f1

        return f1

n = int(input())
print(calc_fib(n))
