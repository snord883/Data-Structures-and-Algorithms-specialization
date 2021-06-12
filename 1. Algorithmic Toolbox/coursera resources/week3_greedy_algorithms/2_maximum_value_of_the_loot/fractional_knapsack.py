# Uses python3
import sys
import numpy as np

def determine_most_value_item(capacity, loot):
    # print(loot)
    weight_item_in_knapsack = min(loot[1][-1],capacity)
    # print("weight_item_in_knapsack: ", weight_item_in_knapsack)
    value_i = weight_item_in_knapsack * loot[0][-1]
    # print("value: ", value_i)
    capacity -= weight_item_in_knapsack
    # print("capacity: ", capacity)

    return value_i, capacity, loot[:,:-1]


def get_optimal_value(capacity, weights, values):
    value = 0.
    value_per_weight = np.array(values)/weights
    loot = np.array([value_per_weight,np.array(weights)])
    loot = loot[:,loot[0].argsort()]
    while capacity>0 and not np.array_equal(loot, [[], []]):
        value_i, capacity, loot = determine_most_value_item(capacity, loot)
        value += value_i
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))