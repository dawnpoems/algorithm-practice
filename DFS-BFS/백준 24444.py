import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())

orders = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1) :
    graph[i].sort()

queue = deque([R])

cnt = 1
orders[R] = cnt

while queue :
    now = queue.popleft()
    for v in graph[now] :
        if orders[v] == 0 :
            cnt += 1
            orders[v] = cnt
            queue.append(v)

for i in range(1, N + 1) :
    print(orders[i])

