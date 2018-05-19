# 파이썬 - 데코레이터 (Decorator)
# http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0-decorator/

# 1) 함수 형식의 데코레이터
#   - 인수를 가진 함수를 데코레이팅할 경우
#
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):  #1
#         print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
#         return original_function(*args, **kwargs)  #2
#     return wrapper_function
#
#
# @decorator_function
# def display():
#     print('display 함수가 실행됐습니다.')
#
#
# @decorator_function
# def display_info(name, age):
#     print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))
#
# display()
# print()
# display_info('John', 25)




# 2) 클래스형식의 데코레이터
#   - __init__ 메소드가 전달된 '함수' 인자를 받고,
#     __call__ 메소드가 wrapper_function 역할을 하는 것.
#     (__call__ : 클래스의 객체가 함수처럼 호출되면 실행되는 함수이다.)

class DecoratorClass:  #1
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('{} 함수가 호출되기전 입니다.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

    def test(self):
        print('테스트')

    name = '이름'


# @DecoratorClass  #2
def display():
    print('display 함수가 실행됐습니다.')


# @DecoratorClass  #3
def display_info(name, age):
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))



display = DecoratorClass(display)
display_info = DecoratorClass(display_info)


#######################
display()
print()
display_info('John', 25)

display.test()
#######################

# __call__ 함수를 통해서 함수를 리턴하면
# 그 값을 받은 변수는 '인스턴스' 이면서 동시에 '함수'가 되는
# 기괴한 현상이...



print(display.name)
print(DecoratorClass.name)
