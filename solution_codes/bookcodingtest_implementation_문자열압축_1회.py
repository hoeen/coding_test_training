# ~10:25
# input_str = input()


input_str = "z"*100*10

# x개단위를 비교하여 가장 적은 표현방식으로 만들기
# greedy?

output_str = ''
temp = 1

def find_nword(in_str, n):
    global output_str, temp
    if len(in_str) < n*2:
        if temp != 1:
            output_str += (str(temp)+in_str)
        else:
            output_str += in_str
        
        return 

    start = in_str[:n]
    find = in_str[n:n*2]
    
    if start != find:
        # print('dif')
        if temp == 1:
            output_str += in_str[:n]
            
        else:
            output_str += (str(temp)+start)
            temp = 1
        
        # 다시 n번째 뒤부터 탐색
        find_nword(in_str[n:], n)
        

    else: # 같은 경우
        # print('same')
        # 등장 횟수를 업데이트
        temp += 1
        # n개 다음부터 다시 탐색
        find_nword(in_str[n:], n)




for str_len in range(1, len(input_str)//2+1):
    find_nword(input_str, str_len)
    res = len(output_str)
    if str_len == 1:
        before = len(output_str)
    if res < before:
        before = res
    print('str_len:', str_len, 'output:', output_str)
    output_str = ''
    temp = 1

print(before)