class Temp:
    # 인스턴스가 메모리에서 소멸될 때 호출되는 함수 - 소멸자
    def __del__(self):
        print("Temp 클래스의 인스턴스가 파괴됩니다.")


obj = Temp()  # 인스턴스가 생성 - reference count 가 1

# obj1 = obj  # 인스턴스를 다른 변수가 가리키도록 하는 것
# reference count 가 1증가합니다.

obj = 1
# 이전에 만들어진 인스턴스 대신에 새로 만들어진 인스턴스를 가리킵니다.
# 이전에 만들어진 인스턴스의 reference count는 1 감소

obj = Temp()  # 참조 횟수가 1이 됩니다.
obj1 = obj  # 참조를 복사했으므로 참조 횟수가 2가 됩니다.
obj = Temp()  # 다른 인스턴스를 참조했으므로 참조 횟수가 1 줄어서 1이 됩니다.

import weakref

obj = Temp()  # 참조 횟수가 1이 됩니다.
obj1 = weakref.ref(obj)  # 참조 횟수를 변경시키지 않고 참조를 복사
obj = Temp()  # 다른 인스턴스를 참조했으므로 참조 횟수가 1 줄어서 1이 됩니다.
