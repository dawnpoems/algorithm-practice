import sys
input = sys.stdin.readline

N = int(input())

line_len = 4 * N - 3

board = [[0] * line_len for _ in range(line_len)]

start = 0
end = line_len
for i in range(N) :
    for j in range(start, end) :
        board[start][j] = 1
        board[end - 1][j] = 1
        board[j][start] = 1
        board[j][end - 1] = 1
    start += 2
    end -= 2

for row in board :
    for b in row :
        if b == 0 :
            print(" ", end="")
        else :
            print("*", end="")
    print()