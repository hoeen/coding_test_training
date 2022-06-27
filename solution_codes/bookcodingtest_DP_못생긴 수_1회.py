# 2, 3, 5를 곱해가면서 작은 수부터 나열
# ~ 11:20
def ugly(n):
    tab = [1]*n
    for j in range(1, n):
        cand = []
        for i in range(j):
            for mul in [2,3,5]:
                multi = tab[i]*mul
                if multi > tab[j-1]:
                    cand.append(multi)
        tab[j] = min(cand)
    return tab[n-1]


n = int(input())
print(ugly(n))


