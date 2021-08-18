# Recursive Binary Search

def binary_search(my_array, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if my_array[mid] == x:
            return mid

        elif my_array[mid] > x:
            return binary_search(my_array, low, mid - 1, x)

        else:
            return binary_search(my_array, mid + 1, high, x)

    else:
        return -1


my_array = [2, 3, 4, 10, 40]
x = int(input("Enter the element of array: "))

result = binary_search(my_array, 0, len(my_array) - 1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
