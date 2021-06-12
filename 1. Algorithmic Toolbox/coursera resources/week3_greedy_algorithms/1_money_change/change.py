# Uses python3
import sys

def get_change(m):
    coins_10, r = get_coins_and_remainder(m, 10)
    coins_5, r = get_coins_and_remainder(r, 5)
    return coins_10 + coins_5 + r

def get_coins_and_remainder(m, c):
    return m // c, m % c


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
