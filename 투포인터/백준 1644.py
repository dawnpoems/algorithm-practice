import sys
input = sys.stdin.readline

N = int(input())

def eratos(n) :
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1) :
        if is_prime[i] :
            for j in range(i * i, n + 1, i) :
                is_prime[j] = False
    
    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes

primes = eratos(N)

start = 0
end = 0
total = 0
cnt = 0
pleng = len(primes)

while start < pleng :
    if total < N and end < pleng :
        total += primes[end]
        end += 1
    else :
        total -= primes[start]
        start += 1
    if total == N :
        cnt += 1

print(cnt)

