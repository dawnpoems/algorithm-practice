import sys
from collections import deque
input = sys.stdin.readline

K = int(input())

def bfs(start, colors, graph) :
    if colors[start] != 0 :
        return True
    queue = deque([start])
    colors[start] = 1
    while queue :
        now = queue.popleft()
        for node in graph[now] :
            if colors[now] == colors[node] :
                return False
            elif colors[node] == 0 :
                colors[node] = 2 if colors[now] == 1 else 1
                queue.append(node)
    return True
    
for i in range(K) :
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    colors = [0] * (V + 1)
    for i in range(E) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    ans = True
    for i in range(1, V + 1) :
        if not bfs(i, colors, graph) :
            ans = False
            break

    if ans :
        print("YES")
    else :
        print("NO")
