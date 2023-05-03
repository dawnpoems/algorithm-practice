import sys
n = int(sys.stdin.readline())

case = []

for i in range(n):
    case.append(int(sys.stdin.readline()))


answer = [[0, 0] for _ in range(41)]


answer[0] = [1, 0]
answer[1] = [0, 1]

for j in case:
    for i in range(2, j + 1):
        answer[i][0] = answer[i-1][0] + answer[i-2][0]
        answer[i][1] = answer[i-1][1] + answer[i-2][1]
    print(" ".join(map(str, answer[j])))
