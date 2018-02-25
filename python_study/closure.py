
# 파이썬 - 클로저 (Closure)
# http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%B4%EB%A1%9C%EC%A0%80-closure/

# def outer_func(tag):  #1
#     text = 'Some text'  #5
#     # tag = tag  #6
#
#     def inner_func():  #7
#         print('<{0}>{1}<{0}>'.format(tag, text))  #9
#
#     return inner_func  #8
#
#
# h1_func = outer_func('h1')  #2
# p_func = outer_func('p')  #3
#
#
# h1_func()  #4
# p_func()  #10



def outer_func(tag):  #1
    # tag = tag  #5
    # 이 코드가 없어도 outer_func에 전달된 인자 tag가
    # 아래 inner_func의 지역변수에 할당되는 것을 확인함.

    def inner_func(txt):  #6
        text = txt  #8
        print('<{0}>{1}<{0}>'.format(tag, text))  #9

    return inner_func  #7


h1_func = outer_func('h1')  #2
p_func = outer_func('p')  #3


h1_func('h1태그의 안입니다.')  #4
p_func('p태그의 안입니다.')  #10
