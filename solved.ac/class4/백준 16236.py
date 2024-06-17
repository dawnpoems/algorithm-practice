import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

sea = []
queue = deque([])
for i in range(N) :
    line = list(map(int, input().split()))
    for j in range(N) :
        if line[j] == 9 :
            queue.append((i, j, 0))
            line[j] = 0
    sea.append(line)

size = 2
full = size
time = 0

def eat() :
    global size
    global full
    full -= 1
    if not full :
        size += 1
        full = size

while True :
    visited = [[False] * N for _ in range(N)]
    can_eat = []
    while queue :
        r, c, dist = queue.popleft()
        if 0 < sea[r][c] < size :
            can_eat.append((r, c, dist))
            # print(can_eat)
        if can_eat :
            continue
        if r - 1 >= 0 and not visited[r - 1][c] and sea[r - 1][c] <= size :
            visited[r - 1][c] = True
            queue.append((r - 1, c, dist + 1))
        if c - 1 >= 0 and not visited[r][c - 1] and sea[r][c - 1] <= size :
            visited[r][c - 1] = True
            queue.append((r, c - 1, dist + 1))
        if c + 1 < N and not visited[r][c + 1] and sea[r][c + 1] <= size :
            visited[r][c + 1] = True
            queue.append((r, c + 1, dist + 1))
        if r + 1 < N and not visited[r + 1][c] and sea[r + 1][c] <= size :
            visited[r + 1][c] = True
            queue.append((r + 1, c, dist + 1))
    # print("-------------")
    # print(time, size, full)
    # print(r, c)
    # for s in sea :
    #     print(*s)
    if can_eat :
        can_eat.sort(key=lambda x : (x[2], x[0], x[1]))
        r, c, dist = can_eat[0]
        sea[r][c] = 0
        queue = deque([(r, c, 0)])
        time += dist
        eat()
    else :
        break

print(time)