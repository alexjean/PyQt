# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 下午 9:26
# @Author  : AlexJean

def fibonacci(n):
    a,b ,counter=0,1,0
    while True:
        if counter > n:
            return
        yield a
        a,b=b,a+b
        counter+=1

fib = fibonacci(10)
print(type(fib))
print([x for x in fib])
