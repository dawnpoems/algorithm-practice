import sys

n, m, rotate = map(int,  sys.stdin.readline().split())

array = []

for i in range(n) :
    row = list(map(int, sys.stdin.readline().split()))
    array.append(row)

for i in range(rotate) :

    new_array = [[0] * m for _ in range(n)]

    width_start = 0 
    width_end = m - 1

    height_start = 0
    height_end = n - 1

    while True :

        if width_start >= width_end or height_start >= height_end :
            break

        for j in range(width_start, width_end + 1) :
            if j - 1 < width_start :
                new_array[height_start + 1][width_start] = array[height_start][j]
            else : 
                new_array[height_start][j - 1] = array[height_start][j]

            if j + 1 > width_end : 
                new_array[height_end - 1][width_end] = array[height_end][j]
            else :
                new_array[height_end][j + 1] = array[height_end][j]

        for k in range(height_start, height_end + 1) :
            if k + 1 > height_end :
                new_array[height_end][width_start + 1] = array[k][width_start]
            else :
                new_array[k + 1][width_start] = array[k][width_start]
            
            if k - 1 < height_start :
                new_array[height_start][width_end - 1] = array[k][width_end]
            else :
                new_array[k - 1][width_end] = array[k][width_end]

        width_start += 1
        width_end -= 1
        height_start += 1
        height_end -= 1

    array = new_array

for i in array :
    for j in i :
        print(j, end=" ")
    print()