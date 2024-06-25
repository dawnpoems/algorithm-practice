import sys, copy
input = sys.stdin.readline
from collections import deque

N = int(input())

times = [0]
graph = [[] for _ in range(N + 1)]
indegree = [0]

def topology_sort() :
    result = copy.deepcopy(times)
    
    while queue :
        now = queue.popleft()
        for v in graph[now] :
            result[v] = max(result[v], result[now] + times[v])
            indegree[v] -= 1
            if indegree[v] == 0 :
                queue.append(v)
    
    # print(result)
    print(max(result))

queue = deque()

for i in range(1, N + 1) :
    line = list(map(int, input().split()))
    times.append(line[0])
    indegree.append(line[1])
    if line[1] == 0 :
        queue.append(i)
    for l in range(2, len(line)) :
        graph[line[l]].append(i)

topology_sort()
