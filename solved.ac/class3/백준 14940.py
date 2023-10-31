import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
answer = [[-1] * m for _ in range(n)]

for i in range(n) :
    board.append(list(map(int, input().split())))

def find_start(row, col) :
    for r in range(row) :
        for c in range(col) :
            if board[r][c] == 2 :
                start = (r, c)
                answer[r][c] = 0
            elif board[r][c] == 0 :
                answer[r][c] = 0
    return (start)

start = find_start(n, m)

def bfs(start, n, m) :
    queue = deque([start])
    while queue :
        now = queue.popleft()
        r = now[0]
        c = now[1]
        if (r - 1 >= 0 and answer[r-1][c] == -1) :
            answer[r-1][c] = answer[r][c] + 1
            queue.append((r-1, c))
        if (r + 1 < n and answer[r+1][c] == -1) :
            answer[r+1][c] = answer[r][c] + 1
            queue.append((r+1, c))
        if (c - 1 >= 0 and answer[r][c-1] == -1) :
            answer[r][c-1] = answer[r][c] + 1
            queue.append((r, c-1))
        if (c + 1 < m and answer[r][c+1] == -1) :
            answer[r][c+1] = answer[r][c] + 1
            queue.append((r, c+1))

bfs(start, n, m)

for i in range(n) :
    for j in range(m) :
        print(answer[i][j], end=" ")
    print()