import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(r, c, width, height) :
    if r < 0 or r >= height or c < 0 or c >= width :
        return (0)
    if board[r][c] == 0 :
        return (0)
    board[r][c] = 0
    dfs(r - 1, c - 1, width, height)
    dfs(r - 1, c, width, height)
    dfs(r - 1, c + 1, width, height)
    dfs(r, c - 1, width, height)
    dfs(r, c + 1, width, height)
    dfs(r + 1, c - 1, width, height)
    dfs(r + 1, c, width, height)
    dfs(r + 1, c + 1, width, height)
    return (1)

while True :
    W, H = map(int, input().split())
    if W == 0 and H == 0 :
        break
    board = []
    for i in range(H) :
        board.append(list(map(int, input().split())))
    cnt = 0
    for r in range(H) :
        for c in range(W) :
            cnt += dfs(r, c, W, H)
    print(cnt)