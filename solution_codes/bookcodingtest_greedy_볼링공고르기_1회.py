# ~3:20

# 무게가 다른 볼링공을 고르는 경우의 수

# combination 직접구현
def comb(inp_list, n):
    #1. 정렬하고 리턴값 생성
    inp_list = sorted(inp_list)
    result = []

    #2. exit 생성.  n보다 길이 작을 경우 result 리턴
    if len(inp_list) < n:
        return result

    #3. n = 1일경우, inp_list의 값을 차례로 result에 append한다.
    elif n == 1:
        for i in inp_list:
            result.append([i])
    
    #4. 재귀 구현
    ## 하나씩 빼고 그것을 가지고 재귀 Loop 생성
    else:
        temp = [j for j in inp_list]
        for k in range(len(inp_list)):
            
            temp.remove(inp_list[k])
            for p in comb(temp, n-1):
                result.append([inp_list[k]] + p)
            
        
    return result


n, m = map(int, input().split())

weight_list = list(map(int, input().split()))

# weight_list = [1,3,2,3,2]

# 조합 리스트 하고, 그중에서 무게 같은걸 뺀다.
# 무게 같은 것들을 뽑아내서 그것의 조합을 구해서 처음 리스트에서 뺌

num_list = list(range(1,n+1)) # 1~n

comb_num = len(comb(num_list, 2))

# 같은 무게끼리의 조합 수를 구한다
same_comb_count = 0
for weight in set(weight_list):
    count = weight_list.count(weight)
    if count > 1:
        same_comb_count += int(count*(count-1)/2) #nC2

print(comb_num - same_comb_count)
