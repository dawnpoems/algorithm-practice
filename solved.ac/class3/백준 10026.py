import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())

board = []
board_colorless = []

for i in range(N) :
    lst = list(input().strip())
    line = []
    line_cl = []
    for l in lst :
        if l == 'R' :
            line.append(1)
            line_cl.append(1)
        elif l == 'G' :
            line.append(2)
            line_cl.append(1)
        else :
            line.append(3)
            line_cl.append(3)
    board.append(line)
    board_colorless.append(line_cl)

# print(board)
# print(board_colorless)

def dfs_rgb(r, c) :
    if (board[r][c] == 0) :
        return (0)
    now_rgb = board[r][c]
    board[r][c] = 0
    if (r - 1 >= 0 and board[r - 1][c] == now_rgb) :
        dfs_rgb(r - 1, c)
    if (r + 1 < N and board[r + 1][c] == now_rgb) :
        dfs_rgb(r + 1, c)
    if (c - 1 >= 0 and board[r][c - 1] == now_rgb) :
        dfs_rgb(r, c - 1)
    if (c + 1 < N and board[r][c + 1] == now_rgb) :
        dfs_rgb(r, c + 1)
    return (1)

def dfs_rg_b(r, c) :
    if (board_colorless[r][c] == 0) :
        return (0)
    now_rgb = board_colorless[r][c]
    board_colorless[r][c] = 0
    if (r - 1 >= 0 and board_colorless[r - 1][c] == now_rgb) :
        dfs_rg_b(r - 1, c)
    if (r + 1 < N and board_colorless[r + 1][c] == now_rgb) :
        dfs_rg_b(r + 1, c)
    if (c - 1 >= 0 and board_colorless[r][c - 1] == now_rgb) :
        dfs_rg_b(r, c - 1)
    if (c + 1 < N and board_colorless[r][c + 1] == now_rgb) :
        dfs_rg_b(r, c + 1)
    return (1)

ans_rgb = 0
ans_rg_b = 0

for i in range(N) :
    for j in range(N) :
            ans_rgb += dfs_rgb(i, j)
            ans_rg_b += dfs_rg_b(i, j)

print(ans_rgb, end=" ")
print(ans_rg_b)