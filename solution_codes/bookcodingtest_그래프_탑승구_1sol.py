# ~5:40
# 서로소 집합으로 풀기
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
        
n = int(input()) # 도킹 개수
k = int(input()) # 비행기 개수

# 부모 테이블
parent = list(range(n+1)) # 0~n
planes = 0
for _ in range(k):
    end = int(input())
    planes += 1
    if parent[end] == end:
        union_parent(parent, end, end-1)
    elif parent[end] != 0:
        union_parent(parent, parent[end], parent[end]-1)
    else:
        planes -= 1
        break

print(planes)




