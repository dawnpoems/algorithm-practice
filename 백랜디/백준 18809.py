import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from collections import deque

N, M, G, R = map(int, input().split())

board = []
can_put = []

for i in range(N) :
    line = list(map(int, input().split()))
    for j in range(M) :
        if line[j] == 2 :
            can_put.append((i, j))
            line[j] = 1
    board.append(line)

# print(board)
# print(can_put)

def backtracking_put(idx) :
    global ans
    if len(queue_green) == G and len(queue_red) == R :
        flower = culture(copy.deepcopy(board), copy.copy(queue_green), copy.copy(queue_red))
        if flower > ans :
            ans = flower
        return
    if idx >= len(can_put) :
        return
    now = can_put[idx]
    if len(queue_green) < G :
        board[now[0]][now[1]] = 0
        queue_green.append(now)
        backtracking_put(idx + 1)
        board[now[0]][now[1]] = 1
        queue_green.pop()
    if len(queue_red) < R :
        board[now[0]][now[1]] = 0
        queue_red.append(now)
        backtracking_put(idx + 1)
        board[now[0]][now[1]] = 1
        queue_red.pop()
    backtracking_put(idx + 1)


ans = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def culture(board, queue_green, queue_red) :
    flower = 0
    # print("----------------------")

    while queue_green and queue_red :
        # print(queue_green, queue_red)
        nq_green = deque()
        nq_red = deque()
        while queue_green :
            r, c = queue_green.popleft()
            for k in range(4) :
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 1 :
                    nq_green.append((nr, nc))
                    board[nr][nc] = 2

        while queue_red :
            r, c = queue_red.popleft()
            for k in range(4) :
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M :
                    if board[nr][nc] == 1 :
                        nq_red.append((nr, nc))
                        board[nr][nc] = 0
                        nq_red.append((nr, nc))
                    if board[nr][nc] == 2 :
                        flower += 1
                        board[nr][nc] = -1

        for ng in nq_green :
            if board[ng[0]][ng[1]] == 2 :
                board[ng[0]][ng[1]] = 0
                queue_green.append(ng)

        queue_red = nq_red
    
    return flower

queue_green = deque()
queue_red = deque()
backtracking_put(0)
print(ans)