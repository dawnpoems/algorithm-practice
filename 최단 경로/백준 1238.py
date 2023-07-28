import sys, heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m) :
    s, e, d = map(int, input().split())
    graph[s].append((e, d))

INF = int(1e9)

def dijk(start) :
    global INF
    distance = [INF] * (n + 1)

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
    return distance

from_x = dijk(x)

max_dist = 0

for k in range(1, n + 1) :
    now_dist = dijk(k)[x] + from_x[k]
    if max_dist < now_dist :
        max_dist = now_dist

print(max_dist)

