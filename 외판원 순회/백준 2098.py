import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())

board = []

for i in range(N) :
    board.append(list(map(int, input().split())))

INF = int(1e9)

dp = [[-1] * (1 << N) for _ in range(N)]

def dfs(now, visited) :

    if visited == (1 << N) - 1 :
        if board[now][0] :
            dp[now][visited] = board[now][0]
        else :
            dp[now][visited] = INF
        return dp[now][visited]
    
    if dp[now][visited] != -1 :
        return dp[now][visited]
    
    dp[now][visited] = INF
    for i in range(N) :
        if board[now][i] != 0 and visited & (1 << i) == 0 :
            dist = dfs(i, visited | (1 << i)) + board[now][i]
            if dp[now][visited] > dist :
                dp[now][visited] = dist
    return dp[now][visited]

print(dfs(0, 1))