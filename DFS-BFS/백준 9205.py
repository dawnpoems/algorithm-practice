import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())

#1000보다 작으면 갈 수 있는 곳, graph 연결하기.
#모든 간선을 연결했을 때, home에서 fest로 갈 수 있는 길이 있다면 happy를 출력.

def dfs (graph, v, visited) :
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)
 

for t in range(tc) :
    n = int(input())
    places = [[]]
    graph = [[] for _ in range(n + 3)]
    for i in range(1, n + 3) :
        now = list(map(int, input().strip().split()))
        places.append(now)
        for p in range(1, len(places) - 1) :
            if abs(places[p][0] - now[0]) + abs(places[p][1] - now[1]) <= 1000 :
                graph[p].append(i)
                graph[i].append(p)

    
    visited = [False] * (n + 3)
    dfs(graph, 1, visited)

    if visited[-1] :
        print("happy")
    else :
        print("sad")


