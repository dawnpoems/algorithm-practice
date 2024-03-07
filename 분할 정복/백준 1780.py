import sys
input=sys.stdin.readline

N = int(input())

board = []
for i in range(N) :
    board.append(list(map(int, input().split())))

zero = 0
one = 0
minus = 0

def is_same(r, c, scale) :
    num = board[r][c]
    for i in range(r, r + scale) :
        for j in range(c, c + scale) :
            if board[i][j] != num :
                return 2
    return num

def count_glob(num) :
    global zero
    global one
    global minus
    if num == 0 :
        zero += 1
    elif num == 1 :
        one += 1
    elif num == -1 :
        minus += 1

def div_conquest(r, c, scale) :
    if (scale == 1) :
        count_glob(board[r][c])
        return
    num = is_same(r, c, scale)
    if num != 2 :
        count_glob(num)
    else :
        div_conquest(r, c, scale // 3)
        div_conquest(r, c + scale // 3, scale // 3)
        div_conquest(r, c + scale * 2 // 3, scale // 3)
        div_conquest(r + scale // 3, c, scale // 3)
        div_conquest(r + scale // 3, c + scale // 3, scale // 3)
        div_conquest(r + scale // 3, c + scale * 2 // 3, scale // 3)
        div_conquest(r + scale * 2 // 3, c, scale // 3)
        div_conquest(r + scale * 2 // 3, c + scale // 3, scale // 3)
        div_conquest(r + scale * 2 // 3, c + scale * 2 // 3, scale // 3)

div_conquest(0, 0, N)
print(minus, zero, one)