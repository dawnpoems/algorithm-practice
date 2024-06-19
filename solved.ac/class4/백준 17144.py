import sys, copy
input = sys.stdin.readline

R, C, T = map(int, input().split())
board = []

for i in range(R) :
    line = list(map(int, input().split()))
    if line[0] == -1 :
        puri = i
    board.append(line)

def spread() :
    global R, C
    result = copy.deepcopy(board)
    for r in range(R) :
        for c in range(C) :
            if board[r][c] <= 0 :
                continue
            spreaded = board[r][c] // 5
            if r - 1 >= 0 and board[r - 1][c] >= 0 :
                result[r - 1][c] += spreaded
                result[r][c] -= spreaded
            if c - 1 >= 0 and board[r][c - 1] >= 0 :
                result[r][c - 1] += spreaded
                result[r][c] -= spreaded
            if r + 1 < R and board[r + 1][c] >= 0 :
                result[r + 1][c] += spreaded
                result[r][c] -= spreaded
            if c + 1 < C and board[r][c + 1] >= 0 :
                result[r][c + 1] += spreaded
                result[r][c] -= spreaded
    return result

def air_purify_up(result) :
    global puri, R, C
    up_puri = puri - 1
    r = up_puri - 1
    c = 0
    while r - 1 >= 0 :
        result[r][c] = result[r - 1][c]
        r -= 1
    r = 0
    while c < C - 1 :
        result[r][c] = result[r][c + 1]
        c += 1
    c = C - 1
    while r + 1 <= up_puri :
        result[r][c] = result[r + 1][c]
        r += 1
    r = up_puri
    while c - 1 > 0 :
        result[r][c] = result[r][c - 1]
        c -= 1
    result[up_puri][1] = 0
    
def air_purify_down(result) :
    global puri, R, C
    r = puri + 1
    c = 0
    while r + 1 < R :
        result[r][c] = result[r + 1][c]
        r += 1
    r = R - 1
    while c + 1 < C :
        result[r][c] = result[r][c + 1]
        c += 1
    c = C - 1
    while r - 1 >= puri :
        result[r][c] = result[r - 1][c]
        r -= 1
    r = puri
    while c - 1 > 0 :
        result[r][c] = result[r][c - 1]
        c -= 1
    result[puri][1] = 0

t = 0
while t < T :
    board = spread()
    # print("------------")
    # for b in board :
    #     print(*b)
    air_purify_up(board)
    # print("------------")
    # for b in board :
    #     print(*b)
    air_purify_down(board)
    # print("------------")
    # for b in board :
    #     print(*b)
    t += 1

# print("------------")
# for b in board :
#     print(*b)


print(sum(sum(row) for row in board) + 2)