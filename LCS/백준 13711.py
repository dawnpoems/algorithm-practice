import sys, bisect
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

transed = []
for b in B :
    transed.append(A.index(b))

dp = [transed[0]]

for i in range(1, N) :
    if dp[-1] < transed[i] :
        dp.append(transed[i])
    else :
        idx = bisect.bisect_left(dp, transed[i])
        dp[idx] = transed[i]

print(len(dp))
