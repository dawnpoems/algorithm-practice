import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())

stickers = []
board = [[0] * M for _ in range(N)]

for k in range(K) :
    r, c = map(int, input().split())
    sti = []
    for i in range(r) :
        sti.append(list(map(int, input().split())))
    stickers.append(sti)

def restore_visited(r, c, visited) :
    for i in range(len(visited)) :
        for j in range(len(visited[0])) :
            if visited[i][j] :
                board[r + i][c + j] = 0
    
def bfs(r, c, sti) :
    sti_hei = len(sti)
    sti_wid = len(sti[0])
    visited = [[False] * sti_wid for _ in range(sti_hei)]
    queue = deque()
    
    for i in range(sti_hei) :
        if sti[i][0] == 1 :
            if board[r + i][c] == 1 :
                return False
            else :
                visited[i][0] = True
                board[r + i][c] = 1
                queue.append((i, 0))
            break

    while queue :
        now = queue.popleft()
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4) :
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
            if 0 <= nr < sti_hei and 0 <= nc < sti_wid and sti[nr][nc] == 1 and not visited[nr][nc] :
                if board[r + nr][c + nc] == 1 :
                    restore_visited(r, c, visited)
                    return False
                else :
                    visited[nr][nc] = True
                    board[r + nr][c + nc] = 1
                    queue.append((nr, nc))
    return True

def rotate_sticker(sti) :
    sti_hei = len(sti)
    sti_wid = len(sti[0])
    ret = [[0] * sti_hei for _ in range(sti_wid)]
    for i in range(sti_hei) :
        for j in range(sti_wid) :
            ret[j][sti_hei - i - 1] = sti[i][j]
    return ret
    
def find_pos(sti) :
    for i in range(N - len(sti) + 1) :
        for j in range(M - len(sti[0]) + 1) :
            if bfs(i, j, sti) :
                return True
    return False

for sti in stickers :
    now = sti
    for rot in range(4) :
        if find_pos(now) :
            break
        if rot < 3 :
            now = rotate_sticker(now)

ans = 0
for i in range(N) :
    for j in range(M) :
        if board[i][j] == 1 :
            ans += 1

print(ans)