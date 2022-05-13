# Write a function called sumZero that takes a list of numbers
# The function should return a list of pairs of indices where the sum is 0
# If not, the function should return undefined

def sumZero(lst):
    lst2 = []
    
    for i in lst:
        for j in reversed(lst):
            if (i + j == 0):
                lst2.append([i, j])
                return lst2
            else:
                return "undefined"

print(sumZero([-4, -3, -2, -1, 0, 1, 2, 3, 4]))
print(sumZero([-3, -2, -1, 0, 1, 2]))