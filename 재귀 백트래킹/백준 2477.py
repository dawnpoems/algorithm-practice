import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())

board = [[0] * N for _ in range(N)]

def star(r, c, num) :
    if num == 1 :
        board[r][c] = 1
        return 
    star(r, c, num // 3)
    star(r, c + num // 3, num // 3)
    star(r, c + num // 3 * 2, num // 3)
    star(r + num // 3, c, num // 3)
    star(r + num // 3, c + num // 3 * 2, num // 3)
    star(r + num // 3 * 2, c, num // 3)
    star(r + num // 3 * 2, c + num // 3, num // 3)
    star(r + num // 3 * 2, c + num // 3 * 2, num // 3)

star(0, 0, N)

for i in range(N) :
    for j in range(N) :
        if board[i][j] == 0 :
            print(" ", end="")
        else :
            print("*", end="")
    print()
