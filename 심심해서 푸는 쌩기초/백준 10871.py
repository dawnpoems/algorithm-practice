n, x = map(int, input().split())

numbers = list(map(int, input().split()))

answers = []

for number in numbers :
    if number < x :
        answers.append(str(number))

print(" ".join(answers))


