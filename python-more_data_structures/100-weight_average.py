#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numerator = sum(score * weight for score, weight in my_list)
    denominator = sum(weight for _, weight in my_list)

    return numerator / denominator if denominator != 0 else 0

# Test cases
print("Av: {:0.2f}".format(weight_average([(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)])))  # Expected: Av: 3.00
print("Av: {:0.2f}".format(weight_average([(1, 1), (2, 2)])))  # Expected: Av: 1.67
print("Av: {:0.2f}".format(weight_average([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])))  # Expected: Av: 3.67
print("Av: {:0.2f}".format(weight_average([(1, 10), (10, 1)])))  # Expected: Av: 1.82
print("Av: {:0.2f}".format(weight_average([(1, 2)])))  # Expected: Av: 1.00
print("Av: {:0.2f}".format(weight_average([])))  # Expected: Av: 0.00
