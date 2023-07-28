import sys, heapq
input= sys.stdin.readline

n, e = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(n + 1)]

for i in range(e) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijk(start) :
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue :
        dist, now = heapq.heappop(queue)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

distance = [INF] * (n + 1)
dijk(v1)
one_v1 = distance[1]
v1_v2 = distance[v2]
v1_n = distance[n]

distance = [INF] * (n + 1)
dijk(v2)
one_v2 = distance[1]
v2_n = distance[n]


answer = min(one_v1 + v2_n, one_v2 + v1_n) + v1_v2
if answer >= INF :
    print(-1)
else :
    print(answer)