import sys
input = sys.stdin.readline

N = int(input())

board = []

for i in range(N) :
    board.append(list(map(int, input().split())))

dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

for r in range(N) :
    for c in range(1, N) :
        if r == 0 and c == 1 :
            dp[r][c][0] = 1
            continue
        if board[r][c] == 1 :
            continue
        if c - 1 >= 0 :
            dp[r][c][0] += dp[r][c - 1][0] + dp[r][c - 1][2]
        if r - 1 >= 0 :
            dp[r][c][1] += dp[r - 1][c][1] + dp[r - 1][c][2]
        if r - 1 >= 0 and c - 1 >= 0 and board[r - 1][c] != 1 and board[r][c - 1] != 1:
            dp[r][c][2] += dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]

print(sum(dp[N - 1][N - 1]))

