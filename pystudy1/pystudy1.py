# print("Hello Python")

# Mutable 과 Immutable
# Mutable 생성 후 변경이 가능한 자료형 (list, set, dict)
# Immutable 생성 후 변경이 불가능한 자료형 (int, float, str, tuple)

# me = [1,2,3]
# print(id(me))

# print(me)

# me.append(4)

# print(me)
# print(id(me))
# list는 1,2,3,4 로 수정이 되지만 id(주소)는 동일하다.
# 즉 동일주소에 값을 수정&변경가능하다

me = 10
id(me)

print(me)
print(id(me))
print(id)

me += 1
id(me)

print(me)
print(id(me))

# 값이 수정되면서 주소도 재지정된다.
# 즉 동일주소에 값을 변경이 불가능하다.
