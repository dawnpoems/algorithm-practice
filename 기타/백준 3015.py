import sys
input = sys.stdin.readline

N = int(input())

people = []
for i in range(N) :
    people.append(int(input()))

stack = []
ans = 1
for i in range(N) :
    while stack and stack[-1][1] > people[i] :
        idx, hei = stack.pop()
    ans += len(stack)
    stack.append((i, people[i]))

# ans += len(stack)

print(ans)