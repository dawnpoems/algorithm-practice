import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

board = []
wh_list = []
bl_list = []
n = int(input())
idx = 0
for i in range(n) :
    board.append(list(map(int, input().split())))


for j in range(n) :
    for i in range(n) :
        if board[i][j] == 1 :
            if (i % 2 == 0) :
                wh_list.append((i, j))
            else :
                bl_list.append((i, j))   
    idx += 1

answer = 0
rc = [0, 0]
bishop = []

def find_one(r) :
    for i in range(r, n) :
        for j in range(n) :
            if board[i][j] == 1 :
                rc[0] = i
                rc[1] = j
                return True
    return False

def is_valid(r, c) :
    # print(bishop)
    for bi in bishop :
        if board[bi[0]][bi[1]] == -1 and abs(bi[0] - r) == abs(bi[1] - c) :
            return False
    return True

def check_total(total) :
    global answer
    # total = 0
    # for i in range(n) :
        # for j in range(n) :
            # if board[i][j] == -1 :
                # total += 1
    if answer < total :
        answer = total

# def print_board() :
#     for i in range(n) :
#         print("".join(map(str, board[i])))
#     print()

#흰검흰검흰검흰검
#검흰검흰검흰검흰
#흰검흰검흰검흰검
#검흰검흰검흰검흰
#흰검흰검흰검흰검
#검흰검흰검흰검흰
#흰검흰검흰검흰검
#검흰검흰검흰검흰
# 아무튼 흰검 나눠서 해야 시간복잡도 안걸림.

def dfs(row, total) :
    if not find_one(row) :
        # print_board()
        check_total(total)
        return
    row = rc[0]
    col = rc[1]
    if is_valid(row, col):
        board[row][col] = -1
        bishop.append((row, col))
        dfs(row, total + 1)
        bishop.pop()
    board[row][col] = 2
    dfs(row, total)
    board[row][col] = 1

dfs(0, 0)
print(answer)