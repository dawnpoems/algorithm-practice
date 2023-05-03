import sys

input = sys.stdin.readline

n, price = map(int, input().split())

money = []
for i in range(n):
    money.append(int(input()))

money.reverse()
count = 0

for j in money:
    count += price//j
    price = price % j

print(count)
