###################################################
## Challenge day 1
## Lecture 1.3 ~ 1.7
## about : functions
###################################################

# python은 indentation(들여쓰기)로 function의 시작과 끝 판단
# 다른 언어처럼 {}로 구분하지 x

# 사용자 정의 함수
# def say_hello():
# print("hello")
# print("bye")

# say_hello()

def say_hello(name="anonymous"):
  print("hello", name)

say_hello()

def plus(a,b):
  print(a+b)    #5 출력

def p_plus(a,b):
  return a+b
  print("이것도 리턴을 할 것인가 - 안할 걸", True)

result = plus(2,3)
p_result = p_plus(2,3)

print(result, p_result) #None 5
# plus 함수는 정의 부분엥서 아무것도 return 하지 않기 때문에 None 출력
# p_plus 함수는 return 을 포함하고 있기 때문에, 2와 3이 대입된 값을 연산하여 5 출력

# return 은 function을 종료함 =>
# python에서는 뭔가를 return 하는 순간, 해당 function을 종료함.
# 한번에 하나의 값만 return 할 수 있음
# 하나의 function안에서 2개의 값을 두 번에 나눠서 return 하거나 할 수 없음. 한번에 한 개만 반환.

# 따라서
# p_plus 함수의 return 아래에 정의된 print 함수는 실행되지 않음

######################################
# Python의 함수매개 인자 방식 >>
# 위치 인자(positional argument)와 키워드 인자(keywords argument)를 지원
# Positional Argument : 위치에 의존적인 인자.
# Keywords Argument : argument의 이름으로 쌍을 이뤄줌 (위치 관계 x)

def say_hello(name, age):
  return f"Hello {name} you are {age} years old"
# return "Hello " + name + "You are " + age + "years old"  와 동일

print_hello = say_hello(age="11", name="helen") #keywords argument
#print_hello = say_hello("helen","11") #positional argument
print(print_hello)