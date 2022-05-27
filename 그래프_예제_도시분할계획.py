# ~ 4:40

# 두 마을을 나눈다.
# 신장트리를 두개. how?
# 일단 다 연결한 다음에 - 가장 큰 값을 빼면 무조건
# 제일 최솟값으로 나눠지나? 반례 못찾겠으니 걍해보자.
import sys
input = sys.stdin.readline

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

# 노드와 간선 입력받기
n, m = map(int, input().split())
parent = list(range(n+1)) # 부모 테이블 초기화

# 모든 간선 담을 리스트와 최종 비용 담을 변수
edges = []
result = []

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c,a,b)) # 비용순으로 정렬 예정

# 간선을 비용순으로 정렬
edges.sort()
# print(edges)

# 간선 하나씩 확인
for cost, a, b in edges:
    # 부모 노드가 같지 않는, 즉 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(cost)

# Result에서 최댓값 하나 빼기
# print(result) 
result.remove(max(result))
# print('removed', result)
print(sum(result))
