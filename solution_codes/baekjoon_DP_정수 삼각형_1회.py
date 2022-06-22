n = int(input())
tri = [None]*n
for i in range(n):
    tri[i] = list(map(int, input().split()))

# dp - tab
tab = [None for _ in range(n)]
for i in range(n):
    tab[i] = [0]*(i+1)

def dp_tab():
    tab[0][0] = tri[0][0] # 맨위 삽입
    for x in range(1, n):
        for y in range(len(tri[x])):
            km = []
            if y-1 >= 0:
                km.append(tab[x-1][y-1])
            if y < len(tri[x])-1:
                km.append(tab[x-1][y])
            tab[x][y] = tri[x][y] + max(km)
            

dp_tab()

print(max(tab[-1]))
