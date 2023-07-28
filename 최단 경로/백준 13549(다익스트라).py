import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())

m = max(n, k)
d = [int(1e9)] * (m*2 + 1)
d[n] = 0


def dijkstar(start) :
    queue = []
    heapq.heappush(queue, (0, start))
    while queue :
        dist, now = heapq.heappop(queue)
        if d[now] < dist :
            continue
        front = now + 1
        if 0 <= front <= m * 2 and d[front] > dist + 1 :
            d[front] = dist + 1
            heapq.heappush(queue, (dist + 1, front))
        back = now - 1
        if 0 <= back <= m * 2 and d[back] > dist + 1 :
            d[back] = dist + 1
            heapq.heappush(queue, (dist + 1, back))
        twice = now * 2
        if 0 <= twice <= m * 2 and d[twice] > dist :
            d[twice] = dist
            heapq.heappush(queue, (dist, twice))
        # print(queue)

dijkstar(n)
# print(d)
print(d[k])