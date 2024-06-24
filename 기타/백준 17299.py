import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

ans = []
stack = []

table = dict()

for a in A :
    if not table.get(a) :
        table[a] = 1
    else :
        table[a] += 1

while A :
    now = A.pop()
    while stack :
        if table[now] < table[stack[-1]] :
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