import sys

perfect = [1, 1, 2, 2, 2, 8]

founded = list(map(int, sys.stdin.readline().split()))

for i in range(6):
    print(perfect[i] - founded[i], end=" ")
