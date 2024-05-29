import sys, copy
input = sys.stdin.readline

N = int(input())

board = []
for i in range(N) :
    board.append(list(map(int, input().split())))

def up(now) :
    global N
    for c in range(N) :
        top = -1
        merged = False
        for r in range(N) :
            if now[r][c] == 0 :
                continue
            if top != -1 and now[top][c] == now[r][c] and not merged :
                # print("merge! :", top, r)
                now[top][c] *= 2
                now[r][c] = 0
                merged = True
            elif r > 0 and top + 1 < r:
                top += 1
                merged = False
                # print("move! :", top, r)
                now[top][c] = now[r][c]
                now[r][c] = 0
            else :
                top = r
                merged = False
            # print(now)
    # print("-----------")

def down(now) :
    global N
    for c in range(N) :
        top = N
        merged = False
        for r in range(N - 1, -1, -1) :
            if now[r][c] == 0 :
                continue
            if top != N and now[top][c] == now[r][c] and not merged :
                # print("merge! :", top, r)
                now[top][c] *= 2
                now[r][c] = 0
                merged = True
            elif r < N - 1 and top - 1 > r :
                top -= 1
                merged = False
                # print("move! :", top, r)
                now[top][c] = now[r][c]
                now[r][c] = 0
            else :
                top = r
                merged = False
            # print(now)
    # print("-----------")
    
def left(now) :
    global N
    for r in range(N) :
        top = -1
        merged = False
        for c in range(N) :
            if now[r][c] == 0 :
                continue
            if top != -1 and now[r][top] == now[r][c] and not merged :
                # print("merge! :", top, c)
                now[r][top] *= 2
                now[r][c] = 0
                merged = True
            elif c > 0 and top + 1 < c:
                top += 1
                merged = False
                # print("move! :", top, c)
                now[r][top] = now[r][c]
                now[r][c] = 0
            else :
                top = c
                merged = False
            # print(now)
    # print("-----------")

def right(now) :
    global N
    for r in range(N) :
        top = N
        merged = False
        for c in range(N - 1, -1, -1) :
            if now[r][c] == 0 :
                continue
            if top != N and now[r][top] == now[r][c] and not merged:
                # print("merge! :", top, c)
                now[r][top] *= 2
                now[r][c] = 0
                merged = True
            elif c < N - 1 and top - 1 > c :
                top -= 1
                merged = False
                # print("move! :", top, c)
                now[r][top] = now[r][c]
                now[r][c] = 0
            else :
                top = c
                merged = False
    #         print(now)
    # print("-----------")

# left(board)
# print(board)

ans_set = set()

board_list = []

def backtracking(dir, depth) :
    now = board_list[-1]
    if dir == 0 :
        up(now)
    elif dir == 1 :
        down(now)
    elif dir == 2 :
        left(now)
    else :
        right(now)
    if depth == 4 :
        ans_set.add(max(max(row) for row in now))
        return
    for i in range(4) :
        board_list.append(copy.deepcopy(now))
        backtracking(i, depth + 1)
        board_list.pop()

for i in range(4) :
    board_list.append(copy.deepcopy(board))
    backtracking(i, 0)
    board_list.pop()

# print(ans_set)
print(max(ans_set))