import sys

n = int(input())
stack = []

for i in range(n):
    saying = sys.stdin.readline().split()
    if saying[0] == "push":
        stack.append(int(saying[1]))
    elif saying[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif saying[0] == "size":
        print(len(stack))
    elif saying[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif saying[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
