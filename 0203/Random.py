# 랜덤 모듈 - 샘플링이나 게임에 많이 사용
import random

# seed 고정 - 정해진 숫자가 순서대로 리턴
random.seed(42)

print(random.random())
print(random.randint(1, 100))

li = ["김백산", "태백산", "소백산"]
print(random.sample(li, 3))  # 비복원 추출 - 동일한 데이터가 추출되지 않음
for i in range(0,4,1):
    print(random.choice(li))  # 복원 추출 - 동일한 데이터가 추출될 수 있음

print(li)
random.shuffle(li)
print(li)
