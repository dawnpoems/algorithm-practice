import sys, bisect
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [nums[0]]
num_dp = [1] * N

for i in range(1, N) :
    if dp[-1] < nums[i] :
        dp.append(nums[i])
        num_dp[i] = len(dp)
    else :
        idx = bisect.bisect_left(dp, nums[i])
        dp[idx] = nums[i]
        num_dp[i] = idx + 1

mx = len(dp)
print(mx)

idx = num_dp.index(mx)
mx -= 1
lis = [nums[idx]]

while mx :
    if num_dp[idx] == mx :
        lis.append(nums[idx])
        mx -= 1
    idx -= 1

lis.reverse()
print(" ".join(map(str, lis)))

