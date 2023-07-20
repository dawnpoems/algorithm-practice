import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())


def dfs(board, r, c) :
    if r < 0 or c < 0 or r >= n or c >= m :
        return False
    if board[r][c] == 1 :
        board[r][c] = 0
        dfs(board, r-1, c)
        dfs(board, r+1, c)
        dfs(board, r, c-1)
        dfs(board, r, c+1)
        return True
    return False


for i in range(t) :
    m, n, k = map(int, input().split())

    board = [[0] * m for _ in range(n)]

    for j in range(k) :
        c, r = map(int, input().split())
        board[r][c] = 1
    
    cnt = 0
    for nn in range(n) :
        for mm in range(m) :
            if dfs(board, nn, mm) :
                cnt += 1
    
    print("-----")
    print(board)
    print(cnt)


    