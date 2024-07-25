import sys
input = sys.stdin.readline

N, A = map(int, input().split())

# (A * K) % N == 1 인 K 찾기 

def euclid(a, b) :
    if b == 0 :
        return a
    return euclid(b, a%b)

def ex_euclid(a, b) :
    s1 = 1
    s2 = 0
    # t1 = 0
    # t2 = 1
    r1 = a
    r2 = b
    while True :
        q = r1 // r2
        r = r1 - r2 * q
        s = s1 - s2 * q
        # t = t1 - t2 * q
        
        if r == 0 :
            return s2

        s1, s2 = s2, s
        # t1, t2, = t2, t
        r1, r2 = r2, r

if euclid(A, N) != 1 :
    print(N - A, -1)
else :
    m = ex_euclid(A, N)
    while m < 0 :
        m += N
    print(N - A, m) 