import sys
input = sys.stdin.readline

TC = int(input())

INF = int(1e9)

def bellman_ford(graph) :
    v = len(graph)
    dist[1] = 0
    for i in range(1, v) :
        for edge in graph :
            if dist[edge[1]] > dist[edge[0]] + edge[2] :
                dist[edge[1]] = dist[edge[0]] + edge[2]
                if i == v - 1 :
                    return True
    return False

for t in range(TC) :
    N, M, W = map(int, input().split())
    graph = []
    for m in range(M) :
        S, E, T = map(int, input().split())
        graph.append((S, E, T))
        graph.append((E, S, T))
    for w in range(W) :
        S, E, T = map(int, input().split())
        graph.append((S, E, -T))
    flag = 0
    dist = [INF] * (N + 1)
    if bellman_ford(graph) :
        print("YES")
    else :
        print("NO")