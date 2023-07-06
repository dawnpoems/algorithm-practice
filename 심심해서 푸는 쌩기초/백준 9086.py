import sys

input = sys.stdin.readline

n = int(input())

for i in range(n) :
    monja = input()
    print(monja[0:1], end="")
    print(monja[-2:-1])