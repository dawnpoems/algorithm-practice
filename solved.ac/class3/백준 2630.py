import sys
input = sys.stdin.readline

n = int(input())

board = []
for i in range(n) :
    board.append(list(map(int, input().split())))

white = 0
black = 0

def cnt_black_or_white(n) :
    global white
    global black
    
    if (n == 0) :
        white += 1
    elif (n == 1) :
        black += 1

def find_board(row, col, len) :
    start = board[row][col]
    if (len == 1) :
        # print(row, end=",")
        # print(col, end="|")
        # print(len)
        cnt_black_or_white(start)
        return
    for r in range(row, row + len) :
        for c in range(col, col + len) :
            if board[r][c] != start :
                find_board(row, col, len // 2)
                find_board(row + len // 2, col, len // 2)
                find_board(row, col + len // 2, len // 2)
                find_board(row + len // 2, col + len // 2, len // 2)
                return
    # print(row, end=",")
    # print(col, end="|")
    # print(len)
    cnt_black_or_white(start)
        
find_board(0, 0, n)
print(white)
print(black)