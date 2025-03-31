import sys
input = sys.stdin.readline

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False

    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False

    return sieve

def find_goldbach(n) :
    start = n // 2
    end = n // 2
    while True :
        while not is_prime[start] :
            start -= 1
        while not is_prime[end] :
            end += 1
        if start + end < n :
            end += 1
        elif start + end == n :
            return [start, end]
        else :
            start -= 1

N = int(input())

is_prime = sieve_of_eratosthenes(N)

ans = []

if N < 8 :
    print(-1)
else :
    ans.append(2)
    if N % 2 == 0 :
       ans.append(2)
       ans.extend(find_goldbach(N - 4))
    else :
        ans.append(3)
        ans.extend(find_goldbach(N - 5))
    
    ans.sort()
    print(*ans)


            

