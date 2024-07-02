import sys
input = sys.stdin.readline

def oper_one(n) :
    global board
    row = len(board)
    n %= 2
    if n == 0 :
        return
    ans = []
    for i in range(row) :
        ans.append(board[row - i - 1])
    board = ans

def oper_two(n) :
    global board
    row = len(board)
    n %= 2
    if n == 0 :
        return
    ans = []
    for i in range(row) :
        ans.append(list(reversed(board[i])))
    board = ans

def oper_three(n) :
    global board
    n %= 4
    for num in range(n) :
        row = len(board)
        col = len(board[0])
        ans = [[0] * row for _ in range(col)]
        for i in range(row) :
            for j in range(col) :
                ans[j][row - i - 1] = board[i][j]
        board = ans

def oper_four(n) :
    global board
    n %= 4
    for num in range(n) :
        row = len(board)
        col = len(board[0])
        ans = [[0] * row for _ in range(col)]
        for i in range(row) :
            for j in range(col) :
                ans[col - 1 - j][i] = board[i][j]
        board = ans

def oper_five(n) :
    global board
    n %= 4
    row = len(board)
    col = len(board[0])
    mr = row // 2
    mc = col // 2
    for num in range(n) :
        ans = [[0] * col for _ in range(row)]
        for i in range(row // 2) :
            for j in range(col // 2) :
                ans[i][mc + j] = board[i][j]
                ans[mr + i][mc + j] = board[i][mc + j]
                ans[mr + i][j] = board[mr + i][mc + j]
                ans[i][j] = board[mr + i][j]
        board = ans

def oper_six(n) :
    global board
    n %= 4
    row = len(board)
    col = len(board[0])
    mr = row // 2
    mc = col // 2
    for num in range(n) :
        ans = [[0] * col for _ in range(row)]
        for i in range(row // 2) :
            for j in range(col // 2) :
                ans[mr + i][j] = board[i][j]
                ans[mr + i][mc + j] = board[mr + i][j]
                ans[i][mc + j] = board[mr + i][mc + j]
                ans[i][j] = board[i][mc + j]
        board = ans

def operate(op, cnt) :
    if op == 1 :
        oper_one(cnt)
    elif op == 2 :
        oper_two(cnt)
    elif op == 3 :
        oper_three(cnt)
    elif op == 4 :
        oper_four(cnt)
    elif op == 5 :
        oper_five(cnt)
    elif op == 6 :
        oper_six(cnt)
    
N, M, R = map(int, input().split())

board = []
for i in range(N) :
    board.append(list(map(int, input().split())))

OPS = list(map(int, input().split()))
cnt = 0
now = 0
for op in OPS :
    if op == now :
        cnt += 1
    else :
        if cnt :
            operate(now, cnt)
        cnt = 1
        now = op

operate(now, cnt)

for b in board :
    print(*b)
