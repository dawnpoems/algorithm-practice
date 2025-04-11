import sys
input = sys.stdin.readline

board = []

for i in range(12) :
    line = []
    line_str = list(input().strip())
    for j in range(6) :
        if line_str[j] == "R" :
            line.append(1)
        elif line_str[j] == "G" :
            line.append(2)
        elif line_str[j] == "B" :
            line.append(3)
        elif line_str[j] == "P" :
            line.append(4)
        elif line_str[j] == "Y" :
            line.append(5)
        else :
            line.append(0)
    board.append(line)

# print("---------------")
# for i in range(12) :
#     print(*board[i])

gr = [-1, 1, 0, 0]
gc = [0, 0, -1, 1]

def dfs(r, c, color, linked) :
    linked.append((r, c))
    visited[r][c] = True
    for i in range(4) :
        nr = r + gr[i]
        nc = c + gc[i]
        if 0 <= nr < 12 and 0 <= nc < 6 and board[nr][nc] > 0 and board[nr][nc] == color and not visited[nr][nc] :
            dfs(nr, nc, color, linked)

def puyo() :
    poped = False
    for i in range(12) :
        for j in range(6) :
            if board[i][j] > 0 and not visited[i][j] :
                linked = []
                dfs(i, j, board[i][j], linked)
                if len(linked) >= 4 :
                    poped = True
                    for l in linked :
                        board[l[0]][l[1]] = 0
    return poped

# print("---------------")
# for i in range(12) :
#     print(*board[i])

def fall() :
    for col in range(6) :
        vert = []
        for row in range(11, -1, -1) :
            if board[row][col] > 0 :
                vert.append(board[row][col])
                board[row][col] = 0
            board[row][col] == 0
        for v in range(len(vert)) :
            board[11 - v][col] = vert[v]



ans = 0
while True :
    visited = [[False] * 6 for _ in range(12)]
    if not puyo() :
        break
    ans += 1
    fall()

print(ans)


