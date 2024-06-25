import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)

ans = 0
ans_lst = []

def dfs(n) :
    global cnt
    global ans
    visited[n] = True
    cnt += 1
    found = False
    for v in graph[n] :
        if not visited[v] :
            found = True
            dfs(v)
    if not found :
        if cnt > ans :
            ans = cnt
            ans_lst = [n]
        if cnt == ans :
            ans_lst.append(n)
    

print(ans)

for i in range(1, N + 1) :
    visited = [False] * (N + 1)
    cnt = 0
    dfs(i)

print(*sorted(ans_lst)) 

