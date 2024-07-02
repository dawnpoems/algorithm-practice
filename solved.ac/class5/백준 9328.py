import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

def add_queue_door(r, c) :
    visited[r][c] = True
    if board[r][c] == "*" :
        return
    elif board[r][c].isupper() :
        doors[ord(board[r][c]) - 65].append((r, c))
    else :
        queue.append((r, c))

for t in range(T) :
    N, M = map(int, input().split())
    board = []
    queue = deque()
    for i in range(N) :
        board.append(list(input().strip()))
    
    keys = [False] * 26
    doors = [[] for _ in range(26)]
    
    visited = [[False] * M for _ in range(N)]
    for i in range(N) :
        add_queue_door(i, 0)
        add_queue_door(i, M - 1)
    
    for j in range(1, M - 1) :
        add_queue_door(0, j)
        add_queue_door(N - 1, j)
    
    lst = list(input().strip())
    if lst[0] != '0' :
        for l in lst :
            keys[ord(l) - 97] = True

    for i in range(26) :
        if keys[i] and len(doors[i]) > 0 :
            queue.extend(doors[i])
            doors[i] = []
    
    # print(queue)
    ans = 0
    while queue :
        # print(queue)
        now = queue.popleft()
        now_str = board[now[0]][now[1]]
        if now_str == "$" :
            ans += 1
        if now_str.islower() :
            keys[ord(now_str) - 97] = True
        
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4) :
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                add_queue_door(nr, nc)
        
        if not queue :
            for i in range(26) :
                if keys[i] and len(doors[i]) > 0 :
                    queue.extend(doors[i])
                    doors[i] = []

    # print("ans : ", ans)
    print(ans)