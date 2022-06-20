n = int(input())
al = list(map(int,input().split()))
b,c = map(int, input().split())

'''
총감독 : 각각의 시험장 1명. 
부감독 : 제한없음.
총감독 한명당 b명. 부감독 한명당 c명
'''

'''구현?
각 리스트에서 
'''

sup = n # 총감독 수 n명

for a in al:
    a -= b
    if a <= 0:
        continue
    elif a % c == 0: # a 여전히 남고 부감독 딱 맞는경우
        second = a // c # 시험장 당 부감독 수. 남는학생은 부감독 하나더
    elif a % c != 0:
        second = a // c + 1
    
    sup += second # 총에 부감독 수 추가

print(sup)



