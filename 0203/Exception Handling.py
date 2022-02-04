# 예외가 발생하는 상황
def ten_div(x):
    return 10 / x


# 기본적인 예외 처리 구문을 이용해서 예외가 발생하더라도 중지되지 않도록 함
try:
    print(ten_div(2))
    print(ten_div(0))  # 예외가 발생해서 프로그램이 중단

except ZeroDivisionError as 예외별명:
    print('예외 발생')

finally:
    print('프로그램 종료')


# 예외강제 발생
def ten_div(x):
    if x > 10:
        # 강제로 예외를 발생시켜서 아래 문장을 수행하지 않음
        raise Exception("숫자가 너무 큽니다.")
    return 10 / x


# raise
# 기본적인 예외 처리 구문을 이용해서 예외가 발생하더라도 중지되지 않도록 함
try:
    print(ten_div(2))
    print(ten_div(15))  # 예외가 발생해서 프로그램이 중단

except ZeroDivisionError as 예외별명:
    print('예외 발생')

finally:
    print('프로그램 종료')

# assert
# 특정 조건을 만족하지 못하는 경우 예외를 발생시켜 프로그램 중단하기
score = 101
assert score <= 100, "score는 100이 넘을 수 없습니다"
print(score)
