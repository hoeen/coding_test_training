# ~3:30  ~4:00
words = ["f", "frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "???zo", "fr???", "fro???", "pro?",  'fr????', 'f????']

# agile 하게 일단 문제를 풀고 수정하자

# words 2 이상 100000 이하 . 단어 각 길이는 10000 이하
# queries 2 이상 100000 이하, 단어 각 길이 10000 이하

# queries 마다 words를 다 돌면서 매치시키고 append 한다.
# 일단 O(N^2) 100000 ** 2 라서 안댐.. 
# from bisect import bisect_left, bisect_right 

def binary_search(array, start, end, direction): # 마지막 문자 위치 반환
    if direction == 'left': #? in right
        if start > end:
            return None
        elif end - start == 1:
            if array[end] == '?':
                return start
            else:
                return None
        else:
            mid = (start + end) // 2
            if array[mid] != '?' and array[mid+1] == '?':  # 끝부분 찾음
                return mid
            elif array[mid+1] != '?': # ?가 더 오른쪽에 있는경우
                return binary_search(array, mid+1, end, 'left')
            elif array[mid] == '?' and array[mid-1] != '?':
                return mid-1
            else: # mid ? and mid-1 ?
                return binary_search(array, start, mid-1, 'left')          

    else: # right  - ? in left
        # print('right:', start, end)
        if start > end:
            return None
        elif end - start == 1:
            if array[start] == '?':
                return end
            else:
                return None
        else:
            mid = (start + end) // 2
            if array[mid] != '?' and array[mid-1] == '?':  # 끝부분 찾음
                return mid
            elif array[mid-1] != '?': # ?가 더 왼쪽에 있는경우
                return binary_search(array, start, mid-1, 'right')
            elif array[mid] == '?' and array[mid+1] != '?':
                return mid+1
            else: # mid ? and mid-1 ?
                return binary_search(array, mid+1, end, 'right')

sort_queries = sorted(zip(range(0, len(queries)), queries), key=lambda x: x[1], reverse=True) # ?? 적은게 앞으로
sq_queries = [i[1] for i in sort_queries]
num_queries = [i[0] for i in sort_queries]

match_queries = [None] * len(queries)   #[ (start, end) ]
print(sort_queries)
# [(4, 'pro?'), (3, 'fro???'), (0, 'fro??'), 
# (5, 'fr????'), (2, 'fr???'), (6, 'f????'), (1, '????o')]  - (num ,sq)

# def match(query: list, word: str):
    


def result(words, queries): 
    ans_list = [0]*len(queries)
    for qi in range(len(queries)):
        q = sq_queries[qi] #정렬된 queries #queries[qi]
        # 이진탐색으로, 어디가 끝점인지 파악
        if q[0] == '?' and q[-1] == '?':
            di = 'all'
            print(None)
            start, end = None, None
        elif q[0] == '?':
            di = 'right'
            print(binary_search(q, 0, len(q)-1, di), len(q)-1)
            start, end = (binary_search(q, 0, len(q)-1, di), len(q)-1)
        else:
            di = 'left'
            print(0, binary_search(q, 0, len(q)-1, di))
            start, end = (0, binary_search(q, 0, len(q)-1, di))

        # start, end 지정 상태에서 이전 겹치는 문자를 찾기
        for s in sq_queries[:qi][::-1]:
            # s, q 비교
            if di == 'left':
                if len(s) == len(q):
                    iscorrect = True
                    for j in range(start, end+1):
                        if s[j] != q[j]:
                            iscorrect = False
                    # if iscorrect: # 겹침!
                    #     ans_list[qi] += 
                        


                    
        
        for w in sorted(words):
            if len(w) != len(q):
                continue
            if (start, end) == (None, None):
                ans_list[qi] += 1
                continue
            correct = True
            for i in range(start, end+1):
                if w[i] != q[i]:
                    correct = False
                    break
            if correct:
                ans_list[qi] += 1

    return ans_list

print(result(words, queries))
    
    