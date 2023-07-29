import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().strip().split()))

up_nums = [0]
up_nums.extend(numbers)
down_nums = [0]
down_nums.extend(reversed(numbers))

up_d = [0]
down_d = [0]

for i in range(1, n + 1) :
    max_j = 0
    min_j = 0
    for j in range(i) :
        if up_nums[j] < up_nums[i] :
            now_up = up_d[j] + 1
            if now_up > max_j :
                max_j = now_up
        if down_nums[j] < down_nums[i] :
            now_down = down_d[j] + 1
            if now_down > min_j :
                min_j = now_down
    up_d.append(max_j)
    down_d.append(min_j)

# print("-------")
# print(up_nums)
# print(up_d)
# print("------")
# print(down_nums)
# print(down_d)

answer = 0
for i in range(1, n + 1) :
    line = up_d[i] + down_d[n + 1 - i] - 1
    if line > answer :
        answer = line
print(answer)    
