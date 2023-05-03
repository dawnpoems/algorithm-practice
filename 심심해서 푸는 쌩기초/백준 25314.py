import sys
n = int(sys.stdin.readline())

answer = ""
while n >= 4:
    n = n - 4
    answer += "long "

answer += "int"

print(answer)
