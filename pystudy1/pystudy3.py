# 표준출력

# 이스케이프 문자
# 출력시 나타내는 문자 ', ", tab, 수직tab, 역슬래시\ 등

# print('Hello \'World\'') # 작은따옴표 \'
# print('Hello \"World\"') # 큰따옴표 \"
# print('1\n22\n33') # 줄바꿈 \n
# print('이름\t연락처') # \t tab
# print('제시카\t02-123-4567')
# print('마틴\t010-8382-0293')

# print함수
# print(value,sep=' ', end=\n, file=sys.stdout, flush=False)

# print('funny','Python')
# print('Python','Java','C',sep=',') #sep 구분기호

# print() # 공백

# print('movie tatanic')
# print('point', end=':')
# print('5') # 윗줄 구분기호 뒤로 이어서 출력

# # 맞춤 출력하기
# print('%5d' % 1) # 1을 5자리로 오른쪽 맞춤 출력
# print('%6d' % 2) # 2를 6자리로 오른쪽 맞춤 출력

# print('%-5d' % 2) # 2를 5자리로 왼쪽 맞춤 출력

# # 소수점 출력하기
# print('%5.2f' % 3.66) # 전체 5자리로 소수 2자리까지 오른쪽 맞춤 출력

# print('%.2f' % 3.222) # 소수 2자리까지 출력

# # 기본예제 %s 사용하기

# name = 'jaeuk'
# print('내 이름은 %s입니다.' %name)
# height=174.5
# print('내 키는 %.1fcm 입니다' %height) # 소수점 자리 지정
# weight=76.75
# print('내 몸무게는 %.2fkg입니다' %weight) # 소수점 자리 지정
# year,month,day=1994,7,20
# print('내 생일은 %d년 %d월 %d일 입니다' %(year,month,day)) # 형식 기호가 2개 이상이면 %뒤에 괄호를 추가해야함!

# format() 메소드

# 예시

# print('My name is {}'.format('Jaeuk'))
# # print('My name is {0}'.format('Jaeuk')) # 0입력시에도 같은 값 [인덱스넘버]

# 'My name is {name}'.format (name='Jae uk') # 표시할 변수명을 지정할 수 있음
# # 이런 경우 반드시 메소드에 '변수명=값' 으로 지정해줘야 함

# # 기본예제

# zipcode='06236'
# print('우편번호 : {}'.format(zipcode))

# address='''서울특별시 강남구 테헤란로 146'''

# print('주소 : {addr}'.format(addr=address))

# tel1,tel2,tel3='02','3023','2934'
# print('연락처 : {0}-{1}-{2}'.format(tel1,tel2,tel3))

# # f-string

# who='you'
# how='happy'
# f'{who} make me {how}'

# input()
# 사용자의 입력을 처리하는 함수.

# n = input('숫자를 입력하세요')
# 사용자입력 : 20
# print(n)
# 20

# name=input('이름을 입력하세요 : ')
# age=input('나이를 입력하세요 : ')

# print('이름은 {} 입니다.'.format(name)) # format
# print('나이는 {} 입니다.'.format(age))

# print(f'이름은 {name} 입니다.') # f-string
# print(f'나이는 {age} 입니다.')

