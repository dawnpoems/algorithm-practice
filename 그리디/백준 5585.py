import sys

coins = [500, 100, 50, 10, 5, 1]

price = 1000 - int(sys.stdin.readline())

count = 0
for coin in coins:
    count += price // coin
    price = price % coin

print(count)
