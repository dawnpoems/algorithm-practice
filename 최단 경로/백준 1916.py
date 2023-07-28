import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m) :
    s, e, d = map(int, input().split())
    graph[s].append((e, d))

start, end = map(int, input().split())

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

dijk(start)

# print(distance)
print(distance[end])