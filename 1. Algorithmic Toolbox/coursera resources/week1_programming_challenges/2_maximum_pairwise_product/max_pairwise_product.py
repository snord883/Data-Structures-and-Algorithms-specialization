# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_1 = -1
    max_2 = -1
    for n in numbers:
        if n > max_1:
            max_2 = max_1
            max_1 = n
        elif n > max_2:
            max_2 = n

    return max_1 * max_2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
