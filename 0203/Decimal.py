# 실수 표현을 정확하게 해주는 모듈
from decimal import Decimal

result = 0.0
for i in range(0, 100, 1):
    result = result + 1.0

print(result)  # 10.0이 아님

# Decimal로 변환해서 실행
k = Decimal("0.0")
for i in range(0, 100, 1):
    k = k + Decimal("0.1")

print(k)

print((1.0 - 0.8) == 0.2)
# compare는 호출하는 데이터가 크면 양수:1 , 같으면:0 , 작으면 음수:-1
print((Decimal('1.0') - Decimal('0.8')).compare(Decimal('0.2')))
