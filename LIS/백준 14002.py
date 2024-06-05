import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [1] * N

for i in range(N) :
    for j in range(i) :
        if nums[j] < nums[i] :
            dp[i] = max(dp[i], dp[j] + 1)

mx = max(dp)
print(mx)

idx = dp.index(mx)
lis = []
lis.append(nums[idx])
mx -= 1

while mx :
    if dp[idx] == mx :
        lis.append(nums[idx])
        mx -= 1
    idx -= 1

lis.reverse()

print(" ".join(map(str, lis)))