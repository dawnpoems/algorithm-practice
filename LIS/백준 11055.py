import sys, copy
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

dp = copy.deepcopy(nums)

for i in range(N) :
    for j in range(i) :
        if nums[j] < nums[i] :
            dp[i] = max(dp[i], dp[j] + nums[i])

# print(dp)
print(max(dp))