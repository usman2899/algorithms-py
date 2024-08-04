for i in range (1, 100):
    a = "";
    if i % 3 == 0:
        a += "Fizz"
    if i % 5 == 0:
        a += "Buzz"
    print(f"{i}: {a}");