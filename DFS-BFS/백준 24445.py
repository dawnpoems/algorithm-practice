import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

order = [0] * (N + 1)

for i in range(1, N + 1) :
    graph[i].sort(reverse=True)

# print(graph)

queue = deque([R])

cnt = 1
order[R] = cnt
while queue :
    now = queue.popleft()
    for v in graph[now] :
        if order[v] == 0 :
            cnt += 1
            order[v] = cnt
            queue.append(v)
            
for i in range(1, N + 1) :
    print(order[i])
