import sys
n = int(sys.stdin.readline())

num_list = []

for i in range(n):
    num_list.append(int(sys.stdin.readline().rstrip()))

num_list.sort()

max_num = 0
max_count = 0
tmp_num = 0
tmp_count = 0

for i in num_list:
    if tmp_num == i:
        tmp_count += 1
    else:
        tmp_num = i
        tmp_count = 1

    if max_count < tmp_count:
        max_num = tmp_num
        max_count = tmp_count

print(max_num)
