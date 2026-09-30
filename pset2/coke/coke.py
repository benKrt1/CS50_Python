amount_due = 50

while amount_due > 0:
    coin = int(input(f"Amount Due: {amount_due}\nInsert Coin: "))
    if coin not in (25, 10, 5):
        continue
    amount_due -= coin

print(f"Change Owed: {-amount_due}")
