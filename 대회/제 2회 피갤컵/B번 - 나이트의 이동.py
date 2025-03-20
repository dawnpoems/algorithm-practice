import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())

R, C = map(int, input().split())

can_move = False

nr = [-2, -2, -1, -1, +1, +1, +2, +2]
nc = [-1, +1, -2, +2, -2, +2, -1, +1]
for i in range(8) :
    if 0 < R + nr[i] <= N and 0 < C + nc[i] <= N :
        can_move = True
        break

if can_move == False :
    print(1)
else :
    if N % 2 == 1 and (R + C) % 2 == 0:
        print(N * N // 2 + 1)
    else : 
        print(N * N // 2)

# visited = [[False] * N for _ in range(N)]

# ans = 0

# def bruteforce(r, c, depth) :
#     visited[r - 1][c - 1] = True
#     global ans
#     if depth >= 2 :
#         depth = 0
#         ans += 1

#     nr = [-2, -2, -1, -1, +1, +1, +2, +2]
#     nc = [-1, +1, -2, +2, -2, +2, -1, +1]
#     for i in range(8) :
#         if 0 < r + nr[i] <= N and 0 < c + nc[i] <= N and visited[r + nr[i] - 1][c + nc[i] - 1] == False:
#             bruteforce(r + nr[i], c + nc[i], depth + 1)

# bruteforce(R, C, 2)

# print(ans)