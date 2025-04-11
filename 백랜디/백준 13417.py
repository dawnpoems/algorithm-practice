import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for t in range(T) :
    N = int(input())
    cards = list(input().split())
    table = deque([])
    for card in cards :
        if not table :
            table.append(card)
        else :
            if card <= table[0] :
                table.appendleft(card)
            else :
                table.append(card)
    print(*table, sep="")