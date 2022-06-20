def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

'''
간선 주어짐
신장 트리를 만들어서,
여행 계획이 이어지는지 확인하면됨
그런데, 사이클이 있는 경우이다.

그냥 하나의 신장 트리 내에 계획의 원소가 존재하면
여행은 가능하다.
'''
n, m = map(int, input().split())

# 같은 트리에 속하는지만 확인하면 되므로, 
# union 함수 수행한 뒤 부모 같은지만 확인하자.
parent = list(range(n+1)) # 0~n

graph = [[] for _ in range(n+1)]
for i in range(n): # 0~ n-1
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            union_parent(parent, i+1, j+1)

plan = list(map(int, input().split()))

result = True
for i in range(len((plan))):
    if i == 0:
        par = parent[plan[i]]
    else:
        if parent[plan[i]] != par:
            result = False

if result:
    print('YES')
else:
    print('NO')












    
    




        