import sys

n = int(input())
queue = []

for i in range(n):
    saying = sys.stdin.readline().split()
    if saying[0] == "push":
        queue.append((int(saying[1])))
    elif saying[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))

    elif saying[0] == "size":
        print(len(queue))
    elif saying[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif saying[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif saying[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
