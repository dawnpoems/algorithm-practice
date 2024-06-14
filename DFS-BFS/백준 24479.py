import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N, M, R = map(int, input().split())

visited = [0] * (N + 1)

graph = [[] for _ in range(N + 1)]

for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1) :
    graph[i].sort()

order = 0
def dfs(E, R) :
    global order
    order += 1
    visited[R] = order
    for x in graph[R] :
        if visited[x] == 0 :
            dfs(E, x)

dfs(graph, R)

for i in range(1, N + 1) :
    print(visited[i])