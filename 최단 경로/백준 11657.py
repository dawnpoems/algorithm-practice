import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = []
INF = int(1e9)

for i in range(M) :
    S, E, T = map(int, input().split())
    edges.append((S, E, T))

dist = [INF] * (N + 1)

def bellman_ford(edges, start) :
    global N
    dist[start] = 0
    for i in range(N) :
        for e in edges :
            if dist[e[0]] != INF and dist[e[0]] + e[2] < dist[e[1]]:
                dist[e[1]] = dist[e[0]] + e[2]
                if i == N - 1 :
                    return False
    return True

if bellman_ford(edges, 1) :
    for i in range(2, N + 1) :
        if dist[i] == INF :
            print(-1)
        else :
            print(dist[i])
else :
    print(-1)
# print(dist)