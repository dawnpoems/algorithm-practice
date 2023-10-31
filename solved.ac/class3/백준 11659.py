import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

table = [0]

total = 0
for num in nums :
    total += num
    table.append(total)

for i in range(m) :
    start, end = map(int, input().split())
    print(table[end] - table[start - 1])