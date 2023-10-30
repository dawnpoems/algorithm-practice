import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dogam = []
quizz = []

for i in range(n) :
	dogam.append(input().strip())

for j in range(m) :
	quizz.append(input().strip())

for quiz in quizz :
	if (quiz.isdigit()) :
		print(dogam[int(quiz) - 1])
	else :
		print(dogam.index(quiz) + 1)