# ~ 4:00
n = int(input())
seq = list(map(int, input().split()))

# n = 10
# seq = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]

# 가장 큰 합. 연속.
# 점화식 : seq[1] ~ seq[:n] = f(n)
tab = [None for _ in range(n)]
tab[0] = seq[0]
for i in range(1, n):
    tab[i] = max(seq[i], tab[i-1]+seq[i])
print(max(tab))



