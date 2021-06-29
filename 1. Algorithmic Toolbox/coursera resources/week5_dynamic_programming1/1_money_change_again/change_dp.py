# Uses python3
import sys

def get_change(money):
    if money ==1:
        return money
    MinNumCoins = [0 for i in range(money)]
    for m in range(1, money):
        MinNumCoins[m] = sys.maxsize
        for c in [1, 3, 4]:
            if m >= c:
                NumCoins = MinNumCoins[m - c] + 1
                if NumCoins <= MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
    
    return MinNumCoins[money-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
