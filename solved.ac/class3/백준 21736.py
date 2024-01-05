import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
visited = [[0] * m for _ in range(n)]

for i in range(n) :
    board.append(list(input().strip()))
    for j in range(len(board[i])) :
        if board[i][j] == 'I' :
            start = (i, j)
            visited[i][j] = 1
    
cnt = 0
queue = deque([start])
while (queue) :
    now = queue.popleft()
    r = now[0]
    c = now[1]
    if (board[r][c] == 'P') :
        cnt += 1
    if (r + 1 < n and board[r + 1][c] != 'X' and visited[r + 1][c] == 0) :
        visited[r + 1][c] = 1
        queue.append((r + 1 , c))
    if (r - 1 >= 0 and board[r - 1][c] != 'X' and visited[r - 1][c] == 0) :
        visited[r - 1][c] = 1
        queue.append((r - 1 , c))
    if (c + 1 < m and board[r][c + 1] != 'X' and visited[r][c + 1] == 0) :
        visited[r][c + 1] = 1
        queue.append((r , c + 1))
    if (c - 1 >= 0 and board[r][c - 1] != 'X' and visited[r][c - 1] == 0) :
        visited[r][c - 1] = 1
        queue.append((r , c - 1))

if (cnt == 0) :
	print("TT")
else :
    print(cnt)