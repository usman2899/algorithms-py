import random


def binary_search(data, target):
    start = 0
    end = len(data) - 1
    while (start <= end):
        middle = (end + start) // 2
        print(middle)
        value = data[middle]
        if (value == target):
            return middle
        elif value < target:
            start = middle + 1
        else:
            end = middle - 1
    return -1



n = 10
max_val = 100
data = [random.randint(1, max_val) for i in range(n)]
data.sort()
print("Data:", data)
target = int(input("Enter target value: "))
target_pos = binary_search(data, target)
if target_pos == -1:
    print("Your target value is not in the list.")
else:
    print("You target value has been found at index", target_pos)