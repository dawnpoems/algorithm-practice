import sys
n = int(sys.stdin.readline())

scores = [0]

for i in range(n):
    scores.append(int(sys.stdin.readline()))

d = [0] * (n+1)

if n == 1:
    print(scores[1])
elif n == 2:
    print(scores[1] + scores[2])
else:

    d[1] = scores[1]
    d[2] = scores[1] + scores[2]

    for i in range(3, n+1):
        d[i] = max(d[i-2], d[i-3] + scores[i-1]) + scores[i]

    print(d[n])
