import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nohear = []
nosee = []

for i in range(n) :
    nohear.append(input().strip())

for j in range(m) :
    nosee.append(input().strip())

ans = list(set(nohear) & set(nosee))

print(len(ans))
ans.sort()
for an in ans :
    print(an)