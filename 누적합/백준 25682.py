import sys
input=sys.stdin.readline

N, M, K = map(int, input().split())

board = []

for i in range(N) :
    board.append(list(input().strip()))
    
black = [[0] * M for _ in range(N)]
white = [[0] * M for _ in range(N)]

for i in range(N) :
    if i % 2 == 0 :
        now = "B"
    else :
        now = "W"
    for j in range(M) :
        if i - 1 >= 0 :
            black[i][j] += black[i - 1][j]
            white[i][j] += white[i - 1][j]
        if j - 1 >= 0 :
            black[i][j] += black[i][j - 1]
            white[i][j] += white[i][j - 1]
        if i - 1 >= 0 and j - 1 >= 0 :
            black[i][j] -= black[i - 1][j - 1]
            white[i][j] -= white[i - 1][j - 1]
        if board[i][j] != now :
            black[i][j] += 1
        else :
            white[i][j] += 1
        if now == "B" :
            now = "W"
        else :
            now = "B"

ans = 10 ** 9
for i in range(K - 1, N) :
    for j in range(K - 1, M) :
        black_now = black[i][j]
        white_now = white[i][j]
        if i - K >= 0 :
            black_now -= black[i - K][j]
            white_now -= white[i - K][j]
        if j - K >= 0 :
            black_now -= black[i][j - K]
            white_now -= white[i][j - K]
        if i - K >= 0 and j - K >= 0 :
            black_now += black[i - K][j - K]
            white_now += white[i - K][j - K]
        ans = min(ans, black_now, white_now)

print(ans)