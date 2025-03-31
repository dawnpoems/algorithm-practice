import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())

board = []

for i in range(N) :
    board.append(list(map(int, input().split())))

result = False

visited = [[False] * N for _ in range(N)]

def dfs(r, c) :
    global result
    if result :
        return
    visited[r][c] = True
    go = board[r][c]
    if go == -1 :
        result = True
        return
    if 0 <= r + go < N and not visited[r + go][c] :
        dfs(r + go, c)
    if 0 <= c + go < N and not visited[r][c + go]:
        dfs(r, c + go)
    
dfs(0, 0)

if result :
    print("HaruHaru")
else :
    print("Hing")
