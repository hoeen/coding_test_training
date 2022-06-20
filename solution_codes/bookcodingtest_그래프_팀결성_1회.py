'''
0~N까지의 번호 학생 부여
팀 합치기와 같은팀여부 확인 연산
'''

n, m = map(int, input().split())

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

student = list(range(0,n+2))
parent = list(range(0,n+2))

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0: # 팀 합치기 연산
        union_parent(parent, b, c)
        print('parent:', parent)
    else: # 같은 팀 확인 연산
        if find_parent(parent, b) == find_parent(parent, c):
            print('YES')
        else:
            print('NO')
    





