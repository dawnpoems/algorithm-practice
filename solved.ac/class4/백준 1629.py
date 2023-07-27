import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

# def gobsem(a, b) :
#     if b == 1 :
#         return a
#     if b % 2 == 1 :
#         ans = ((gobsem(a, b//2)) ** 2) * a
#         print(ans)
#         return ans
#     else :
#         ans = ((gobsem(a, b//2)) ** 2)
#         print(ans)
#         return ans

# print(gobsem(a, b))

def gobsem(a, b, c) :
    if b == 1 :
        return a % c
    if b % 2 == 1 :
        return (((gobsem(a, b//2, c)) ** 2) * a) % c
    else :
        return ((gobsem(a, b//2, c)) ** 2) % c

print(gobsem(a, b, c))