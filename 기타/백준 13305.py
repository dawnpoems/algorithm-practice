import sys

n = (int(sys.stdin.readline()) - 1)
distance_list = list(map(int, sys.stdin.readline().split()))
oil_list = list(map(int, sys.stdin.readline().split()))

price_all = 0
tmp_price = oil_list[0]

for i in range(n):
    if (oil_list[i] < tmp_price):
        tmp_price = oil_list[i]

    price_all += (distance_list[i] * tmp_price)

print(price_all)
