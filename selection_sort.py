# def selection_sort(xs):
#     for i in range (0, len(xs)):
#         smallest_num= xs[i]
#         smaleest_index = i
#         for j in range(i+1, len(xs)):
#             if xs[j] < smallest_num:
#                 smallest_num = xs[j]
#                 smaleest_index = j
#         temp = xs[i]
#         xs[i] = smallest_num
#         xs[smaleest_index] = temp

# Bit improv code
def selection_sort(xs):
    for i in range (0, len(xs)):
        smallest_index = i
        for j in range(i+1, len(xs)):
            if xs[j] < xs[smallest_index]:
                smallest_index = j
        xs[i], xs[smallest_index] = xs[smallest_index], xs[i]



xs = [3, 2, 1, 5, 4]
print(xs)
selection_sort(xs)
print(xs)

# A nice Pythonic way to check  a list is sorted
# without relying on using Python's own sorting methods to compare.
print(all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1)))