import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M, K = map(int, input().split())

board = [[0] * M for _ in range(N)]

for i in range(K) :
    c_start, r_start, c_end, r_end = map(int, input().split())
    r = r_start
    while r < r_end :
        c = c_start
        while c < c_end :
            board[r][c] = 1
            c+= 1
        r += 1

def dfs(r, c) :
    global area
    if board[r][c] == 1 :
        return (0)
    board[r][c] = 1
    area += 1
    if r - 1 >= 0 : 
        dfs(r - 1, c)
    if r + 1 < N :
        dfs(r + 1, c)
    if c - 1 >= 0 :
        dfs(r, c - 1)
    if c + 1 < M :
        dfs(r, c + 1)
    return (1)

ans = []
count = 0

for i in range(N) :
    for j in range(M) :
        area = 0
        if dfs(i, j) == 1 :
            count += 1
            ans.append(area)
    
print(count)
print(*sorted(ans))

