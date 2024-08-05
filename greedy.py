# Me
def make_change(target_amount):
    coins = 0;
    while target_amount > 0:
        if target_amount >= 200:
            target_amount -= 200
            coins += 1
        elif target_amount >= 100:
            target_amount -= 100
            coins += 1
        elif target_amount >= 50:
            target_amount -= 50
            coins += 1
        elif target_amount >= 20:
            target_amount -= 20
            coins += 1
        elif target_amount >= 10:
            target_amount -= 10
            coins += 1
        elif target_amount >= 5:
            target_amount -= 5
            coins += 1
        elif target_amount >= 2:
            target_amount -= 2
            coins += 1
        else:
            target_amount -= 1
            coins += 1
    return coins

# Solution
def make_change(target_amount):
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]  # Order is important!
    coin_count = 0  # Initialise count
    values = []  # Store values here
    for coin in denominations:
        while target_amount >= coin:  # Use the current coin until its value is too large
            target_amount -= coin  # Decrease the remaining amount
            values.append(coin)  # Make a note of which coin was used
            coin_count += 1  # Increase the coin count
    return coin_count, values


print(make_change(24))  # 3: 20p + 2p + 2p
print(make_change(163))  # 5: £1 + 50p + 10p + 2p + 1p