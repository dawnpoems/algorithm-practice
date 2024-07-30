import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())

board = []

for i in range(N) :
    board.append(list(map(int, input().split())))

INF = int(1e9)

ans = INF

def backtracking(dist, now, dest, depth) :
    global ans
    # print(dist, now)
    if depth == N:
        if now == dest :
            ans = min(ans, dist)
        return
    for i in range(N) :
        if board[now][i] != 0 and not visited[i]:
            visited[i] = True
            backtracking(dist + board[now][i], i, dest, depth + 1)
            visited[i] = False

visited = [False] * N
backtracking(0, 0, 0, 0)

print(ans)