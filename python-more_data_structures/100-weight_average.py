#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return "Av: 0.00"

    numerator = sum(score * weight for score, weight in my_list)
    denominator = sum(weight for _, weight in my_list)

    average = numerator / denominator if denominator != 0 else 0
    return f"Av: {average:.2f}"

# Test the function
print(weight_average([(10, 2), (20, 1), (30, 3)]))  # Output: Av: 20.00
print(weight_average([]))  # Output: Av: 0.00
