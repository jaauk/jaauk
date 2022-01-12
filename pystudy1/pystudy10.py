# 기타제어문
# break문
# break가 포함된 반복문에서 종료

# n=1
# while True: #무한루프
#     print(n)
#     if n ==10:
#         break
#     n+=1
    
# 기본예제

# while True: # 무한루프 구성
#     city = input('서울의 수도는?')
#     if city == '서울' or city == 'seoul' or city == 'SEOUL':
#         print('정답입니다.')
#         break # 정답일 때 반복 종료
#     else:
#         print('오답입니다. 다시 시도하세요.') # 오답일 떄 반복

# # 기본예제 2

# hobbies = []
# while True: # 무한루프 구성
#     hobby = input('취미 입력')
#     if hobby == '': # 아무것도 입력안했을 때 종료
#         print('입력된 취미가 모두 저장되었습니다.')
#         break
#     else: # 입력했을 때 hobby에 추가
#         hobbies.append(hobby)
# print(hobbies)



# continue문
# 특정 조건을 만족하는 경우 실행에서 제외하고 싶을 때 사용한다.
# while의 경우 조건의 결과가 True이면 처음부터
# for문의 경우 반복객체로 이동하여 꺼낼 요소가 남아 있으면 for문 실행

# # 3의 배수를 제외한 모든 값의 합
# total = 0
# for a in range(1.101):
#     if a % 3 == 0:
#         continue # 3의 배수일 경우 다시 돌아감
#     total += a # 3의 배수가아닐 경우 합산
# print(total)

# # 기본예제
# # 과일 이름을 입력받아 리스트에 보관
# # 중복된 과일은 저장할 수 없고, 중복된 과일을 입력하면 다른 과일을 입력받는다.

# fruits =['사과','감귤'] 
# count = 3 # 입력남은 횟수

# while count > 0: # 입력횟수 0이되면 종료
#     fruit = input('과일이름 입력')
#     if fruit in fruits:
#         print('동일한 과일이 있다.')
#         continue # 중복된 경우 다시 입력받으러 돌아감.
#     fruits.append(fruit)
#     count -=1 # 남은입력횟수 (중복되지 않은 과일을 입력했을 때 실행됨)
#     print('입력이 {}남았습니다.'.format(count))
# print('과일은 {}입니다.'.format(fruits))

# # 기본예제 2
# # 5개의 정수를 입력받아 그 합계를 구함. 음수를 입력할 경우 재입력 받음

# count = 0
# total = 0
# while count < 5: # 0일때 1번 ... 4일때 5번째 입력
#     n = int(input('{}번째 양의 정수를 입력하세요 >>>'.format(count)))
#     if n <= 0: # 음수 입력불가.
#         print('0 이하의 정수는 처리할 수 없습니다. 재입력 하세요 >>>')
#         continue # 다시돌아감
#     total += n
#     count += 1
# print('입력된 5개의 양수의 합은{}입니다.'.format(total))

# #-----예제1-----

# money = int(10000)

# while money > 0:
#     pay = int(input('사용할 금액 입력>>>'))
#     if money < pay:
#         print('{}원 부족합니다.'.format(pay-money))
#         continue
#     money = money - pay
#     print('남은 돈은 {}원 입니다.'.format(money))
#     if pay < 0:
#         print('0 이하의 금액은 사용할 수 없습니다.')
#         continue

# #-----예제2-----
# p = '★  '
# # print(p*5)
# while True:
#     pp = int(input('영화의 평점을 입력하세요 >>>'))
#     if pp < 0 :
#         print('평점은 1~5 사이만 입력가능합니다.')
#         continue
#     elif pp > 5 :
#         print('평점은 1~5 사이만 입력가능합니다.')
#         continue
#     break
# print(p*pp)

# #-----예제3-----
# # 저장된 비밀번호는 qwerty이며 최대 5번 시도할 수 있음.

# password='qwerty'
# count = 5
# while count > 0:
#     input_password=str(input('비밀번호를 입력하세요 >>>'))
#     if input_password != password:
#         count -=1
#         continue
#     elif input_password == password:
#         print('비밀번호를 맞혔습니다.')
#         break
# if count == 0:
#     print('비밀번호 입력 횟수를 초과했습니다.')

#-----예제4-----
# 짝수인 단 (2,4,6,8)단은 출력하지 말고 blank line만 추가
# 각 단까지만 출력하세요. 3단이면 3*3까지 5단이면 5*5까지

dan=1
n=1

while dan<=9:
    if dan % 2 == 0:
        print('\n')
        dan+=1
        continue    
    elif dan % 2 != 0:
        print(f'{dan}*{n}={dan*n}')
        n+=1
        if dan < n:
            dan+=1
            n=1
        continue
    break














