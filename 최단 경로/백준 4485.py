import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


proNum = 1

def dijkstra(start_r, start_c, N):
    q = []
    heapq.heappush(q, (0, start_r, start_c))
    distance[start_r][start_c] = 0
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    while q:
        dist, now_r, now_c= heapq.heappop(q)
        if distance[now_r][now_c] < dist:
            continue
        for i in range(4):
            r = now_r + dr[i]
            c = now_c + dc[i]
            if r < 0 or r >= N or c < 0 or c >= N :
                continue
            cost = dist + board[r][c]
            if cost < distance[r][c]:
                distance[r][c] = cost
                heapq.heappush(q, (cost, r, c))

cnt = 1
while True :
    N = int(input())
    if N <= 0:
        break
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    distance = [[INF] * N for _ in range(N)]
    dijkstra(0, 0, N)
    # print("------------")
    # for d in distance :
        # print(*d)

    print("Problem", cnt, end=": ")
    print(distance[N - 1][N - 1] + board[0][0])
    cnt += 1
