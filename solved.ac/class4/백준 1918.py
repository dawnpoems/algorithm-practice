import sys
input = sys.stdin.readline

line = list(input().strip())
stack = []
now_stack = []

for c in line :
    if c == '(' :
        stack.append(now_stack)
        now_stack = []
    elif c == ')':
        while now_stack :
            print(now_stack.pop(), end="")
        now_stack = stack.pop()
    elif c == '*' or c == '/':
        while now_stack and (now_stack[-1] == '*' or now_stack[-1] == "/") :
                print(now_stack.pop(), end="")
        now_stack.append(c)
    elif c == '+' or c == '-' :
        while now_stack :
            print(now_stack.pop(), end="")
        now_stack.append(c)
    else :
        print(c, end="")

while now_stack :
        print(now_stack.pop(), end="")

while stack :
    now_stack = stack.pop()
    while now_stack :
        print(now_stack.pop(), end="")

print()