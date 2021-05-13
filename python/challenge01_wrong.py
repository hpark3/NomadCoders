## 7가지 연산자 이용하여 계산기 만들기
# plus, minus, times, division, negation(역수), power(제곱), remainder
# (추가) user가 다른 타입끼리 연산 시도 시, 예외 처리 어떻게 할 지
# 참고하기 : bulit-in function 이용해서 다른 type으로 변환
#
# 개인 참고자료 : https://redmuffler.tistory.com/428

def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def rem(a, b):
    return a % b


def power(a, b):
    return a ** b


def neg(a):
    return -a


print('-' * 30)
print("MENU")
print('-' * 30)
print("1.plus\n2.minus\n3.multiply\n4.divide\n5.remainder\n6.exponent\n7.negate\n8.exit")
print('-' * 30)

while True:
    # 예외처리 참고자료
    # https://withcoding.com/85
    # https://wayhome25.github.io/python/2017/02/26/py-12-exception/
    # https://mungto.tistory.com/97
    try:
        menu = int(input("select a number on the menu: "))
    except ValueError:
        print('{}는 숫자가 아닙니다.'.format(input()))  # 에러 발생 시 처리할 코드

    # else 대신 finally 를 사용하면 메뉴 선택 하지 않고도 프로그램이 계속 실행되기 때문에
    # 여기서는 else 가 적절
    else:
        # 논리 연산자
        # https://wikidocs.net/20699
        try:
            if (menu > 0 and menu < 7):
                a = int(input("1st number: "))
                b = int(input("2nd number: "))
                if (menu == 1):
                    result = sum(a, b)
                    print("%d, %d를 계산한 결과는 %d입니다." % (a, b, result))
                elif (menu == 2):
                    result = sub(a, b)
                    print("%d, %d를 계산한 결과는 %d입니다." % (a, b, result))
                elif (menu == 3):
                    result = mul(a, b)
                    print("%d, %d를 계산한 결과는 %d입니다." % (a, b, result))
                elif (menu == 4):
                    result = div(a, b)
                    print("%d, %d를 계산한 결과는 %d입니다." % (a, b, result))
                elif (menu == 5):
                    result = rem(a, b)
                    print("%d, %d를 계산한 결과는 %d입니다." % (a, b, result))
                elif (menu == 6):
                    result = power(a, b)
                    print("%d, %d를 계산한 결과는 %d입니다." % (a, b, result))
            elif (menu == 7):
                a = int(input("number: "))
                result = neg(a)
                print("%d의 역수는 %d입니다." % (a, result))
            elif (menu == 8):
                print("종료합니다")
                break
            else:
                print("잘못입력했습니다. 다시 입력해주세요.")
        except:
            # format 함수 사용 포맷팅 : 2개 이상의 값 넣기
            # https://wikidocs.net/13
            print('{}와 {}는 자료형이 달라서 계산 불가.'.format(input(), input()))
