import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

K = int(input())

def hanoi(n, start, end, via) :
    if n == 1 :
        print(start, end)
        return
    hanoi(n - 1, start, via, end)
    print(start, end)
    hanoi(n - 1, via, end, start)

print(2 ** K - 1)

if K <= 20 :
    hanoi(K, 1, 3, 2)