import sys
input = sys.stdin.readline

N = int(input())

blocks = []
for i in range(N) :
    blocks.append(int(input()))

stack = []
ans = 0
for i in range(N) :
    while stack and stack[-1][1] > blocks[i] :
        idx, hei = stack.pop()
        if stack :
            wid = i - stack[-1][0] - 1
        else :
            wid = i
        # print(hei, wid)
        ans = max(ans, hei * wid)
    stack.append((i, blocks[i]))
    # print(stack)

# print('--------------')
while stack:
    idx, hei = stack.pop()
    if stack :
        wid = N - stack[-1][0] -1
    else :
        wid = N
    # print(hei, wid)
    # print(stack)
    ans = max(ans, hei * wid)

print(ans)