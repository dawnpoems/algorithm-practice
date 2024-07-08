import sys
input = sys.stdin.readline

N, K = map(int, input().split())

scores = []
for i in range(N) :
    scores.append(float(input()))

scores.sort()

trimmed = 0
adjusted = scores[K] * (K) + scores[N - K - 1] * (K)

for i in range(K, N - K) :
    trimmed += scores[i]
    adjusted += scores[i]

trimmed /= N - 2 * K
adjusted /= N

print(f"{trimmed + 0.00000001 :.2f}")
print(f"{adjusted + 0.00000001:.2f}")