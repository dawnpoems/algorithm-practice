import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N, M, R = map(int ,input().split())

graph = [[] for _ in range(N + 1)]

visited = [0] * (N + 1)

cnt = 0
def dfs(n) :
    global cnt
    cnt += 1
    visited[n] = cnt
    for node in graph[n] :
        if visited[node] == 0 :
            dfs(node)

for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1) :
    graph[i].sort(reverse=True)

dfs(R)

for i in range(1, N + 1) :
    print(visited[i])