import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())

graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1) :
    line = list(map(int, input().split()))
    j = 1
    while line[j] != -1 :
        graph[line[0]].append((line[j], line[j + 1]))
        j += 2

def dfs(now, depth) :
    global ans
    global best_node
    visited[now] = True
    if ans < depth :
        ans = depth
        best_node = now
    for c in graph[now] :
        if not visited[c[0]] :
            dfs(c[0], depth + c[1])

visited = [False] * (N + 1)
ans = 0
best_node = 0
dfs(1, 0)
visited = [False] * (N + 1)
ans = 0
tmp = best_node
best_node = 0
dfs(tmp, 0)

print(ans)