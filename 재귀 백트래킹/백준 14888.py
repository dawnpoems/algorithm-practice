import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

plus, minus, mult, div = map(int, input().split())

ans_min = 10 ** 9
ans_max = (-1) * ans_min

def backtracking(plus, minus, mult, div, now, depth) :
    global ans_min
    global ans_max
    if depth == N:
        if (ans_min > now) :
            ans_min = now
        if (ans_max < now) :
            ans_max = now
        return
    if plus > 0 :
        backtracking(plus - 1, minus, mult, div, now + nums[depth], depth + 1)
    if minus > 0 :
        backtracking(plus, minus - 1, mult, div, now - nums[depth], depth + 1)
    if mult > 0 :
        backtracking(plus, minus, mult - 1, div, now * nums[depth], depth + 1)
    if div > 0 :
        ret = now // nums[depth]
        if now < 0 and nums[depth] > 0 :
            ret = ((-now) // nums[depth]) * (-1) 
        backtracking(plus, minus, mult, div -  1, ret, depth + 1)

backtracking(plus, minus, mult, div, nums[0], 1)

print(ans_max)
print(ans_min)