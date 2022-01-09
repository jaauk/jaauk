# 응용예제

# #-----예제1-----
# # 100~90 = A , 89~80 = B , 79~70 = C , 69~60 = D , 59이하 F

# score = int(input('점수 입력 >>>'))
# if score >= 90:
#     print('"A"')
# elif score >= 80:
#     print('"B"')
# elif score >= 70:
#     print('"C"')
# elif score >= 60:
#     print('"D"')
# else:
#     print('"F"')

# #-----예제2-----
# # 3의 배수인지 판별

# num = int(input('정수 입력 >>>>'))

# a = num%3
# if a == 0:
#     print('3의 배수')
# else:
#     print('3의 배수 아님')

# #-----예제3-----
# 정수3개 입력받아 가장 큰 수 출력

# num1 = int(input('정수입력 1 >>>'))
# num2 = int(input('정수입력 2 >>>'))
# num3 = int(input('정수입력 3 >>>'))

# if num1 > num2 > num3:
#     print(num1)
# elif num1 > num3 > num2:
#     print(num1)
# elif num2 > num1 > num3:
#     print(num2)
# elif num2 > num3 > num1:
#     print(num2)
# else:
#     print(num3)

# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# elif num3 > num1 and num3 > num2:
#     print(num3)
# else:
#     print('error')

# #-----예제4-----
# 차량 2부제 프로그램

car = str(input('차량번호 입력 >>>'))
approval = ['2','4','6','8','0'] # 인덱스 중 해당값이 있는지? 나중에 다시 체크하기!!
# print(car[-1])
if car[-1]=='2'or'4'or'6'or'8'or'0':
    
    print('운행가능')
else:
    print('운행불가')
