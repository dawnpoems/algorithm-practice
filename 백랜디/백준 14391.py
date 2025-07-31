import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for i in range(N) :
    board.append(list(map(int, list(input().strip()))))

pieces = [[0] * M for _ in range(N)]
cases = [[-1] * M for _ in range(N)]

ans = 0

def backTracking(r, c, case) :
    print(r, c, case)
    global ans
    if r == N - 1 and c == M - 1 :
        print('---------')
        print("case---")
        for c in cases :
            print(*c)
        print("pieces---")
        for p in pieces :
            print(*p)
        now_sum = sum(sum(p) for p in pieces)
        if now_sum > ans :
            print(now_sum)
            ans = now_sum
        return
    nr = r + 1
    nc = c
    if nr >= N :
        nc = c + 1
        nr -= N

    # 새로 시작한 경우
    cases[r][c] = 0
    pieces[nr][nc] = board[nr][nc]
    backTracking(nr, nc)
    cases[r][c] = prev_cases

    # 위쪽꺼 붙인 경우
    if nr > 0 and (cases[nr - 1][nc] == 0 or cases[nr - 1][nc] == 1) :
        backTracking(nr, nc, 1)
    # 왼쪽꺼 붙인 경우
    if nc > 0 and (cases[nr][nc - 1] == 0 or cases[nr][nc - 1] == 2) :
        backTracking(nr, nc, 2)

backTracking(0, 0, 0)
print(ans)