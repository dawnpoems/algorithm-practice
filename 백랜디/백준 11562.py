import sys
input = sys.stdin.readline

N, M = map(int, input().split())

INF = int(1e9)
dist = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1) :
    dist[i][i] = 0


for i in range(M) :
    u, v, b = map(int, input().split())
    if b == 0 :
        dist[u][v] = 0
        dist[v][u] = 1
    else :
        dist[u][v] = 0
        dist[v][u] = 0
    
for k in range(1, N + 1) :
    for i in range(1, N + 1) :
        for j in range(1, N + 1) :
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

K = int(input())
for k in range(K) :
    u, v = map(int, input().split())
    print(dist[u][v])

