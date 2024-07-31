import sys
input = sys.stdin.readline

ans = 0

N = int(input())

def get_happiness(n) :
    global ans
    if n <= 1 :
        return
    half = n // 2
    ans += half * (n - half)
    get_happiness(half)
    get_happiness(n - half)

get_happiness(N)
print(ans)