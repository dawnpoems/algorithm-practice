import sys
input = sys.stdin.readline

one = list(input().strip())
two = list(input().strip())

d = [[0] * len(two) for _ in range(len(one))]

for i in range(len(one)) :
    for j in range(len(two)) :
        if one[i] == two[j] :
            if i == 0 or j == 0 :
                d[i][j] = 1
            else :
                d[i][j] = d[i-1][j-1] + 1
        else :
            d[i][j] = max(d[i][j-1], d[i-1][j])
            
for row in d :
    print(" ".join(map(str, row)))
print(max(map(max, d)))
