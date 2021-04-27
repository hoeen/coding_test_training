def solution(orders, course):
    import itertools
    
    def match_char(a,b,n):
        match = ''.join([i for i in a if i in b])
        result = list(itertools.combinations(list(match),n))  # 조합으로 개수에 맞는 쌍 생성

        if len(result)>=1:
            return [''.join(sorted(list(result[i]))) for i in range(len(result))]
        else:
            return ''
        # 개수 정해진 경우 : 값을 개수에 맞게 조합으로 나눈다. 

    ex1 = orders
    tot_menu_list = []
    for i in range(len(ex1)-1):

        for num in course:
            course_num_list = []
            for j in range(1,len(ex1)-i):
                course_num_list+=match_char(ex1[i],ex1[i+j],num)
            tot_menu_list+=course_num_list


    value_count = {}
    for n in set(tot_menu_list):
        value_count[n] = tot_menu_list.count(n)
        #course 수마다 뽑아서 제일 큰 값을 갖는걸 찾는다. 딕셔너리 이용?


    # 개수별로 뽑아서 제일 큰값 갖는걸 찾기
    final = []
    for num in course:
        max_num = 0
        for cs in list(value_count.keys()):
            if len(cs) == num:
                if tot_menu_list.count(cs) > max_num:
                    max_num = tot_menu_list.count(cs)

        final+=[i for i in list(value_count.keys()) if (len(i) == num) & (tot_menu_list.count(i) == max_num)]    

    answer = sorted(final)
    return answer
