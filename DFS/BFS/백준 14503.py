import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())

r, c, d = map(int, input().strip().split())

board = []
for i in range(n) :
    board.append(list(map(int, input().strip().split())))

queue = deque([(r, c, d)])

dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]
# 북동남서 순서. d 순서와 동일

answer = 0

while queue :
    now = queue.popleft()
    if board[now[0]][now[1]] == 0 :
        board[now[0]][now[1]] = 2
        answer += 1

    back_flag = False
    for i in range(1, 5) :
        nd = now[2] - i
        if nd < 0 :
            nd += 4

        nx = now[0] + dx[nd]
        ny = now[1] + dy[nd]

        if board[nx][ny] != 0 :
            continue

        queue.append((nx, ny, nd))
        back_flag = True
        break
        
    if back_flag == False :
        back_d = now[2] + 2
        if back_d >= 4 :
            back_d -= 4
        back_x = now[0] + dx[back_d] 
        back_y = now[1] + dy[back_d]

        if board[back_x][back_y] == 1 :
            break
        
        queue.append((back_x, back_y, now[2]))

print(answer)


