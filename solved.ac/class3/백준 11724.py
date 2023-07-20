import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited) :
    if visited[v] :
        return False
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)
    return True

cnt = 0

for i in range(1, n + 1) :
    if dfs(graph, i, visited) :
        # print(visited)
        cnt += 1

print(cnt)
