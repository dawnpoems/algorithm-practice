import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

cards = list(map(int, input().strip().split()))

for i in range(m) :
    cards.sort(reverse=True)
    one = cards.pop()
    two = cards.pop()

    cards.append(one + two)
    cards.append(one + two)

print(sum(cards))