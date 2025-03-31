import sys
input = sys.stdin.readline

N = int(input())

trees = list(map(int, input().split()))
grows = list(map(int, input().split()))

lst = []

for i in range(N) :
    lst.append((grows[i], trees[i]))
    
lst.sort()

ans = 0

for i in range(N) :
    ans += lst[i][0] * i + lst[i][1]

print(ans)


    




        