import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

board = []

for i in range(N) :
    board.append(list(map(int, input().split())))

for i in range(N) :
    board[i][i] = 1

for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            if board[i][j] == 0 and board[i][k] == 1 and board[k][j] == 1 :
                board[i][j] = 1

# for b in board :
#     print(b)

plan = list(map(int, input().split()))

ans = True

for i in range(M - 1) :
    if board[plan[i] - 1][plan[i + 1] - 1] == 0 :
        ans = False
        break

if ans :
    print("YES")
else :
    print("NO")