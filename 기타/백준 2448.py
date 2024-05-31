import sys
input = sys.stdin.readline

N = int(input())

M = 2 * N - 1

board = [[0] * M for _ in range(N)]

def put_tri(r, c) :
    board[r][c] = 1
    board[r+1][c-1] = 1
    board[r+1][c+1] = 1
    board[r+2][c-2] = 1
    board[r+2][c-1] = 1
    board[r+2][c] = 1
    board[r+2][c+1] = 1
    board[r+2][c+2] = 1


def star(num, r, c) :
    global N, M
    if num == 3 :
        put_tri(r, c)
        return
    star(num // 2, r, c)
    next_r = r + num // 2
    if next_r <= N :
        star(num // 2, next_r, c - (num // 2))
        star(num // 2, next_r, c + (num // 2))

star(N, 0, M // 2)

for i in range(N) :
    for j in range(M) :
        if board[i][j] == 1 :
            print("*", end="")
        else :
            print(" ", end="")
    print()