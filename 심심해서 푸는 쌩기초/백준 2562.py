import sys
input = sys.stdin.readline

numbers = []

for i in range(9) :
    numbers.append(int(input()))

m_num = max(numbers)

print(m_num)
print(numbers.index(m_num) + 1)