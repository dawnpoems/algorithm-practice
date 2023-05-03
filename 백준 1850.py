import sys

c, d = map(int, sys.stdin.readline().split())


def uclide(a, b):
    if a % b == 0:
        return b

    else:
        return uclide(b, a % b)


a = max(c, d)
b = min(c, d)

for i in range(uclide(a, b)):
    print('1', end='')
