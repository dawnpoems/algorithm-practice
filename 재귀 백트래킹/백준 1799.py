import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

board = []
N = int(input())

for i in range(N) :
    board.append(list(map(int, input().split())))
    
def is_ok(r, c, board) :
    i = r - 1
    j = c - 1
    while i >= 0 and j >= 0 :
        if board[i][j] == 2 :
            return False
        i -= 1
        j -= 1
    i = r - 1
    j = c + 1
    while i >= 0 and j < N :
        if board[i][j] == 2 :
            return False
        i -= 1
        j += 1
        
    return True

ans_black = 0

def backtracking_black(r, c, board, cnt) :
    global ans_black
    if r >= N :
        ans_black = max(ans_black, cnt)
        return
    next_r, next_c = r, c + 2
    if next_c >= N :
        next_r += 1
        next_c = next_r % 2
    if board[r][c] == 1 and is_ok(r, c, board):
        board[r][c] = 2
        backtracking_black(next_r, next_c, board, cnt + 1)
        board[r][c] = 1
    backtracking_black(next_r, next_c, board, cnt)

ans_white = 0

def backtracking_white(r, c, board, cnt) :
    global ans_white
    if r >= N :
        ans_white = max(ans_white, cnt)
        return
    next_r, next_c = r, c + 2
    if next_c >= N :
        next_r += 1
        next_c = 0
        if next_r % 2 == 0 :
            next_c = 1
    if board[r][c] == 1 and is_ok(r, c, board):
        board[r][c] = 2
        backtracking_white(next_r, next_c, board, cnt + 1)
        board[r][c] = 1
    backtracking_white(next_r, next_c, board, cnt)

backtracking_black(0, 0, board, 0)
backtracking_white(0, 1, board, 0)
print(ans_black + ans_white)