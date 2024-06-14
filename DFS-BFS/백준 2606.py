import sys

nodes = int(sys.stdin.readline())
n = int(sys.stdin.readline())

graph = [[] for _ in range(nodes + 1)]

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (nodes + 1)


# 깊이우선탐색 함수
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 1번에서 시작해서 한번
dfs(graph, 1, visited)


# True의 갯수만큼 바이러스가 닿은 곳임
virus = 0
for i in visited:
    if i == True:
        virus += 1

# 1번 본인은 빼라고 했으므로 -1
print(virus - 1)
