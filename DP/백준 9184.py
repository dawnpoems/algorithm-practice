import sys
input = sys.stdin.readline

def func(a, b, c) :

    if a <= 0 or b <= 0 or c <= 0 :
        if 0 <= a <= 20 and 0 <= b <= 20 and 0 <= c <= 20 :
            numbers[a][b][c] = 1
        return 1
    
    if a > 20 or b > 20 or c > 20 :
        return func(20, 20, 20)
        
    if numbers[a][b][c] != 0 :
        return numbers[a][b][c]

    if a < b and b < c :
        numbers[a][b][c] = func(a, b, c-1) + func(a, b-1, c-1) - func(a, b-1, c)
        return numbers[a][b][c]
    else :
        numbers[a][b][c] = func(a-1, b, c) + func(a-1, b-1, c) + func(a-1, b, c-1) - func(a-1, b-1, c-1)
        return numbers[a][b][c]

# a, b, c = map(int, input().strip().split())
# numbers = [[[0] * 21 for _ in range(21)] for _ in range(21)]
# result = func(a, b, c)
# for table in numbers :
#     print("----")
#     for row in table :
#          print(" ".join(map(str, row)))

# print(result)

numbers = [[[0] * 21 for _ in range(21)] for _ in range(21)]

while True :
    a, b, c = map(int, input().strip().split())
    if a == -1 and b == -1 and c == -1 :
        break
    print("w("+ str(a) + ", " + str(b) + ", " + str(c) +") = ", end="")
    print(func(a, b, c))


