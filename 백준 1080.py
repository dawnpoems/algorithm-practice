import sys

a, b = map(int, sys.stdin.readline().split())

start_matrix = []
result_matrix = []
for i in range(a):
    start_line = list(map(int, list(sys.stdin.readline().rstrip())))
    start_matrix.append(start_line)
    result_line = list(map(int, list(sys.stdin.readline().rstrip())))
    result_matrix.append(result_line)


print(start_matrix)
print(result_matrix)


def flip(start_matrix):
    for i in range(3):
        for j in range(3):
            now_num = start_matrix[i][j]
            if now_num == 0:
                start_matrix[i][j] = 1
            else:
                start_matrix[i][j] = 0


for i in range(a - 2):
    for j in range(b - 2):
        start_num = start_matrix[i][j]
        result_num = result_matrix[i][j]
        if start_num != result_num:
