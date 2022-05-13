#Create 2 arrays with the same length.
#The function will return True if the square of each element in the first array is equal to the element in the second array.
#If not, the function will return False.

def main(array1, array2):
    for i in array1:
        for j in array2:
            if i == j ** 2:
                return True
            else:
                return False

while True:
    try:
        lengthArrays = int(input("\nEnter the length of the arrays: "))
        break
    except ValueError:
        print("Input Error - Enter a number")

array1 = []
array2 = []

for i in range(lengthArrays):
    array1.append(int(input(f"\nEnter a number value of the index {i} of the first array: ")))
    array2.append(int(input(f"Enter a number value of the index {i} of the second array: ")))

print(main(array1, array2))