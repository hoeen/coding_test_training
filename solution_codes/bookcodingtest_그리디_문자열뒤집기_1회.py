# ~4:40
# 00101010 최소 뒤집기로 0 또는 1을 만들기

# 101101101이면?
# 그냥 순서 바뀔때까지 뒤집으면 되는데..
# 문제는 11110111100011111인경우? 1을 뒤집을지 0을 뒤집을지 알수없다.
# 그러면, 연속된 1 세고 연속된 0을 세서, 그중 작은값을 리턴하면된다.

import time
import sys
s = sys.stdin.readline().strip()
# s = '10110110100011111'
t0 = time.time()
count = {'1':0, '0':0}
for i in range(len(s)):
    # 연속된 0과 1 카운트하기
    if i == 0:
        now = s[i]
        count[now] += 1
    elif s[i] != s[i-1]:
        now = s[i]
        count[now] += 1
    else:
        continue
print(time.time()-t0, 's')
print(count.values())
print(min(count.values()))

print(2/10**6)



