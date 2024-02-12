import sys
input = sys.stdin.readline

line = input().strip()
q = int(input())

cumul_lst = []

cumul = {}

for c in range(ord('a'), ord('z') + 1) :
    cumul[chr(c)] = 0

# print(cumul)
cumul_lst.append(cumul)

for l in line :
    cumul = cumul.copy()
    cumul[l] += 1
    cumul_lst.append(cumul)

print(cumul_lst)

for i in range(q) :
    dest, start, end = input().split()
    print(cumul_lst[int(end) + 1][dest] - cumul_lst[int(start)][dest])