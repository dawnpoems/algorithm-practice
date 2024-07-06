import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

INF = int(1e9)

graph = [[INF] * (N + 1) for _ in range(N + 1)]
nxt = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1) :
    graph[i][i] = 0

for i in range(M) :
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    nxt[a][b] = b

for k in range(1, N + 1) :
    for i in range(1, N + 1) :
        for j in range(1, N + 1) :
            if graph[i][k] + graph[k][j] < graph[i][j] :
                graph[i][j] = graph[i][k] + graph[k][j]
                nxt[i][j] = nxt[i][k]

print("--------------")

for i in range(1, N + 1) :
    for j in range(1, N + 1) :
        if graph[i][j] == INF :
            print(0, end=" ")
        else :
            print(graph[i][j], end=" ")
    print()


for i in range(1, N + 1) :
    for j in range(1, N + 1) :
        path = []
        path.append(i)
        idx = nxt[i][j]
        while idx :
            path.append(idx)
            idx = nxt[idx][j]
        if len(path) == 1 :
            print(0)
        else :
            print(len(path), end=" ")
            print(*path)


