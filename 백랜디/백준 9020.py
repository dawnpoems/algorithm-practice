import sys
input = sys.stdin.readline

T = int(input())

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False

    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False

    return sieve


is_prime = sieve_of_eratosthenes(10000)

for t in range(T) :
    N = int(input())
    start = N // 2
    end = N // 2
    while True :
        while not is_prime[start] :
            start -= 1
        while not is_prime[end] :
            end += 1
        if start + end < N :
            end += 1
        elif start + end == N :
            break
        else :
            start -= 1
    print(start, end)

            