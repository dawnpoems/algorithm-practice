import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
e_list = [[] for _ in range(n + 1)]

for i in range(m) :
    s, e, d = map(int, input().split())
    graph[s].append((e, d))

# for i in range(m) :
#     s, e, d = map(int, input().split())
#     if e in e_list :
#         idx = e_list.index(e)
#         if d < graph[s][idx] :
#             graph[s][idx] = (e, d)
#     else :
#         e_list[s].append(e)
#         graph[s].append((e, d))

start, end = map(int, input().split())

INF = int(1e9)
#거리, 경로 기록
distance = [[INF, ""] for _ in range(n + 1)]

def dijk(start) :
    queue = []
    heapq.heappush(queue, (0, start , str(start)))
    distance[start] = [0, str(start)]
    while queue :
        dist, now, route = heapq.heappop(queue)
        if distance[now][0] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            now_route = route + "/" + str(i[0])
            if cost < distance[i[0]][0] :
                distance[i[0]] = [cost, now_route]
                heapq.heappush(queue, (cost, i[0], now_route))
    # print(queue)

dijk(start)
# print(distance)
# print(distance[end])

answer = distance[end]
print(answer[0])
answer_list = answer[1].split("/")
print(len(answer_list))
print(" ".join(answer_list))