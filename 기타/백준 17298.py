import sys, copy
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

ans = []
stack = []

while A :
    now = A.pop()
    while stack :
        if now < stack[-1] :
            break
        stack.pop()
    if not stack :
        ans.append(-1)
    else :
        ans.append(stack[-1])
    stack.append(now)

while ans :
    a = ans.pop()
    print(a, end=" ")