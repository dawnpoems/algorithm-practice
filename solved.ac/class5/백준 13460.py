import sys
input = sys.stdin.readline
    
def up(red_r, red_c, blue_r, blue_c) :
    rr = red_r
    rc = red_c
    br = blue_r
    bc = blue_c
    while board[rr][rc] == 0 :
        rr -= 1
    while board[br][bc] == 0 :
        br -= 1
    
    if board[rr][rc] == 2 or board[br][bc] == 2 :
        return rr, rc, br, bc
    
    if board[rr][rc] == 1 :
        rr += 1
    if board[br][bc] == 1 :
        br += 1
    
    if rr == br and rc == bc :
        if red_r < blue_r :
            br += 1
        else :
            rr += 1
    
    return rr, rc, br, bc

def down(red_r, red_c, blue_r, blue_c) :
    rr = red_r
    rc = red_c
    br = blue_r
    bc = blue_c
    while board[rr][rc] == 0 :
        rr += 1
    while board[br][bc] == 0 :
        br += 1
        
    if board[rr][rc] == 2 or board[br][bc] == 2 :
        return rr, rc, br, bc
    
    if board[rr][rc] == 1 :
        rr -= 1
    if board[br][bc] == 1 :
        br -= 1
    
    if rr == br and rc == bc :
        if red_r > blue_r :
            br -= 1
        else :
            rr -= 1
    
    return rr, rc, br, bc

def left(red_r, red_c, blue_r, blue_c) :
    rr = red_r
    rc = red_c
    br = blue_r
    bc = blue_c
    while board[rr][rc] == 0 :
        rc -= 1
    while board[br][bc] == 0 :
        bc -= 1
        
    if board[rr][rc] == 2 or board[br][bc] == 2 :
        return rr, rc, br, bc
    
    if board[rr][rc] == 1 :
        rc += 1
    if board[br][bc] == 1 :
        bc += 1
    
    if rr == br and rc == bc :
        if red_c < blue_c :
            bc += 1
        else :
            rc += 1
    
    return rr, rc, br, bc

def right(red_r, red_c, blue_r, blue_c) :
    rr = red_r
    rc = red_c
    br = blue_r
    bc = blue_c
    while board[rr][rc] == 0 :
        rc += 1
    while board[br][bc] == 0 :
        bc += 1
    
    if board[rr][rc] == 2 or board[br][bc] == 2 :
        return rr, rc, br, bc
    
    if board[rr][rc] == 1 :
        rc -= 1
    if board[br][bc] == 1 :
        bc -= 1
    
    if rr == br and rc == bc :
        if red_c > blue_c :
            bc -= 1
        else :
            rc -= 1
    
    return rr, rc, br, bc

ans = 20

def backtracking(udlr, depth, red_r, red_c, blue_r, blue_c) :
    global ans
    
    if depth > 10 :
        return
    if udlr == 0 :
        rr, rc, br, bc = up(red_r, red_c, blue_r, blue_c)
    elif udlr == 1 :
        rr, rc, br, bc = down(red_r, red_c, blue_r, blue_c)
    elif udlr == 2 :
        rr, rc, br, bc = left(red_r, red_c, blue_r, blue_c)
    elif udlr == 3:
        rr, rc, br, bc = right(red_r, red_c, blue_r, blue_c)
    
    if Hole[0] == br and Hole[1] == bc :
        return
    if Hole[0] == rr and Hole[1] == rc :
        ans = min(ans, depth)
        return
    backtracking(0, depth + 1, rr, rc, br, bc)
    backtracking(1, depth + 1, rr, rc, br, bc)
    backtracking(2, depth + 1, rr, rc, br, bc)
    backtracking(3, depth + 1, rr, rc, br, bc)

N, M = map(int, input().split())

board = []

for i in range(N) :
    line = list(input().strip())
    col = []
    for j in range(M) :
        l = line[j]
        if l == "#" :
            col.append(1)
        elif l == "." :
            col.append(0)
        elif l == "O" :
            col.append(2)
            Hole = (i, j)
        elif l == "R" :
            col.append(0)
            RED = (i, j)
        else :
            col.append(0)
            BLUE = (i, j)
    board.append(col)


for b in board :
    print(*b)

backtracking(0, 1, RED[0], RED[1], BLUE[0], BLUE[1])
backtracking(1, 1, RED[0], RED[1], BLUE[0], BLUE[1])
backtracking(2, 1, RED[0], RED[1], BLUE[0], BLUE[1])
backtracking(3, 1, RED[0], RED[1], BLUE[0], BLUE[1])

if ans == 20 :
    print(-1)
else :
    print(ans)