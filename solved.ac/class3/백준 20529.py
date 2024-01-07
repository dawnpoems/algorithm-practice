import sys
from itertools import combinations
input = sys.stdin.readline

t = int(input())

def get_bits(mbtis) :
    bits = []
    for mbti in mbtis :
        num = 0
        for i in range(4) :
            if (i > 0) :
                num = num << 1
            if (mbti[i] == 'E' or mbti[i] == 'S' or mbti[i] == 'T' or mbti[i] == 'J') :
                num += 1
        bits.append(num)
    return bits

def get_score(c) :
    score = 0
    # print(c)
    for i in range(4) :
        if not (0b0001 & c[0] & c[1] & c[2] == 1 or 0b0001 & (c[0] | c[1] | c[2]) == 0) :
            score += 2
        c[0] = c[0] >> 1
        c[1] = c[1] >> 1
        c[2] = c[2] >> 1
    return (score)

for i in range(t) :
    n = int(input())
    mbtis = input().split()
    if (n >= 16**2) :
        print(0)
        continue
    bits = get_bits(mbtis)
    comb = combinations(bits, 3)
    min_score = 12
    for c in comb :
        now = get_score(list(c))
        if (now < min_score) :
            min_score = now
    print(min_score)
