import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

one = 0
two = 0

table = [0] * (n + 1)

table[1] = 1
table[2] = 1

def fib_dp (n) :
    global two
    if n == 1 or n == 2:
        return 1
    if table[n] != 0 :
        return table[n]
    two += 1
    table[n] = fib_dp(n - 1) + fib_dp(n - 2)    
    return table[n]

fib_dp(n)

print(table[n], two)
    
    


