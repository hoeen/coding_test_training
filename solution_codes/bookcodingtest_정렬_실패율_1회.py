N =  5
stages = [6,6,6,6,6,6]
stages.sort()
failure = [[i, 0] for i in range(N+1)]

idx = stages[0]
# 처음 수부터 N보다 큰 경우를 생각해 주어야 한다. 이것이 결정적 반례
if idx <= N:
    failure[idx][1] = stages.count(idx) / len(stages[0:])

for i in range(1, len(stages)):
    if stages[i] > stages[i-1]:
        if stages[i] <= N:
            idx = stages[i]
            failure[idx][1] = stages.count(idx) / len(stages[i:])

failure = failure[1:]
failure.sort(key=lambda x: (-x[1],x[0]))
# print(failure)
answer = []
for f in failure:
    answer.append(f[0])
print(answer)
        

        