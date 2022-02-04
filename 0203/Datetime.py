# datetime 모듈

import datetime

# 현재 시간을 가지고 생성
dt = datetime.datetime.now()
print(dt)
# 날짜
print(dt.date())
# 시간
print(dt.time())

# 년도만 추출
print(dt.date().year)
# 시간만 추출
print(dt.time().hour)

# 문자열로 변환
s = dt.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')
print(s)

# 문자열을 가지고 datetime 만들기
dt1 = datetime.datetime.strftime(dt, "%Y-%m-%d %H:%M")
print(dt1)

# 날짜와 날짜 차이

dt1 = datetime.datetime.now()
dt2 = datetime.datetime(1993, 4, 21, 12)

td = dt1 - dt2
print(td)
print(td.days, " 일이 지남")
