# 신장 트리
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

n = int(input())
# n = 5
parent = list(range(n+1)) # 0~n 
# coords = [
# [11, -15, -15, 1],
# [14, -5, -15, 2],
# [-1, -1, -5, 3],
# [10, -4, -1, 4],
# [19, -4, 19, 5],
# ]
coords = []
for i in range(1, n+1):
    li = list(map(int, input().split()))
    li.append(i)
    coords.append(li)

xsort = [(c[0], c[3]) for c in sorted(coords, key=lambda x: x[0])]
ysort = [(c[1], c[3]) for c in sorted(coords, key=lambda x: x[1])]
zsort = [(c[2], c[3]) for c in sorted(coords, key=lambda x: x[2])]

edges = []
for data in [xsort, ysort, zsort]:
    for i in range(len(data)-1):
        # 거리, a, b 추가
        edges.append((abs(data[i+1][0]-data[i][0]), data[i][1], data[i+1][1]))

edges.sort() # 거리 작은순으로 정렬

result = 0
for dist, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += dist

print(result)



    