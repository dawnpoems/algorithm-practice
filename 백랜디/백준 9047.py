import sys
input = sys.stdin.readline

N = int(input())

for i in range(N) :
    ans = 0
    now = int(input())
    while now != 6174:
        lst = []
        for i in range(4) :
            lst.append(now % 10)
            now //= 10
        # print("lst :", lst)
        lst.sort()
        mn = 0
        for i in range(4) :
            mn *= 10
            mn += lst[i]
        mx = 0
        for i in range(3, -1, -1) :
            mx *= 10
            mx += lst[i]
        now = mx - mn
        # print(mx, mn, now)
        ans += 1
    print(ans)

