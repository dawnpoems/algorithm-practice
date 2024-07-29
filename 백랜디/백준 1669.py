import sys
input = sys.stdin.readline

X, Y = map(int, input().split())

start = 0
dest = Y - X

cnt = 0
ans = 0
while True :
    # print(start, dest)
    if start + cnt * 2 + 1 > dest :
        break
    start += cnt * 2 + 1
    ans = cnt * 2 + 1
    cnt += 1

# print(start, dest, cnt)

while cnt :
    while start + cnt <= dest :
        start += cnt
        ans += 1
    if start == dest :
        break
    cnt -= 1

print(ans)