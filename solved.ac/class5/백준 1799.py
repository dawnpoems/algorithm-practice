import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

board = []
rc = [0, 0]
total = 0

n = int(input())

for i in range(n) :
    board.append(list(map(int, input().split())))

def find_zero(r) :
    for i in range(r, n) :
        for j in range(n) :
            if board[i][j] == 0 :
                rc[0] = i
                rc[1] = j
                return True
    return False

def is_valid(row, col, num) :
    for i in range(9) :
        if board[i][col] == num :
            return False
        if board[row][i] == num :
            return False
    for j in range(3) :
        for k in range(3) :
            if board[(row // 3)*3 + j][(col // 3)*3 + k] == num:
                return False
    return True

def dfs(r) :
    global total
    if not find_zero(r) :
        total += 1
        return
    row = rc[0]
    col = rc[1]
    if is_valid(row, col, i):
        board[row][col] = i
        dfs(row)
        board[row][col] = 0
# print("--------")
dfs(0)