'''
입력 형태:
| 순번 | 구분  |    문제   | 유형   | 1회 풀이  | 2회 풀이 | 3회 풀이 | 풀이 코드 |
| 00  | 취코테| 모험가 길드 | 그리디 |  ✅❗️     |        |        | 바로가기 |
'''
import os
import unicodedata      # 한글 string의 길이를 다르게 인식하는 경우가 있어, unicodedata 패키지를 이용해 통일

# 현재 파일 리스트 저장
# with open('cote-filelists.txt', 'w') as f:
#     for file in files:
#         f.write(file+'\n')


# 파일 생성
if 'cote-filelists.txt' not in os.listdir('.'):
    with open('cote-filelists.txt', 'w') as f:
        f.write('')



# 이후 링크에 넣기 위해 상위 폴더 이름 불러오기
# folder = os.getcwd().split('/')[-1]


# 기존 파일 리스트 불러오고 현재 디렉토리 파일과 비교해 추가된 파일을 탐색
before_filelist = []
with open('cote-filelists.txt', 'r') as f:
    for line in f.readlines():
        before_filelist.append(line.strip())


files = []
for _, _, filenames in os.walk('.'):
    for filename in filenames:
        if '_' in filename and (filename.endswith('py') or filename.endswith('sql')):
            files.append(filename)


diff_files = list(set(files) - set(before_filelist))


# README 파일 모든 줄 리스트화
readme_list = []
with open('../README.md', 'r') as f:
    for line in f.readlines():
        readme_list.append(line.strip())

# print(readme_list)

def mark_by_trial(trial):
    mark_trial = '✅'
    if unicodedata.normalize('NFC',trial).endswith('답'):
        mark_trial = '✅❗️'
    return mark_trial

def readme_list_insert(dfiles):
    
    global readme_list
    refnew_list = {}  # ref가 같다면 한 테이블로 묶기 위해 key:value로 지정
    # 파일 이름 예시: 취코테_그리디_모험가 길드_1회.py
    # breakpoint()
    for new_file in dfiles:
        #### 입력 파일 파악 #################################
        # '_' 로 구분지어 리스트화  - [구분, 유형, 이름, 회차]
        # if len(new_file[:-3].split('_')) < 5:
        ref, type, name, trial = new_file[:-3].split('_')[:4]
        # elif len(new_file[:-3].split('_')) == 5:   # 참고 항목이 뒤에 있을때
        #     ref, type, name, trial, cf = new_file[:-3].split('_')
        
        # 한글 매칭 위해서 unicodedata 이용
        ref = unicodedata.normalize('NFC',ref)

        # 신규 구분인지 확인
        isNew = True
        
        for bf in before_filelist:
            if ref in bf:
                isNew = False
                break
        if isNew:
            if ref not in refnew_list:
                refnew_list[ref] = []  
            refnew_list[ref].append(new_file)
            continue # 신규 구분일 경우 다음 차례로 넘김
        

        # 2회, 3회차 문제풀이 파일인 경우
        multi = False
        if trial.startswith('2') or trial.startswith('3'):
            multi = True
        ##################################################



        #### 파일 내용 README 에 입력 ########################
        # README 파일의 각 '구분'을 찾아 표 맨 마지막에 insert한다.
        for i in range(len(readme_list)):
            # line[i]의 정보 가져오기  [구분, 유형, 이름, 회차, *참고]
            refline = [f.strip() for f in readme_list[i].split('|')]
            refline = refline[1:len(refline)-1]
            

            if multi and len(refline) > 3:
                if unicodedata.normalize('NFC',refline[3]) == unicodedata.normalize('NFC',name): # 이미 푼 문제인 경우 - 같은 이름 찾아 회차 추가
                    mark_trial = mark_by_trial(trial)
                    if trial.startswith('2'): 
                        refline[5] = mark_trial
                    elif trial.startwith('3'):
                        refline[6] = mark_trial
                    else:
                        raise TypeError("입력 회차가 맞지 않습니다.")
                
                    # 링크 추가 - github 에서 한글 파일명을 인식하지 못해 보류..
                    # refline[7] = r'<a href="' + folder + '/' + new_file + r'">풀이 코드</a>'
            
                    # 내용 바꿈
                    readme_list[i] = '| ' + ' | '.join(refline) + ' |'
                    break
        

            # 기존 구분에 속한 신규 문제인 경우 : 같은 구분 마지막에 줄 추가
            elif i < len(readme_list)-1 and \
                '|' in readme_list[i] and ref in readme_list[i] and \
                '|' not in readme_list[i+1] and ref not in readme_list[i+1]:

                mark_trial = mark_by_trial(trial)

                readme_list.insert(i+1, 
                                '| '+' | '.join(
                                    [str(int(refline[0])+1), ref, type, name, mark_trial, '', '', '']#r'<a href="' + folder + '/' + new_file + r'">풀이 코드</a>']
                                )+' |')
            
                break

            # 가장 마지막 줄에 추가해야 하는 경우
            elif i == len(readme_list)-1 and \
                '|' in readme_list[i] and ref in readme_list[i]:

                mark_trial = mark_by_trial(trial)

                readme_list.append(   # 마지막에 append
                                '| '+' | '.join(
                                    [str(int(refline[0])+1), ref, type, name, mark_trial, '', '', '']#r'<a href="' + folder + '/' + new_file + r'">풀이 코드</a>']
                                )+' |')
            
                break
    return refnew_list

refnew_list = readme_list_insert(diff_files)   

# 새 구분인 경우: README 맨 마지막에 add한다.   
for key in refnew_list:
    ref, type, name, trial = refnew_list[key][0][:-3].split('_')[:4]
    
    mark_trial = mark_by_trial(trial)
   
    # 새 양식 추가
    readme_list += [
        '## ' + ref,
        '| 순번 | 구분 | 유형 | 문제 | 1회 풀이 | 2회 풀이 | 3회 풀이 | 풀이 코드 |',
        '| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | ------- |',
        '| '+' | '.join([str(1), ref, type, name, mark_trial, '', '', 
                        #r'<a href="' + folder + '/' + refnew_list[key][0] + r'">풀이 코드</a>'])
            ]) + ' |'
    ]
    # breakpoint()
    before_filelist.append(refnew_list[key][0])
    if len(refnew_list[key]) > 1:
        _ = readme_list_insert(refnew_list[key][1:])

# breakpoint()
# readme 갱신
with open('../README.md', 'w') as f:
    for line in readme_list:
        f.write(line+'\n')

## filelists 갱신
with open('cote-filelists.txt', 'a') as f:
    for line in diff_files:
        f.write(line+'\n')