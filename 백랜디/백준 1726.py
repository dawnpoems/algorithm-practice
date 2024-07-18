import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

board = []

for i in range(N) :
    board.append(list(map(int, input().split())))

SR, SC, SD = map(int, input().split())
ER, EC, ED = map(int, input().split())

def bfs(sr, sc, sd) :
    
    queue = deque([(sr, sc, sd, 0)])
    
    visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    visited[sr][sc][sd] = True

    while queue :
        nr, nc, nd, cnt = queue.popleft()
        # print(nr, nc, nd, cnt)
        if nr == ER - 1 and nc == EC - 1 and nd == ED - 1 :
            return cnt
        
        #Go k
        if nd == 0 :
            for i in range(nc + 1, nc + 4) :
                if i >= M or board[nr][i] == 1 :
                    break
                if not visited[nr][i][nd] :
                    visited[nr][i][nd] = True
                    queue.append((nr, i, nd, cnt + 1))
        elif nd == 1 :
            i = nc - 1
            for i in range(nc - 1, nc - 4, -1) :
                if i < 0 or board[nr][i] == 1 :
                    break
                if not visited[nr][i][nd] :
                    visited[nr][i][nd] = True
                    queue.append((nr, i, nd, cnt + 1))
        elif nd == 2 :
            for i in range(nr + 1, nr + 4) :
                if i >= N or board[i][nc] == 1 :
                    break
                if not visited[i][nc][nd] :
                    visited[i][nc][nd] = True
                    queue.append((i, nc, nd, cnt + 1))
        else :
            i = nr - 1
            for i in range(nr - 1, nr - 4, -1) :
                if i < 0 or board[i][nc] == 1 :
                    break
                if not visited[i][nc][nd] :
                    visited[i][nc][nd] = True
                    queue.append((i, nc, nd, cnt + 1))
                i -= 1

        #Turn dir :
        if nd < 2 :
            dir_one = 2
            dir_two = 3
        else :
            dir_one = 0
            dir_two = 1
        if not visited[nr][nc][dir_one] :
            visited[nr][nc][dir_one] = True
            queue.append((nr, nc, dir_one, cnt + 1))
        if not visited[nr][nc][dir_two] :
            visited[nr][nc][dir_two] = True
            queue.append((nr, nc, dir_two, cnt + 1))
        # print(queue)

print(bfs(SR - 1, SC - 1, SD - 1))