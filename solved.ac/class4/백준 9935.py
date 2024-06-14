import sys
input = sys.stdin.readline

string = list(input().strip())
bomb = list(input().strip())

ans = []
dp = [-1]

for s in string :
    ans.append(s)
    if s == bomb[dp[-1] + 1] :
        dp.append(dp[-1] + 1)
        if dp[-1] == len(bomb) - 1 :
            for i in range(len(bomb)) :
                ans.pop()
                dp.pop()
    elif s == bomb[0] :
        dp.append(0)
    else :
        dp.append(-1)

if ans :
    print(*ans, sep="")
else :
    print("FRULA")