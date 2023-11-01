import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
max_num = max(nums)
scores = [0] * (max_num + 1)
table = [0] * (max_num + 1)

for numb in nums :
    table[numb] = 1
    
for i in range(n) :
    k = nums[i] * 2
    while (k <= max_num) :
        if table[k] == 1 :
            scores[nums[i]] += 1
            scores[k] -= 1
        k += nums[i]

for numb in nums :
    print(scores[numb], end=" ")