import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):

    Parenthesis = list(sys.stdin.readline())

    result = True

# 조건1 : 갯수가 맞아야 함.
    if (Parenthesis.count("(") != Parenthesis.count(")")):
        result = False

    count = 0
    # 조건2 : 왼쪽에 '(' 갯수를 넘는 ')'이 한번이라도 오른쪽에 있으면 안됨.
    for i in Parenthesis:
        if i == "(":
            count += 1

        elif i == ")":
            count -= 1

        if count < 0:
            result = False

    if result == True:
        print("YES")
    else:
        print("NO")
