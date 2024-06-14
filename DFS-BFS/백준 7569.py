import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().strip().split())

all_tomatos = []

queue = deque([])

for i in range(h) :
    tomatos_layer = []
    for j in range(n) :
        row = list(map(int, input().strip().split()))
        tomatos_layer.append(row)
        for k in range(len(row)) : 
            if row[k] == 1 :
                queue.append((i, j, k))

    all_tomatos.append(tomatos_layer)

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

while queue :
    now = queue.popleft()

    for i in range(6) :
        nz = now[0] + dz[i]
        nx = now[1] + dx[i]
        ny = now[2] + dy[i]
        if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m :
            continue
        if all_tomatos[nz][nx][ny] == -1 or all_tomatos[nz][nx][ny] == 1 :
            continue
        if all_tomatos[nz][nx][ny] == 0 :
            all_tomatos[nz][nx][ny] = all_tomatos[now[0]][now[1]][now[2]] + 1
            queue.append((nz, nx, ny))
        
no_flag = False
max_tomato = 0 
for z in all_tomatos :
    for x in z :
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




