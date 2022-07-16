
from itertools import combinations
l, c = map(int, input().split())
ch_list = input().split()

# l,c = 4, 6
# ch_list = ['a','t','c','i','s','w']

vowel = list('aeiou')
# 조합 - 정렬하여 출력
for ans in combinations(sorted(ch_list), l):
    loc = [v in ans for v in vowel]
    if any(loc):
        if l - sum(loc) >= 2:
            print(''.join(ans))




