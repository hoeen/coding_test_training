# 삽입, 삭제, 교체
# 연산 수를 최소화
# ~12:00
a = 'cat'

b = 'cut'

table = [[0]*(len(b)+1) for _ in range(len(a)+1)]

table[0] = list(range(len(b)+1))
num = 0
for i in range(len(table)):
    table[i][0] = num
    num += 1

for col in range(1, len(b)+1):
    for row in range(1, len(a)+1):
        if a[row-1] == b[col-1]:
            table[row][col] = table[row-1][col-1]
        else:
            table[row][col] = 1+ min(table[row-1][col],
                                table[row-1][col-1],
                                table[row][col-1]    
                                )

for t in table:
    print(t)

print(table[-1][-1])
        