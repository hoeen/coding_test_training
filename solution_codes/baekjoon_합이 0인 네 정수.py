n = int(input())

A, B, C, D = list(), list(), list(), list()

# print(list(map(int, input().split())))

for _ in range(n):
    a, b, c, d  = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

A.sort()
B.sort()
C.sort()
D.sort()

count = 0
for a in A:
    for b in B:
        for c in C:
            if a+b+c+max(D) < 0:
                # print('impossible')
                continue
            else:
                for d in D:
                    # print(a,b,c,d)
                    if a+b+c+d == 0:
                        # print('count+1')
                        count += 1
                    elif a+b+c+d > 0:
                        # print('morethan0')
                        break # 다음 a,b,c에서 시작 

print(count)