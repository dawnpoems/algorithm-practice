import sys
input = sys.stdin.readline

N = int(input())

def star(r_start, c_start, r_end, c_end) :
    c = c_start
    while c <= c_end :
        board[r_start][c] = 1
        board[r_end][c] = 1
        c += 1
    r = r_start + 1
    while r < r_end :
        board[r][c_start] = 1
        board[r][c_end] = 1
        r += 1
    board[r_start + 1][c_end] = 0
    board[r_start + 2][c_end - 1] = 1

if N == 1 :
    print("*")
else :
    row = N * 4 - 1
    col = N * 4 - 3
    board = [[0] * (N * 4 - 3) for _ in range(N * 4 - 1)]
    for i in range(N - 1) :
        star(i * 2, i * 2, row - i * 2 - 1, col - i * 2 - 1)
    print(board)
    board[N * 2 - 2][(N - 1) * 2] = 1
    board[N * 2 - 1][(N - 1) * 2] = 1
    board[N * 2][(N - 1) * 2] = 1
    for i in range(row) :
        space = 0
        for j in range(col) :
            if board[i][j] == 1 :
                for k in range(space) :
                    print(" ", end="")
                    space = 0
                print("*", end="")
            else :
                space += 1
        print()
            
    