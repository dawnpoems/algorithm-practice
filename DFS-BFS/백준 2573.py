import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

board = []

for i in range(n) :
    board.append(list(map(int, input().split())))

bada = []

def melt(i, j, n, m) :
    cnt = 0
    if i - 1 >= 0 and board[i-1][j] == 0 :
        cnt += 1
    if i + 1 < n and board[i+1][j] == 0 :
        cnt += 1
    if j - 1 >= 0 and board[i][j-1] == 0 :
        cnt += 1
    if j + 1 < m and board[i][j+1] == 0 :
        cnt += 1
    
    bada.append((i, j, cnt))

def dfs(r, c, n, m) :

    if r <= 0 or r >= n-1 or c <= 0 or c >= m-1 :
        return False
    
    if board[r][c] != 0 and not visited[r][c] :
        visited[r][c] = True
        melt(r, c, n, m)

        dfs(r + 1, c, n, m)
        dfs(r - 1, c, n, m)
        dfs(r, c + 1, n, m)
        dfs(r, c - 1, n, m)
        return True
    return False


time = -1
found_flag = False

while True :
    end_flag = True
    time += 1
    visited = [[False] * m for _ in range(n)]
    piece_cnt = 0

    for i in range(1, n-1) :
        if found_flag :
            break
        for j in range(1, m-1) :
            if board[i][j] != 0 and not visited[i][j] :
                if piece_cnt > 0 :
                    found_flag = True
                    break
                else :
                    if dfs(i, j, n, m) :
                        piece_cnt += 1
                        end_flag = False
    
    # print("------")
    # print(found_flag, end_flag)
    # print("board")
    # for row in board :
    #     print(" ".join(map(str, row)))
    
    # print("bada")
    # print(bada)

    if found_flag or end_flag :
        break

    while bada :
        r, c, cnt = bada.pop()
        board[r][c] -= cnt
        if board[r][c] < 0 :
            board[r][c] = 0

# print("answer = ", end="")
if found_flag :
    print(time)
else :
    print(0)