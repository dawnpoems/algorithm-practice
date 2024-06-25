import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

def topology_sort() :
    queue = deque()
    for i in range(1, N + 1) :
        if indegree[i] == 0 :
            queue.append(i)
    
    new_rank = []
    while queue :
        now = queue.popleft()
        if queue :
            break
        new_rank.append(now)
        for v in graph[now] :
            indegree[v] -= 1
            if indegree[v] == 0 :
                queue.append(v)
    
    
    print("ans : ", new_rank)

for t in range(T) :
    N = int(input())
    pre_rank = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for i in range(1, N) :
        graph[pre_rank[i - 1]].append(pre_rank[i]) #낮은숫자 -> 높은숫자 연결되어있음.
        indegree[pre_rank[i]] += 1
    
    M = int(input())
    for i in range(M) :
        u, v = map(int, input().split())
        if pre_rank.index(u) < pre_rank.index(v) : #u 숫자 높아짐 v 숫자 낮아짐.
            graph[v].append(u) #v가 몇등일지는 모르는데 일단 u보다는 낮음.
            indegree[u] += 1
        else :
            graph[u].append(v) #몇등일지는 모르는데 일단 v보다는 낮음.
            indegree[v] += 1
    

    print(graph)
    print(indegree)
    topology_sort()
    print("-------------")
    