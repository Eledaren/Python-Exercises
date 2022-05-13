# Write a function that takes a list of numbers and an average number.
# Determine if two numbers in the list are within the average.
# It must return true the sum of the two numbers is equal to the average.

def Average(list, avg):
    for i in list:
        for j in reversed(list):
            if i < avg and j > avg:
                average = (i + j) / 2
                if average == avg:
                    return True
                
print(Average([1, 2, 3, 4, 5], 3))
print(Average([1, 2, 3, 4, 5], 4))
print(Average([1, 2, 3, 4, 5], 5))