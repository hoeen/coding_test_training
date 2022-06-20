# ~ 6:20
# n, m = map(int, input().split())


n, m = 7, 11
graph = [ 
(0, 1, 7),
(0, 3, 5),
(1, 2, 8),
(1, 3, 9),
(1, 4, 7),
(2, 4, 5),
(3, 4, 15),
(3, 5, 6),
(4, 5, 8),
(4, 6, 9),
(5, 6, 11)
]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 크루스칼 코드 - 최소의 비용으로 모든 도시 연결

# 부모 리스트 생성
parent = list(range(n)) # 0~n-1
edges = []
result = 0
total = 0
for i in range(m):
    a, b, cost = graph[i]#map(int, input().split())
    edges.append((cost, a, b))
    total += cost
edges.sort()

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(total - result)
