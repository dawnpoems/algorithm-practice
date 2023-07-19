import sys
input = sys.stdin.readline

n = int(input())

stack = []

num = 1
answers = []
no_flag = False

for i in range(n) :
    target = int(input())
    if no_flag :
        break
    while True :
        if len(stack) == 0 or stack[-1] < target :
            if num > target :
                no_flag = True
                break
            stack.append(num)
            num += 1
            answers.append("+")
        elif stack[-1] == target :
            stack.pop()
            answers.append("-")
            break
        elif stack[-1] > target :
            stack.pop()
            answers.append("-")

    # print("------")
    # print(target)
    # print(stack)

if no_flag :
    print("NO")
else :
    print("\n".join(answers))