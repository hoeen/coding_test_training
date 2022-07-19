import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
m = int(input())

dp_tab = [[False]*(n) for _ in range(n)]

for e in range(n):
    for s in range(0, e+1):
        if e == s:
            dp_tab[s][e] = 1
        elif e - s == 1:
            if seq[e] == seq[s]:
                dp_tab[s][e] = 1
            else:
                dp_tab[s][e] = 0
        else:
            if seq[e] == seq[s] and dp_tab[s+1][e-1] == 1:
                dp_tab[s][e] = 1
            else:
                dp_tab[s][e] = 0

# print(time.time() - t0, 's')
# for p in dp_tab:
#     print(p)

for _ in range(m):
    s, e = map(int, input().split())
    print(dp_tab[s-1][e-1])