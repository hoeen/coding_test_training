# ~1:30
n = int(input())

coins = list(map(int, input().split(' ')))
# coins = sorted(coins)

# coins = [1,1,2,3,9]
# 만들수없는 금액중 최솟값
# 1 1 2 3 9

'''
target 1
1 있으니 1까지 만들수있음.. 다음 target-> 2
다음 1이 있으니 2까지 만들수있음. 다음 target -> 3
다음은 2가 있어서 4까지 만들수있음. 다음 target -> 5
다음은 3이 있어서 7까지 만들수있음. 다음 target -> 8
다음은 9가 있음. target보다 큰경우, 최소 9+1~7이기 때문에 8 못만듬.  


'''
target = 1
for x in sorted(coins):
    if target < x:
        break
    target += x

print(target)


'''오답노트

아이디어를 떠올리기 쉽지 않다. 그리디적 사고방식 - 단순무식하게 다가간다. 
일단 코인문제는, 정렬을 해서
하나하나 더해보면서 아이디어를 찾아야한다.

'''