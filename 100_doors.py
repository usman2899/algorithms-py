# By myself
doors = [False] * 101
i = 1;
while (i <= 100):
    num = i
    while (num <= 100):
        if (doors[num] == False):
            doors[num] = True
        else:
            doors[num] = False
        num += i
    i += 1
print(doors)
print("\n")

# Mine with help, solution also done like this
doors = [False] * 101
for i in range(1, 101):
    for j in range(i, 101, i):
        doors[j] = not doors[j]
print(doors)