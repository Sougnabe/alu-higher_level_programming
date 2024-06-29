#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numerator = sum(score * weight for score, weight in my_list)
    denominator = sum(weight for _, weight in my_list)

    return numerator / denominator if denominator != 0 else 0

# Test the function
result = weight_average([(10, 2), (20, 1), (30, 3)])  # Example: should return the numeric value
print("Av: {:0.2f}".format(result))  # Format the result to two decimal places

result = weight_average([])  # Example: should return 0
print("Av: {:0.2f}".format(result))  # Format the result to two decimal places
