# 성적 순위를 정확히 알수 있는 학생의 수 구하기
# ~ 11:00
n, m = map(int,input().split())

'''
순위를 정확히 안다 - 모든 학생들과 연결된다
플로이드 워셜 복잡도 O(N**3) 이므로 100**3 연산 충분함
일반적 플로이드워셜 알고리즘 수행 후, 
연결되는 경우를 세서 다른 노드와 모두 연결되면 순위를 알 수 있다.
'''

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for x in range(1, n+1):
    for y in range(1, n+1):
        if x == y:
            graph[x][y] = 0

for _ in range(m):
    a, b = map(int, input().split()) # a < b
    graph[a][b] = 1
    # graph[b][a] = 1




# 플로이드 워셜
# 거리는 필요없고 도달 여부만 알면 되므로, 혹시 연결이 된다면 INF에서 1로 바뀌게 된다.
for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

for g in graph:
    print(g)

result = 0
# 한 명씩 체크하며 도달 가능한지 보기
for st in range(1, n+1):
    count = 0
    for a in range(1, n+1):
        if graph[a][st] != INF or graph[st][a] != INF:
            count += 1
    
    if count == n:
        result += 1


print(result)

