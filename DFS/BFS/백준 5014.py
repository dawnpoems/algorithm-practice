import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

queue = deque([S])
counts = [-1] * (F + 1)
counts[S] = 0
el_flag = False

while queue :
    v = queue.popleft()
    if v == G :
        print(counts[v])
        el_flag = True
        break
    uv = v + U
    ud = v - D

    if 1 <= uv <= F and counts[uv] == -1 :
        counts[uv] = counts[v] + 1
        queue.append(uv)
    if 1 <= ud <= F and counts[ud] == -1 :
        counts[ud] = counts[v] + 1
        queue.append(ud)

if not el_flag :
    print("use the stairs")

