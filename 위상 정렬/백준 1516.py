import sys, copy
input = sys.stdin.readline
from collections import deque

N = int(input())

times = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

def topology_sort() :
    result = copy.deepcopy(times)
    queue = deque()
    for i in range(1, N + 1) :
        if indegree[i] == 0 :
            queue.append(i)
    
    while queue :
        now = queue.popleft()
        for v in graph[now] :
            result[v] = max(result[v], result[now] + times[v])
            indegree[v] -= 1
            if indegree[v] == 0 :
                queue.append(v)
    
    for i in range(1, N + 1) :
        print(result[i])

for i in range(1, N + 1) :
    line = list(map(int, input().split()))
    times[i] = line[0]
    j = 1
    while line[j] != -1 :
        indegree[i] += 1
        graph[line[j]].append(i)
        j += 1


# print(times)
# print(indegree)
# print(graph)
topology_sort()