import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


proNum = 1

while True:  # 0이면 종료
    n = int(input())
    if n <= 0:
        break
    nodes = []
    for i in range(n):
        nodes.append(list(map(int, input().split())))

    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for i in nodes:
        # a, b, c = map(int, input().split())
        graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
