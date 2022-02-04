import copy

# scala 데이터 참조
a = 1
print(id(a))
a = 2
print(id(a))

# a에 저장된 데이터가 다르므로 다른 id

b = 1
print(id(b))

a = 10
b = a  # 10이 저장된 곳의 id를 복사
a = 20  # a 의 id가 변경됨
print(a)
print(b)  # b를 가지고 값을 변경한 적이 없으므로 이전 값 그대로

ar = [100, 200, 300]
br = ar

# 세부 데이터를 변경했으므로 br에 영향을 줌
ar[0] = 300
print(ar)
print(br)

# ar의 참조 자체가 변경 된 것이므로 이제는 ar과 br은 아무 상관없음
ar = [300, 200, 100]
ar[0] = 700
print(ar)
print(br)

print("==================================")

# copy 모듈

aar = [100, 200, 300]
# 얕은 복제를 이용 - 새로운 곳에 복사를 해서 그 곳의 id를 리턴
bbr = copy.copy(aar)

print(aar)
print(bbr)

# 새로 복제를 했기 떄문에 aar을 변경시켜도 bbr에는 영향이 없음
aar[0] = 700
print(aar)
print(bbr)

print("==================================")

aar = [[1000,2000,3000], [4000, 5000, 6000]]
# list안에 다른 list가 존재하는 경우는 copy로 복제를 해도
# 내부 데이터를 변경하면 복제된 데이터에 영향을 줌
bbr = copy.copy(aar)
print(aar)
print(bbr)

aar[0][0] = 12345
print(aar)
print(bbr)
print("==============================")
aar = [[1000,2000,3000], [4000, 5000, 6000]]
# list안에 다른 list가 존재하는 경우는 deepcopy로 복제를 하면
# 재귀적으로 복제를 하므로 이런 현상이 없어짐
bbr = copy.deepcopy(aar)
print(aar)
print(bbr)

aar[0][0] = 12345
print(aar)
print(bbr)
print("==============================")
