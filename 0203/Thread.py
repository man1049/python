# 콜백 함수 지정을 이용한 스레드 생성 및 시작
import threading, time

"""
def threadEx(id):
    for i in range(0, 10, 1):
        print('id={0}--->{1}'.format(id, i))
        time.sleep(1)


for i in range(2):
    targ = "{0}번 스레드".format(i)
    th = threading.Thread(target=threadEx, args=(arg, ))
    th.start()
"""


# 상속을 이용한 스레드 생성 및 시작
class ThreadEx(threading.Thread):
    def run(self):
        for i in range(0, 10, 1):
            print('id={0}--->{1}'.format(self.getName(), i))
            time.sleep(1)


for i in range(2):
    th = ThreadEx()
    th.start()
