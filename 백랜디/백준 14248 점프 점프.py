import sys
input = sys.stdin.readline

N = int(input())

stones = list(map(int, input().split()))

start = int(input())



visited = [False] * N

def dfs(now) :
    if not visited[now] :
        visited[now] = True
    # print("in : ", now, jumped_left, jumped_right)
    left = now - stones[now]
    right = now + stones[now]
    # print("lr : ", left, right)s
    if left >= 0 and not visited[left]:
        dfs(left)
    if right < N and not visited[right]:
        dfs(right)

dfs(start - 1)

# print(visited)

ans = 0
for v in visited :
    if v :
        ans += 1
print(ans)