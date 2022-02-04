# time 모듈
import time

print(time.time())  # foloat 으로 현재 시간 리턴
print(time.localtime())  # struct_time 형식으로 현재 시간 리턴

time.sleep(2)  # 2초 대기

print(time.time())