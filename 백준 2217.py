import sys

n = int(sys.stdin.readline())
weight_list = []
max_num = 0
count = 0

for i in range(n):
    weight_list.append(int(sys.stdin.readline()))

weight_list.sort(reverse=True)

for i in range(n):
    count += 1
    if max_num < weight_list[i] * count:
        max_num = weight_list[i] * count

print(max_num)
