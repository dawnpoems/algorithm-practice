import sys
input = sys.stdin.readline

N, K = map(int, input().split())

abilitis = []

for i in range(N) :
    a, b, c = map(int, input().split())
    one = a + b
    two = b + c
    three = a + c
    abilitis.append((one, two, three))

one_s = sorted(abilitis, key=lambda x : -x[0])
two_s = sorted(abilitis, key=lambda x : -x[1])
three_s = sorted(abilitis, key=lambda x : -x[2])

one_total = 0
two_total = 0
three_total = 0
for i in range(K) :
    one_total += one_s[i][0]
    two_total += two_s[i][1]
    three_total += three_s[i][2]

print(max(one_total, two_total, three_total))