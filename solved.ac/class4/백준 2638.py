import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())

board = []

for i in range(N) :
    board.append(list(map(int, input().split())))

def dfs(r, c) :
    if board[r][c] == 1 :
        vanish[r][c] += 1
        return
    else :
        vanish[r][c] = -1
    if r - 1 >= 0 and vanish[r - 1][c] != -1 :
        dfs(r - 1, c)
    if c - 1 >= 0 and vanish[r][c - 1] != -1 :
        dfs(r, c - 1)
    if r + 1 < N and vanish[r + 1][c] != -1 :
        dfs(r + 1, c)
    if c + 1 < M and vanish[r][c + 1] != -1 :
        dfs(r, c + 1)


def is_cheeze() :
    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 1 :
                return True
    return False

t = 0
while is_cheeze() :
    vanish = [[0] * M for _ in range(N)]
    dfs(0, 0)
    for i in range(N) :
        for j in range(M) :
            if vanish[i][j] >= 2 :
                board[i][j] = 0
    t += 1

print(t)