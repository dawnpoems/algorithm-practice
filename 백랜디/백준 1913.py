import sys
input = sys.stdin.readline

N = int(input())

target = int(input())

board = [[0] * N for _ in range(N)]

pos = -1

def put_idx(r, c) :
    global idx
    global target
    global pos
    idx += 1
    board[r][c] = idx
    if idx == target :
        pos = (r + 1, c + 1)

mid = N // 2
r = mid
c = mid
idx = 0
put_idx(r, c)
for i in range(1, N // 2 + 1) :
    r -= 1
    put_idx(r, c)
    while c < mid + i:
        c += 1
        put_idx(r, c)
    while r < mid + i :
        r += 1
        put_idx(r, c)
    while c > mid - i :
        c -= 1
        put_idx(r, c)
    while r > mid - i :
        r -= 1
        put_idx(r, c)

for b in board :
    print(*b)

print(*pos)