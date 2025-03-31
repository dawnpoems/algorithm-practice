import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def bfs(start_r, start_c, start_num) :
    queue = deque([(start_r, start_c, 0)])
    visited = [[False] * W for _ in range(H)]
    visited[start_r][start_c] = True

    gr = [-1, +1, 0, 0]
    gc = [0, 0, -1, +1]
    clean_cnt = 0
    while queue :
        r, c, depth = queue.popleft()
        if board[r][c] >= 1 :
            clean_cnt += 1
            graph[start_num][board[r][c]] = depth
            if clean_cnt >= dirty_cnt :
                return True
        for i in range(4) :
            nr = r + gr[i]
            nc = c + gc[i]
            if 0 <= nr < H and 0 <= nc < W and board[nr][nc] != -1 and not visited[nr][nc] :
                visited[nr][nc] = True
                queue.append((nr, nc, depth + 1))
    return False

def backTracking(depart, dist, mask) :
    global ans
    if mask == 2 ** (dirty_cnt) - 1 :
        ans = min(ans, dist)
    for i in range(dirty_cnt) :
        if (mask >> i) & 1 != 1 :
            mask += 1 << i
            backTracking(i + 1, dist + graph[depart][i + 1], mask)
            mask -= 1 << i

while True :
    W, H = map(int, input().split())

    if W == 0 and H == 0 :
        break

    board = []
    dirty_cnt = 0
    dirty_pos = []
    for i in range(H) :
        str = list(input().strip())
        line = []
        for j in range(W) :
            if str[j] == "." :
                line.append(0)
            elif str[j] == "*" :
                dirty_cnt += 1
                line.append(dirty_cnt)
                dirty_pos.append((i, j))
            elif str[j] == "x" :
                line.append(-1)
            elif str[j] == "o" :
                line.append(0)
                start = (i, j)
        board.append(line)

    graph = [[0] * (dirty_cnt + 1) for _ in range(dirty_cnt + 1)]
    if bfs(start[0], start[1], 0) :
        for i in range(dirty_cnt) :
            bfs(dirty_pos[i][0], dirty_pos[i][1], i + 1)
        ans = INF
        backTracking(0, 0, 0)
        print(ans)
    else :
        print(-1)
    
