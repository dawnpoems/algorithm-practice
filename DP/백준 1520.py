import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []

for i in range(N) :
    board.append(list(map(int, input().split())))
    
dp = [[0] * M for _ in range(N)] #(a, b)에서는 (N - 1, M - 1) 까지 c개의 경로로 도달할 수 있음

visited = [[False] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c) :
    if r == N - 1 and c == M - 1 :
        return 1
    print(r, c)
    if dp[r][c] or visited[r][c]:
        return dp[r][c]
    visited[r][c] = True
    for i in range(4) :
        mr = r + dr[i]
        mc = c + dc[i]
        if 0 <= mr < N and 0 <= mc < M and board[mr][mc] < board[r][c] :
            dp[r][c] += dfs(mr, mc)
    return dp[r][c]

dfs(0, 0)
# print("------dp------")
# for d in dp :
#     print(*d)

print(dp[0][0])

