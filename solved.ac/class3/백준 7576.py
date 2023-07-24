import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().strip().split())

all_tomatos = []

queue = deque([])

for j in range(n) :
    row = list(map(int, input().strip().split()))
    for k in range(len(row)) : 
        if row[k] == 1 :
            queue.append((j, k))

    all_tomatos.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue :
    now = queue.popleft()

    for i in range(4) :
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m :
            continue
        if all_tomatos[nx][ny] == -1 or all_tomatos[nx][ny] == 1 :
            continue
        if all_tomatos[nx][ny] == 0 :
            all_tomatos[nx][ny] = all_tomatos[now[0]][now[1]] + 1
            queue.append((nx, ny))
        
no_flag = False
max_tomato = 0 
for x in all_tomatos :
    for tomato in x :
        if tomato == 0 :
            no_flag = True
            break
        if tomato > max_tomato :
            max_tomato = tomato
                

if no_flag :
    print(-1)
else :
    print(max_tomato - 1)
