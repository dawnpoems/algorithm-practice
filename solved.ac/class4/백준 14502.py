import sys, copy
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(100000)

N, M = map(int, input().split())

board = []
virus = []

for i in range(N) :
    line = list(map(int, input().split()))
    for j in range(M) :
        if line[j] == 2 :
            virus.append((i, j))

    board.append(line)

def bfs(board) :
    queue = deque(virus)
    while queue :
        r, c = queue.popleft()
        if r - 1 >= 0 and board[r - 1][c] == 0 :
            board[r - 1][c] = 2
            queue.append((r - 1, c))
        if c - 1 >= 0 and board[r][c - 1] == 0 :
            board[r][c - 1] = 2
            queue.append((r, c - 1))
        if r + 1 < N and board[r + 1][c] == 0 :
            board[r + 1][c] = 2
            queue.append((r + 1, c))
        if c + 1 < M and board[r][c + 1] == 0 :
            board[r][c + 1] = 2
            queue.append((r, c + 1))
    cnt = 0
    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 0 :
                cnt += 1
    return cnt

ans = 0
def backtracking(wall) :
    global N
    global M
    global ans
    if wall >= 3 :
        ans = max(ans, bfs(copy.deepcopy(board)))
        return
    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 0 :
                board[i][j] = 1
                backtracking(wall + 1)
                board[i][j] = 0

backtracking(0)

print(ans)