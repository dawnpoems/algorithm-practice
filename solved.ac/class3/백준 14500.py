import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []

for i in range(n) :
    board.append(list(map(int, input().split())))

max_num = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(board, v, total) :
    global max_num
    if visited[v[0]][v[1]] >= 4 :
        if max_num < total :
            max_num = total
        return
    else :
        for i in range(4) :
            nr = v[0] + dr[i]
            nc = v[1] + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m :
                continue
            if visited[nr][nc] == 0 :
                visited[nr][nc] = visited[v[0]][v[1]] + 1
                dfs(board, (nr, nc), total + board[nr][nc])
                visited[nr][nc] = 0

def check_cross(v) :
        global max_num
        cross_list = []
        cross_total = board[i][j]
        for b in range(4) :
            nr = i + dr[b]
            nc = j + dc[b]
            if nr < 0 or nr >= n or nc < 0 or nc >= m :
                continue
            cross_total += board[nr][nc]
            cross_list.append(board[nr][nc])
        
        if len(cross_list) == 3 :
            if max_num < cross_total :
                max_num = cross_total
        elif len(cross_list) == 4 :
            for c in range(4) :
                nr = i + dr[c]
                nc = j + dc[c]
                cross_total -= board[nr][nc]
                if max_num < cross_total :
                    max_num = cross_total
                cross_total += board[nr][nc]

visited = [[0] * m for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        visited[i][j] = 1
        dfs(board, (i, j), board[i][j])
        visited[i][j] = 0
        check_cross((i,j))

print(max_num)