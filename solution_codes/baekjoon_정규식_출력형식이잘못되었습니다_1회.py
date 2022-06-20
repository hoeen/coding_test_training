'''
대소문자 차이 없이 같게봄
공백 유무만 봄
({[,]}) 같음
, ; 같음
'''
import re
k = int(input())


text_list = []
for _ in range(k*2):
    text_list.append(input())      


for j in range(k):
    check_list = []
    for i in range(2):
        text = text_list.pop(0)  
        text = text.lower() # 소문자로 통일
        text = re.sub('[{[(]',' ( ',text)
        text = re.sub('[]})]',' ) ',text) # 괄호 () 로 통일
        text = re.sub('[;,]',' , ',text)
        text = re.sub(':',' : ',text)
        text = re.sub('\.',' \. ',text)
        text = re.sub(' {1,}', ' ',text) # 공백 1개로 통일
        text = text.strip() # 양옆 공백 제거

        # 다 끝났으면 text_list에 추가
        check_list.append(text)
    
    # print(check_list)
    print(f'Data Set {j+1}:', end=' ')
    if check_list[0] == check_list[1]:
        if j != k-1:
            print('equal\n')
        else:
            print('equal')
    else:
        if j != k-1:
            print('not equal\n')
        else:
            print('not equal')
