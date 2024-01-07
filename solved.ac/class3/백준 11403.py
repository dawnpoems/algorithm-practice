import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N)]
answer = [[0] * N for _ in range(N)]

for i in range(N) :
    now = input().split()
    for j in range(N) :
        if (now[j] == '1') :
            graph[i].append(j)

# print(graph)

def dfs(start, end, now) :
    visited[now] = True
    if (now == end) :
        answer[start][end] = 1
        return
    for node in graph[now] :
        if not visited[node] :
            dfs(start, end, node)
            visited[now] = False

for i in range(N) :
    for j in range(N) :
        visited = [False] * N
        for node in graph[i] :
            dfs(i, j, node)

for i in range(N) :
    for j in range(N) :
        print(answer[i][j], end=" ")
    print()

# print(answer)



