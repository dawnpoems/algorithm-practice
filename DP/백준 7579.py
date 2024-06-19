import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mems = list(map(int, input().split()))
costs = list(map(int, input().split()))

INF = 10 ** 9
dp = [INF] * (M + 1) # 필요한 메모리가 idx일 때, 최소 cost를 기록할 곳
dp[0] = 0

for i in range(N) : #현재 메모리
    for j in range(M, 0, -1) : #코스트 순회
        if j - mems[i] < 0 :
            dp[j] = min(dp[j], costs[i])
        else : 
            dp[j] = min(dp[j], dp[j - mems[i]] + costs[i])
    # print(dp)

print(dp[-1])