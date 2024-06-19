import sys
input = sys.stdin.readline

N, M = map(int, input().split())

vals = list(map(int, input().split()))

knows_num = vals[0]
knows = vals[1:]

partis = []
graph = [[] for _ in range(N + 1)]
for i in range(M) :
    vals = list(map(int, input().split()))
    party_num = vals[0]
    party = vals[1:]
    partis.append(party)
    for i in range(len(party)) :
        for j in range(i) :
            graph[party[i]].append(party[j])
            graph[party[j]].append(party[i])

visited = [False] * (N + 1)

def dfs(n) :
    visited[n] = True
    for v in graph[n] :
        if not visited[v] :
            dfs(v)

for kn in knows :
    dfs(kn)

cannot_say = []
for i in range(1, N + 1) :
    if visited[i] :
        cannot_say.append(i)

ans = 0
for party in partis :
    if len(set(party) & set(cannot_say)) == 0 :
        ans += 1

print(ans)

# knows있는 파티 + knows 있는 파티를 와본 사람이 있는 파티는 무조건 진실만 말해야 함
# 탐색으로 관련 파티는 싹 제외.
# 나머지는 걍 다 거짓말 해도 되잖아..?
