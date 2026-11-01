# Python Program: Linear Search and Binary Search


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Input
arr = list(map(int, input("Enter array elements: ").split()))
key = int(input("Enter element to search: "))

# Linear Search
print("\n--- Linear Search ---")

result = linear_search(arr, key)

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found")


# Binary Search
sorted_arr = sorted(arr)

print("\n--- Binary Search ---")
print("Sorted Array:", sorted_arr)

result = binary_search(sorted_arr, key)

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found")
