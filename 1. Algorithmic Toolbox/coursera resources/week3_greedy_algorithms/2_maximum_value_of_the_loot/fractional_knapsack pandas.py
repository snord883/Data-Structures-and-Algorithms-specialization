# Uses python3
import sys
import pandas as pd
import numpy as np

def get_optimal_value(capacity, weights, values):
    value = 0.
    value_per_weight = np.array(values)/weights
    loot = pd.DataFrame({"weights": np.array(weights), "value_per_weight": value_per_weight})
    loot.sort_values(by=["value_per_weight"], ascending=False, inplace=True)
    # print("LOOT: ", loot)
    for index, row in loot.iterrows():
        weight_item_in_knapsack = min(row.weights,capacity)
        # print("weight_item_in_knapsack: ", weight_item_in_knapsack)
        value += weight_item_in_knapsack * row.value_per_weight
        # print("value: ", value)
        capacity -= weight_item_in_knapsack
        # print("capacity: ", capacity)
        if capacity==0:
            return value
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
