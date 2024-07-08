import sys
input = sys.stdin.readline

W, H = map(int, input().split())

P, Q = map(int, input().split())

T = int(input())

p = (T % (2 * W)) + P
q = (T % (2 * H)) + Q

if p > W :
    p = 2 * W - p

if q > H :
    q = 2 * H - q

if p < 0 :
    p = -p
if q < 0 :
    q = -q

print(p, q)