#~4:10
'''
캐릭터 점수 N
자릿수 기준 점수 N을 반으로 나눔. 
왼쪽과 오른쪽의 합이 같으면 끝.
'''

n = list(map(int,input()))
# print(type(n[0]))

div = len(n)//2
left = n[:div]
right = n[div:]
if sum(left) == sum(right):
    print('LUCKY')
else:
    print('READY')