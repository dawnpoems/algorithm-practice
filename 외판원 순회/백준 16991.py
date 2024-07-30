import sys, math
input = sys.stdin.readline
from itertools import combinations

N = int(input())

pos = []
for i in range(N) :
    x, y = map(int, input().split())
    pos.append((i, x, y))

INF = 1e9

board = [[INF] * N for _ in range(N)]

def get_dist(x1, x2, y1, y2) :
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

for comb in combinations(pos, 2) :
    idx1, x1, y1 = comb[0]
    idx2, x2, y2 = comb[1]
    dist = get_dist(x1, x2, y1, y2)
    board[idx1][idx2] = dist
    board[idx2][idx1] = dist
    
# print(board)
dp = [[-1] * (1 << N) for _ in range(N)]

def dfs(now, visited) :
    if visited == (1 << N) - 1 :
        dp[now][visited] = board[now][0]
        return dp[now][visited]
    
    if dp[now][visited] != -1 :
        return dp[now][visited]

    dp[now][visited] = INF
    for i in range(N) :
        if visited & (1 << i) != 0 :
            continue
        dp[now][visited] = min(dp[now][visited], dfs(i, visited | (1 << i)) + board[now][i])
    return dp[now][visited]

print(dfs(0, 1))
# print(dp)