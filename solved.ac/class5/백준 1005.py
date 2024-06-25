import sys, copy
input = sys.stdin.readline
from collections import deque

T = int(input())

def topology_sort(w) :
    result = copy.deepcopy(times)
    queue = deque()
    for i in range(1, N + 1) :
        if indegree[i] == 0 :
            queue.append(i)
    
    while queue :
        now = queue.popleft()
        if now == w :
            print(result[now - 1])
            break
        for v in graph[now] :
            result[v - 1] = max(result[v - 1], result[now - 1] + times[v - 1])
            indegree[v] -= 1
            if indegree[v] == 0 :
                queue.append(v)
    

for t in range(T) :
    N, K = map(int, input().split())
    times = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for i in range(K) :
        u, v = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1
    # print(indegree)
    W = int(input())
    topology_sort(W)