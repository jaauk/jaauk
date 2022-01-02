# 연산자와 우선순위
# 연산자의 주요 우선순위
# 1 list, tuple, set, dict
# 2 index, slicing
# 3 거듭제곱 **
# 4 양의부호,음의부호
# 5 곱셈-덧셈-관계연산자
# 6 논리 not - and - or - 조건 if,else

# 기본 연산자
# 산술 연산자

# 덧셈+,뺄셈-,곱셈*,제곱**,나눗셈/,몫//,나머지%

# # 기본예제

# a=7
# b=2

# print('{}+{}={}'.format(a,b,a+b)) # =9
# print('{}-{}={}'.format(a,b,a-b)) # =5
# print('{}*{}={}'.format(a,b,a*b)) # =14
# print('{}**{}={}'.format(a,b,a**b)) # =49
# print('{}/{}={}'.format(a,b,a/b)) # =3.5
# print('{}//{}={}'.format(a,b,a//b)) # =3
# print('{}%{}={}'.format(a,b,a%b)) # =1

# # 기본 예제
# # 저금통에 용돈을 넣고 빼는 과정의 프로그램

# piggy_bank=0

# money=10000
# piggy_bank += money
# # 현재 piggy_bank = 10000
# print('저금통에 용돈{}원을 넣었습니다.'.format(money))
# print('지금 저금통에는{}원이 있습니다.'.format(piggy_bank))

# snack=2000
# piggy_bank -= snack
# print('저금통에서 스낵 구입비 {}을 뺏습니다.'.format(snack))
# print('저금통에 {}원이 남았습니다.'.format(piggy_bank))


# 관계연산자

# 크다 >
# 작다 <
# 크거나 같다 >=
# 작거나 같다 <=
# 같다 ==
# 같지 않다 !=

# 논리bool 자료형은 True와 False만 가진다. True와 False는 항상 대문자로 시작해야한다.

# 논리연산자

# and 모두 참 or not
# or 하나라도 참 or not
# not 참이면 not 거짓이면 참

# # 기본예제

# a=15
# print('{}>10:{}'.format(a,a>10))
# print('{}<10:{}'.format(a,a<10))
# print('{}>=10:{}'.format(a,a>=10))
# print('{}<=10:{}'.format(a,a<=10))
# print('{}==10:{}'.format(a,a==10))
# print('{}!=10:{}'.format(a,a!=10))

# # 기본예제

# a=10
# b=0
# print('{}>0 and {}>0 :{}'.format(a,b,a>0 and b>0))
# print('{}>0 or {}>0 :{}'.format(a,b,a>0 or b>0))
# print('not {} : {}'.format(a, not a))
# print('not {} : {}'.format(b, not b))

# # 조건연산자

a=10
b=20
result=(a-b) if(a>=b) else(b-a)
print('{}와{}의 차는 {}입니다.'.format(a,b,result))

# 응용예제

# #-----예제1-----
# # 임의의 두 자리 정수를 입력받아서 십의 자리와 일의 자리로 분리하여 출력하는 프로그램 구현

# a=int(input('두 자리 정수를 입력해주세요 >>>'))
# print(type(a))
# print('십의 자리 : {}'.format(a//10))
# print('일의 자리 : {}'.format(a%10))

# # #-----예제2-----
# # 1분은 60초이고, 1시간은 60분이다. 1시간은 3600초이다. 임의의 초를 입력받아 해당 초를 시, 분, 초로 변환하는 프로그램 구현

# time=int(input('초를 입력하세요 >>>'))
# hour=int(time/3600)
# minute=int((time/60)-(hour*60)) # 1시간일때 -60 2시간일때 -120 ...... 
# second=time%60
# print(type(hour))
# print(type(minute))
# print(type(second))
# print('변환 결과는 {0}시간 {1}분 {2}초 입니다.'.format(hour,minute,second))


# #-----예제3-----
# 네 자리 정수로 구성된 사원번호를 기준으로 근무 시간을 결정하려한다. 사원번호의 끝자리 숫자가 5 이상이면 '오전' 아니면 '오후'를 출력하는 프로그램 구현

number=int(input('사원번호를 입력하세요 >>>'))
work=(number%10)
part=True if(work>=5) else(False)
work_time={True : '오전', False : '오후'}
print('근무 시간은 {0}입니다.'.format(work_time[part])) 

# 자료형의 형식을 주의할 것!! 




