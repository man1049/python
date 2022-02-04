# fractions 모듈의 모든 내용을 fractions라는 이름으로 묶어서 가져오기
# import fractions

# fractions 모듈의 Fraction을 현재 모듈에 포함시켜서 가져오기ㅣ - fractions
# fractions를 제외하고 사용해도 됨
from fractions import Fraction

result = Fraction(5, 7) + Fraction('5/7')
print(result)
