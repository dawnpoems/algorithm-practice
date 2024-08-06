import sys
input = sys.stdin.readline

R, C, Q = map(int, input().split())

board = [[]]

for i in range(R) :
    line = list(map(int, input().split()))
    s = 0
    row = [0]
    for i in range(C) :
        s += line[i]
        row.append(s)
    board.append(row)

# for b in board :
#     print(b)

for i in range(Q) :
    r1, c1, r2, c2 = map(int, input().split())
    ans = 0
    for i in range(r2 - r1 + 1) :
        ans += board[r1 + i][c2] - board[r1 + i][c1 - 1]
        # print(ans)
    ans //= (r2 - r1 + 1) * (c2 - c1 + 1)
    print(ans)