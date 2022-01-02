# # 형 변환 str -> int, float

# 예시

# n=input('정수 입력 >>>')
# print(type(n)) # <class 'str'>

# # 정수로 변환하기

# n=int(input('정수 입력 >>>')) # 실수 변환시 float
# print(type(n)) # <class 'int'>

# # 예제

# price=500000
# n=int(input('할부 개월 입력 >>'))
# print('매달 할부금은 {0:.2f}원 입니다.'.format(price/n)) # 소수점 표현하기 {인덱스번호:소수점자리수}

# # # 응용예제
# # -----예제1-----
# # 두개의 실수를 입력받아 합산하기
# # n1=1.23
# # n2=2.34

# n1=float(input('첫 번째 실수를 입력하세요 >>>'))
# n2=float(input('두 번째 실수를 입력하세요 >>>'))

# print(n1+n2)

# #-----예제2-----
# 1~12사이에 월을 입력받아 해당 월이 며칠까지 있는지 구하시오

# month={'1':'30', '2':'28', '3':'31', '4':'30', '5':'31', '6':'30', '7':'31', '8':'31', '9':'30', '10':'31', '11':'30', '12':'31'}
# # print('2월은 '+month['1'])
# sel=input('월을 입력하시오 >>')
# print('{0}월은 {1}일 까지 있습니다.'.format(sel,(month[sel])))

# #-----예제3-----
# # 예제와 같이 동작하는 프로그램을 구현하시오
# english_dict={
#     'flower':'꽃',
#     'fly':'날다',
#     'floor':'바닥'
# }
# # 영어 단어를 입력하세요 >>> flower
# # flower:꽃
# find_dict=input('영어 단어를 입력하세요 :')
# print((find_dict),':',(english_dict[find_dict]))

# #-----예제4-----
# # 학생들의 희망장소를 조사하고 원하는 장소를 입력받아 동일한 입력은 무시하고 모든 입력을 저장하려 한다.
# # 실행예와같은 동작 프로그램을 구현하라

# student1=str(input('희망하는 수학여행지 입력 >>>'))

# student2=str(input('희망하는 수학여행지 입력 >>>'))

# student3=str(input('희망하는 수학여행지 입력 >>>'))

# tr_list=[student1,student2,student3]

# f_list=list(set((tr_list))) # 기존리스트를 set로 변환하여 중복제거 후 다시 list로 변환
# # print(f_list)

# print('조사된 여행지는',end='')
# print(f_list, '입니다')





