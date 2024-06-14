import heapq
import sys
input = sys.stdin.readline

N, M, A, B, C = map(int, input().split())

graph = [[] for _ in range(N + 1)]
lines = []

for i in range(M) :
    start, end, cost = map(int, input().split())
    heapq.heappush(lines, (cost, start, end))
    graph[start].append((end, cost))
    graph[end].append((start, cost))

INF = int(1e9)

def dejkstra(start) :
    queue = []
    heapq.heappush(queue, (0, start))
    dist[start] = 0
    while queue :
        d, now = heapq.heappop(queue)
        if dist[now] < d :
            continue
        for i in graph[now] :
            cost = d + i[1]
            if cost < dist[i[0]] :
                dist[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

def dejkstra_shame(start) :
    global C
    queue = []
    heapq.heappush(queue, (0, 0, start))
    dist[start] = 0
    while queue :
        s, d, now = heapq.heappop(queue)
        if dist[now] < d :
            continue
        for i in graph[now] :
            cost = d + i[1]
            shame = max(d, i[1])
            if s < dist[i[0]] and C:
                dist[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dist = [INF] * (N + 1)
dejkstra(A)
if dist[B] > C :
    print(-1)


else :
    graph = [[] for _ in range(N + 1)]
    while lines :
        dist = [INF] * (N + 1)
        cost, start, end = heapq.heappop(lines)
        graph[start].append((end, cost))
        graph[end].append((start, cost))
        if lines and lines[0][0] == cost :
            continue
        dejkstra(A)
        if dist[B] <= C :
            print(cost)
            break
