import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = dict()

words = []

for i in range(N) :
    w = input().strip()
    if len(w) >= M :
        if w in dic :
            dic[w] += 1
        else :
            dic[w] = 1

for i in dic.items() :
    words.append(i)

words.sort(key=lambda i : (-i[1], -len(i[0]), i[0]))

# print(words)
for w in words :
    print(w[0])