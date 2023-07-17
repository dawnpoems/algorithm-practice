import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

board = []

for i in range(n) :
    board.append(list(map(int, input().split())))

def melt(i, j, n, m) :
    if i - 1 >= 0 and new_board[i-1][j] > 0:
        new_board[i - 1][j] -= 1
    if i + 1 < n and new_board[i+1][j] > 0:
        new_board[i + 1][j] -= 1
    if j - 1 >= 0 and new_board[i][j - 1] > 0:
        new_board[i][j - 1] -= 1
    if j + 1 < m and new_board[i][j + 1] > 0:
        new_board[i][j + 1] -= 1

def dfs(r, c, n, m) :
    if r < 0 or r >= n or c < 0 or c >= m :
        return False

    if new_board[r][c] != 0 :
        new_board[r][c] = 0
        dfs(r + 1, c, n, m)
        dfs(r - 1, c, n, m)
        dfs(r, c + 1, n, m)
        dfs(r, c - 1, n, m)
        return True
    return False


time = 0
end_flag = False
broke_flag = False

while not end_flag :
    new_board = copy.deepcopy(board)
    end_flag = True

    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 0 :
                melt(i, j, n, m)
            else :
                end_flag = False

    board = copy.deepcopy(new_board)

    time += 1
    mass = 0

    # print("-------")

    # for row in new_board :
    #     print(" ".join(map(str, row)))

    for i in range(n) :
        for j in range(m) :
            if dfs(i, j, n, m) :
                mass += 1
    if mass >= 2 :
        break

print(time)