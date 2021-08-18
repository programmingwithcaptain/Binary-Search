# Iterative Binary Search

def binary_search(my_array, x):
    low = 0
    high = len(my_array) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if my_array[mid] < x:
            low = mid + 1
        elif my_array[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


my_array = [2, 4, 5, 8, 9]
x = int(input("Enter the element of array: "))

result = binary_search(my_array, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
