import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

dp = [nums[0]]

for i in range(1, N) :
    if nums[i] > dp[-1] :
        dp.append(nums[i])
    else :
        idx = bisect_left(dp, nums[i])
        dp[idx] = nums[i]

print(len(dp))