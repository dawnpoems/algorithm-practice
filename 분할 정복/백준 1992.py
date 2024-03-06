import sys
input=sys.stdin.readline

N = int(input())

board = []

for i in range(N) :
    board.append(list(map(int, list(input().strip()))))

def is_same(r, c, scale) :
    num = board[r][c]
    for i in range(r, r + scale) :
        for j in range(c, c + scale) :
            if (board[i][j] != num) :
                return (-1)
    return (num)

def compress(r, c, scale) :
    if (scale == 1 or is_same(r, c, scale) != -1) :
        print(board[r][c], end="")
        return 
    print("(", end="")
    compress(r, c, scale // 2)
    compress(r, c + scale // 2, scale // 2)
    compress(r + scale // 2, c, scale // 2)
    compress(r + scale // 2, c + scale // 2, scale // 2)
    print(")", end="")

compress(0, 0, N)