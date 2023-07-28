import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for i in range(m) :
    board.append(list(map(int, list(input().strip()))))

INF = int(1e9)

distance = [[INF] * n for _ in range(m) ]

def dijk(r, c) :
    queue = []
    heapq.heappush(queue, (0, r, c))
    distance[r][c] = 0
    while queue :
        dist, row, col = heapq.heappop(queue)
        if distance[row][col] < dist :
            continue
        if row + 1 < m :
            if board[row+1][col] == 1 :
                cost = dist + 1
            else : 
                cost = dist
            if cost < distance[row+1][col] :
                distance[row+1][col] = cost
                heapq.heappush(queue, (cost, row+1, col))
        
        if col+ 1 < n :
            if board[row][col + 1] == 1 :
                cost = dist + 1
            else : 
                cost = dist
            if cost < distance[row][col+1] :
                distance[row][col+1] = cost
                heapq.heappush(queue, (cost, row, col+1))
        
        if row -1 >= 0 :
            if board[row-1][col] == 1 :
                cost = dist + 1
            else : 
                cost = dist
            if cost < distance[row-1][col] :
                distance[row-1][col] = cost
                heapq.heappush(queue, (cost, row-1, col))

        if col - 1 >= 0 :
            if board[row][col-1] == 1 :
                cost = dist + 1
            else : 
                cost = dist
            if cost < distance[row][col-1] :
                distance[row][col-1] = cost
                heapq.heappush(queue, (cost, row, col-1))

dijk(0, 0)

# print(distance)
print(distance[m-1][n-1])