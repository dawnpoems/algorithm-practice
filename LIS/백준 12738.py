import sys, bisect
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [nums[0]]

for i in range(N) :
    if dp[-1] < nums[i] :
        dp.append(nums[i])
    else :
        idx = bisect.bisect_left(dp, nums[i])
        dp[idx] = nums[i]

# print(dp)
print(len(dp))