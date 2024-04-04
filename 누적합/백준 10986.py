import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

mods = [0] * M

total = 0
for num in nums :
    total += num
    mods[total % M] += 1

ans = mods[0]

for i in range(M) :
    ans += (mods[i] - 1) * mods[i] // 2
    
print(ans)