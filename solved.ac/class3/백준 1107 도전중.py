import sys, math
input = sys.stdin.readline

channel = input().strip()
c = len(channel) - 1
dest = int(channel)

M = int(input())
if (M) :
    brock = list(map(int, input().split()))
else :
    brock = []

one = min(abs(dest - 100), abs(100 - dest))

cnt = 0
ans = 0
num = 0

print(brock)

while (c >= 0) :
    num *= 10
    cnt += 1
    now = dest / (10 ** c)
    flo = math.floor(now)
    print("flo :", end=" ")
    print(flo)
    if flo not in brock :
        dest -= flo * (10 ** c)
        c -= 1
        num += flo
        print(num)
        continue
    i = 1
    while (flo - i >= 0 or flo + i < 10) :
        # cnt += 1
        up = -1
        down = -1
        if flo - i >= 0 and flo - i not in brock :
            up = flo - i
        if flo + i < 10 and flo + i not in brock :
            down = flo + i
        if up == -1 and down != -1 :
            num += down
            break
        elif up != -1 and down == -1 :
            num += up
            break
        elif up != -1 and down != -1 :
            if (round(now) > flo) :
                num += up
            else :
                num += down
            break
        i += 1
    dest -= flo * (10 ** c)
    print(num)
    c -= 1

print(min(one, cnt + abs(int(channel) - num)))