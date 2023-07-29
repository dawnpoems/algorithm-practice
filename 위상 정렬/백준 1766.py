import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology() :
    queue = []
    for i in range(1, n + 1) :
        if indegree[i] == 0 :
            heapq.heappush(queue, i)

    while queue :
        now = heapq.heappop(queue)
        print(now, end=" ")
        for i in graph[now] :
            indegree[i] -= 1
            if indegree[i] == 0 :
                heapq.heappush(queue, i)

topology()