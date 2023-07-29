import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if i == j :
            graph[i][j] = 0

for i in range(m) :
    s, e, d = map(int, input().split())
    if graph[s][e] > d :
        graph[s][e] = d

for k in range(1, n + 1) :
    for s in range(1, n + 1) :
        for e in range(1, n + 1) :
            graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])

for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        now = graph[i][j]
        if now == INF :
            print(0, end=" ")
        else :
            print(graph[i][j], end=" ")
    print()