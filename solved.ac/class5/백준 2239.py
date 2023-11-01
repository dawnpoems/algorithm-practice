import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

board = []
rc = [0, 0]
found = False

for i in range(9) :
    board.append(list(map(int, list(input().strip()))))

def find_zero(r) :
    for i in range(r, 9) :
        for j in range(9) :
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

def print_board() :
    for i in range(9) :
        print("".join(map(str, board[i])))

def dfs(r) :
    global found
    if found :
        return
    if not find_zero(r) :
        found = True
        print_board()
        return
    row = rc[0]
    col = rc[1]
    for i in range(1, 10) :
        if is_valid(row, col, i):
            board[row][col] = i
            dfs(row)
            board[row][col] = 0
# print("--------")
dfs(0)