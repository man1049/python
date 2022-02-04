# 파일 시스템 정보를 위한 모듈
import os.path
import time

print("최종 수정 시간 : ", os.path.getmtime('C:\\Users\\Jeon\\Desktop\\openvr_api.dll'))
print("최종 수정 시간 : ", time.gmtime(os.path.getmtime('C:\\Users\\Jeon\\Desktop\\openvr_api.dll')))
