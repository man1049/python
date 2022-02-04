import os
import sys

# 처음 다른 곳에서 파이썬을 실행 할 때 가장 먼저 확인하는 정보

print(os.getcwd())  # 현재 작업 디렉토리 확인
print(sys.getdefaultencoding())  # 현재 인코딩 방식
print(sys.path)  # 현재 참조하는 모듈의 순서
