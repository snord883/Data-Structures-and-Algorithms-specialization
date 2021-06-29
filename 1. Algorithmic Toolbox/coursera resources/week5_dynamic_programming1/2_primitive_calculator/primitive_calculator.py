# Uses python3
import sys

# def incorrect_optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)

# def optimal_sequence2(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif (n - 1) % 3 == 0:
#             n -= 1
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)

def optimal_sequence(n):
    MinOperations = [0] * (n + 1)
    for i in range(1, len(MinOperations)):
        MinOperations[i] = MinOperations[i-1] + 1
        if i % 2 == 0:
            MinOperations[i] = min(MinOperations[i], MinOperations[i // 2] + 1)
        if i % 3 == 0:
            MinOperations[i] = min(MinOperations[i], MinOperations[i // 3] + 1)
    
    result = [1] * MinOperations[-1]
    for i in range(1, MinOperations[-1]):
        result[-i] = n
        if MinOperations[n-1] == MinOperations[n] - 1:
            n -= 1
        elif n % 2 == 0 and (MinOperations[n // 2] == MinOperations[n] - 1):
            n //= 2
        else:
            n //= 3
    return result


input = sys.stdin.read()
n = int(input)
# print(optimal_sequence(n))
# for i in range(1,n+1):
#     sequence = list(optimal_sequence(i))
#     sequence2 = list(optimal_sequence2(i))
#     print(f"{i}: {len(sequence) - 1}\t{len(sequence2) - 1}")
sequence = list(optimal_sequence(n))
# sequence = list(optimal_sequence2(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
