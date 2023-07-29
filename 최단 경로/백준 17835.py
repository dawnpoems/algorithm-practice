import sys, heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())

INF = float('inf')
graph = [[] for _ in range(n + 1)]


for i in range(m) :
    s, c, d = map(int, input().split())
    graph[c].append((s, d))

def dijkstra(start) :
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

cities = list(map(int, input().split()))

distance = [INF] * (n + 1)
for city in cities :
    dijkstra(city)

# print(distance)
max_route = 0
max_idx = 0
for i in range(1, n + 1) :
    if max_route < distance[i] :
        max_route = distance[i]
        max_idx = i

print(max_idx)
print(max_route)



