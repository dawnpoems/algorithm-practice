import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

n = int(input())

table = [0] * (n + 1)

table[0] = table[1] = 1

for i in range(2, n + 1) :
    table[i] = (table[i - 1] + table[i - 2]) % 15746
    
print(table[n])