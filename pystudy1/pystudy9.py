# for문
# 기본구조
# for 변수 in 반복가능객체:
#   반복실행문

# 예시 
# for n in [1,2,3]:
#     print(n)
# 1 2 3 각각 출력

# 시퀀스 자료형 : 문자열 리스트 튜플 = 순서에따라 사용
# 비시퀀스 자료형 : 세트 딕셔너리 = 순서와 상관없이 하나씩 사용


# 문자와 숫자가 모두 포함되어있는지 확인하는 프로그램

# pwd = input('비밀번호를 입력하세요')

# ch_count = 0
# num_count = 0

# for ch in pwd:
#     if ch.isalpha():
#         ch_count +=1
#     elif ch.isnumeric():
#         num_count +=1
    
# if ch_count > 0 and num_count > 0:
#     print('가능한 비밀번호입니다.')
# else:
#     print('불가능한 비밀번호입니다.')

# ch.isalpha()는 ch가 문자인 경우 True 반환
# ch.isnumeric()은 ch가 숫자인 경우 True 반환

# 리스트 순회 , 리스트 내포
# 리스트는 순차적 실행
# # 리스트 내포 = [표현식 for 변수 in 반복객체]
# li=[n*2 for n in [1,2,3]] # = 2,4,6
# # [표현식 for 변수 in 반복객체 if 조건식]
# lis=[n*2 for n in [1,2,3,4,5]if n % 2 ==1]

# for문과 range()함수
# 정수의 범위를 만들어 낼 때 유용한 함수

# range(초깃값,종료값,증감값)
# 종료값은 생략할 수 없음 즉, 하나만 입력했을 때 종료값으로 인식
# 초깃값을 생략하면 0부터시작
# 증감값을 생략하면 1씩 증가
# class'range'
# range 함수의 값을 직접확인하려면 리스트나, 튜플같은 시퀀스 자료형으로 형변환 해야한다.
# list(range(1,6))
# [1,2,3,4,5]
# tuple(range(1.6))
# [1,2,3,4,5]

# for n in [1,2,3,4,5,6,7,8,9,10]: = for n in range(1,11):

# 반복 횟수 지정으로 사용
# for n in range(10):
    # print('Hello')
# = Hello 가 10번 수행된다.


# 기본예제
# 구구단 입력받아 출력하기

# dan = int(input('출력할 구구단 입력:'))
# for n in range(1,10):
#     print(f'{dan}*{n}={dan*n}')


# for문과 딕셔너리
# dict은 key와 value의 조합 데이터를 구성
# person={
#     'name' : '이재욱',
#     'age' : '29'
#     }
# for item in person:
#     print(item) # dict의 key 출력

# for key in person:
#     print(person[key]) # dict의 value 출력 (각 key의 맞는)

# for key in person:
#     print(person.get(key)) # get()을 통해서도 가져올 수 있음


# # 기본예제

# eng_dict={
#     'sun':'태양',
#     'moon':'달',
#     'star':'별',
#     'space':'우주'
# }

# for word in eng_dict: # word에 key 저장
#     print('{}의 뜻:{}'.format(word,eng_dict.get(word)))

# # word로 순차적으로 전달되는 것은 eng_dict의 키 값('sun,moon,star,space)






# #-----예제1-----
# # 1~5 사이에 존재하는 모든 정수를 역순으로 출력

# for n in range(5,0,-1):
#     print(n)

# #-----예제2-----
# # 양의정수 입력 후 1부터 입력한 수 까지 출력

# n = int(input('정수입력'))
# for j in range(1,n+1):
#     j=sum(list(range(1,n+1)))
# print('1부터{}사이 합계는 {}입니다.'.format(n,j))

# #-----예제3-----
# 임의이 정수 입력받은 뒤 그 수만큼 과일 이름을 입력받아 basket 리스트에 저장

# pruit=int(input('몇 개의 과일을 보관할까요?>>>'))
# basket=list()
# for n in range(1,pruit+1):
#     sel=str(input('{}번째 과일을 입력하세요 >>>'.format(n)))
#     basket.append(sel)
    
# print(f'입력받은 과일들은{basket} 입니다.')    
# print('입력받은 과일들은{}입니다.'.foramt(basket))


# #-----예제4-----
# # 성적프로그램 한반에 10명
# # exam = [99,78,100,91,81,85,54,100,71,50]
# # 100점을 제외한 점수를 5점씩 증가시킨 리스트를 생성하여 출력하고, 증간된 점수가 100점이 넘지 않도록 처리

# exam = [99,78,100,91,81,85,54,100,71,50]
# # print(type(exam[0])) # int
# score = list()
# s=0
# for a in range(1,(len(exam)+1)):
#     a=exam[s]+5
#     if a<100:
#         a=exam[s]+5
#     else:
#         a=exam[s]+(100-exam[s])
#     s+=1
#     score.append(a)

# print(score)

# #-----예제5-----
# 1~99 정수를 대상으로 3,6,9 가 들어가는 수는 '짝'으로 표시하여 출력
n=1
num=0
clap='짝'
clap2='짝짝'

for i in range(n,100):
    num+=1
# 가장 해당이 적은 조건먼저! 반복문이 전부 돌 수 있도록 처리
    if (num%10 == 3 or num%10 == 6 or num%10 == 9) and (int(num/10)==3 or int(num/10)==6 or int(num/10)==9):
        print(clap2,end='\t')   # 1의자리(나머지)가 3,6,9 이면서(and) 10의자리(몫)(int변환필수)가 3,6,9일 때 
    elif (num%10 == 3 or num%10 ==6 or num%10 ==9) or (int(num/10)==3 or int(num/10)==6 or int(num/10)==9):
        print(clap,end='\t')    # 1의자리가 3,6,9 이거나 10의자리가 3,6,9 일 때
        if num%10 == 0: # 10단위로 줄 바꿈
            print(end='\n')
    else:
        print(num,end='\t') # 해당없는 수 출력 ex) 1,2,4,5,7,8 ...
        if num%10 == 0: # 10단위로 줄 바꿈
            print(end='\n')