import sys
input = sys.stdin.readline

N = int(input())

board = []

for i in range(N) :
    board.append(list(map(int, input().split())))

# 시간초과나면 3차원 visited로 이 각도상에서 r, c에 도달한적이 있는지 봐도 될듯.
cnt = 0
def backtracking(direction, r, c) :
    global cnt
    if r == N - 1 and c == N - 1 :
        cnt += 1
        return
    if direction == 0 :
        if c + 1 < N and board[r][c + 1] != 1:
            backtracking(0, r, c + 1)
        if r + 1 < N and c + 1 < N and board[r + 1][c] != 1 and board[r][c + 1] != 1 and board[r + 1][c + 1] != 1:
            backtracking(2, r + 1, c + 1)
    elif direction == 1 :
        if r + 1 < N and board[r + 1][c] != 1:
            backtracking(1, r + 1, c)
        if r + 1 < N and c + 1 < N and board[r + 1][c] != 1 and board[r][c + 1] != 1 and board[r + 1][c + 1] != 1:
            backtracking(2, r + 1, c + 1)
    else :
        if c + 1 < N and board[r][c + 1] != 1:
            backtracking(0, r, c + 1)
        if r + 1 < N and board[r + 1][c] != 1:
            backtracking(1, r + 1, c)
        if r + 1 < N and c + 1 < N and board[r + 1][c] != 1 and board[r][c + 1] != 1 and board[r + 1][c + 1] != 1:
            backtracking(2, r + 1, c + 1)

backtracking(0, 0, 1)

print(cnt)