# 반복문
# while
# 기본구조
# while True:
    # print('Hello World')

# 기본예제

# n=10
# while n>=1:
#     print(n)
#     n -=1

# 반복 범위가 정해져 있을 경우 초깃값,종료값,증감값을 올바르게 작성!!
# 반복하는 횟수나 범위가 명확하지 않은 경우에도 사용할 수 있음

# # 기본예제

# my_list = [] # list형태

# n =int(input('정수를 입력하세요(종료는 0입니다. >>>>'))

# while n !=0: # 0이 종료명령어 역할
#     my_list.append(n)
#     n = int(input('추가입력 >>>'))

# print(my_list)


# # while 중첩문

# day =1 

# while day <=5:
#     hour =1 # 두번째 while문의 변수 위치 주의할 것!!
#     while hour <=3:
#         print('{}일 {}교시 입니다.'.format(day,hour))
#         hour +=1
#     day+=1 # 첫번째 while문 증감값 위치 주의할 것!!


# # 구구단 출력프로그램

# dan=2
# while dan <=9:
#     n =1
#     while n <=9:
#         print('{} x {} = {}'.format(dan,n,dan*n))
#         n+=1
#     dan +=1


# #-----예제1-----
# # 정수를 입력받아 그 횟수만큼 문자 출력

# num = int(input('횟수입력 :'))
# re = 1
# while re <= num:
#     print('{}번째 "Hello"'.format(re))
#     re+=1


# #-----예제2-----
# 1~100까지 정수 중 7의 배수 출력
# k=1
# while k <=100:
#     if k % 7 ==0:
#         print(k)
#     k+=1

# #-----예제3-----
# 300원 이상일 때 반복실행, 잔액부족시 종료
# insert_money=int(input('넣을 돈 >>>'))

# while insert_money>=300:

#     coffee= insert_money/300
#     change= insert_money%300
#     print('커피{0}잔, 잔돈 {1}원'.format(int(coffee),change))

#     insert_money=int(input('넣을 돈 >>>')) # 반복실행
# print('잔액 부족') # 종료

# #-----예제4-----
# 정수 5개 입력받기 (단, 중복된 값은 무시)

# in_num=set([])

# while len(in_num) <5: # 5번째입력 후 돌아왔을 때 False가 돼야하기 때문에 <5 설정해야함.
#     five_num=(int(input('0~9 사이의 정수 입력 >>>')))
#     in_num.add(five_num)
#     print(len(in_num))

# print(in_num)
# print(len(in_num))


# #-----예제5-----
# 1~100 사이의 모든 정수를 한 줄에 10개씩 출력

a=1

while a<=100:
    print(a,end='\t')
    a+=1
    if a%10==1:
        print('\n')

# #-----예제6-----
# 구구단 세로,가로 출력

dan=2
b=1

while b<=9:
    # print(f'{dan}x{b}={dan*b}',end='\t')
    dan=2
    while dan<=9:
        print(f'{dan}x{b}={dan*b}',end='\t')
        dan+=1
    b+=1
    print('\n')




