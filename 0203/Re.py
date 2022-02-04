#re - 정규식 모듈
import re

match = re.match('[0-9]', '1234')
print(match)

match = re.match('[0-9]', '가나다라')
print(match)

# 정규식 객체 생성
p = re.compile('the')
print(p.findall('The Hell in the Cat'))

# 대소문자 구분하지 않고 검색
p = re.compile('the', re.I)
print(p.findall('The Hell in the Cat'))

# 주민등록번호 패턴 검사
p = re.compile("(\d{6})-?(\d{7})")
num = '123456-1234567'

if p.search(num) != None:
    print("올바른 주민등록번호 형식입니다.")
else:
    print("아닙니다.")

# 불용어 제거
result = re.sub("-", "", num)
print(result)

