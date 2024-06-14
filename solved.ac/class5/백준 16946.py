import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for i in range(N) :
    board.append(list(map(int, list(input().strip()))))

def dfs(r, c, board) :
    global cnt
    global tag
    if board[r][c] != 0:
        return
    cnt += 1
    board[r][c] = 1
    tags[r][c] = tag
    linked.append((r, c))
    if r - 1 >= 0 :
        dfs(r - 1, c, board)
    if r + 1 < N :
        dfs(r + 1, c, board)
    if c - 1 >= 0 :
        dfs(r, c - 1, board)
    if c + 1 < M :
        dfs(r, c + 1, board)

areas = [[0] * M for _ in range(N)]
tags = [[0] * M for _ in range(N)]

tag = 1
for r in range(N) :
    for c in range(M) :
        cnt = 0
        linked = []
        if board[r][c] == 0 and areas[r][c] == 0:
            dfs(r, c, board)
            tag += 1
        while linked :
            lr, lc = linked.pop()
            areas[lr][lc] = cnt

for r in range(N) :
    for c in range(M) :
        if areas[r][c] != 0 :
            print(0, end="")
        else :
            ans = 1
            added = []
            if r - 1 >= 0 and tags[r - 1][c] not in added:
                ans += areas[r - 1][c]
                added.append(tags[r - 1][c])
            if r + 1 < N and tags[r + 1][c] not in added :
                ans += areas[r + 1][c]
                added.append(tags[r + 1][c])
            if c - 1 >= 0 and tags[r][c - 1] not in added :
                ans += areas[r][c - 1]
                added.append(tags[r][c - 1])
            if c + 1 < M and tags[r][c + 1] not in added :
                ans += areas[r][c + 1]
                added.append(tags[r][c + 1])
            print(ans % 10, end="")
    print()
