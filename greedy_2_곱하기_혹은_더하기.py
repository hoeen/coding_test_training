# ~4:30
'''
0~9 로 문자열이 주어졌을때, 사이에 x 혹은 + 를 넣어
가장 큰 수를 구하는 프로그램을 작성하시오.
연산은 무조건 왼쪽부터'''

# 0 1은 앞뒤는 곱하기 들어가면 안되고 무조건 더하기, 
# 2부터는 무조건 곱하기네?

s = list(map(int,input()))


for i in range(len(s)):
    if i == 0:
        result = s[i]
    else:
        if s[i] == 0 or s[i] == 1:
            result += s[i]
        elif s[i-1] == 0 or s[i-1] == 1:
            result += s[i]
        else:
            result *= s[i]

print(result)
