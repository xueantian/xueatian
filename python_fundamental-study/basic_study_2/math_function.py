#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com

#定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解

#

def quadratic(a,b,c):
    import math
    sqrt = b**2-4*a*c

    if sqrt < 0:
        print('Error with no result')
        x1 = x2 = 0
        return x1,x2
    elif sqrt == 0:
        print('there is only one value for X')
        sqrt_result = math.sqrt(sqrt)
        x1 =(0 - b + sqrt_result)/(2*a)
        x2 = x1
        return x1, x2
    else:
        print('there are two values for X')
        sqrt_result = math.sqrt(sqrt)
        x1 = (0 - b + sqrt_result)/(2*a)
        x2 = (0 - b - sqrt_result)/(2*a)
        return x1, x2

def main1():

    e = float(input('what is a?'))
    if e <0:
        print('a can not low than zero')
        return
    else:
        pass
    f = float(input('what is b?'))
    g = float(input('what is c?'))
    x1,x2 = quadratic(e,f,g)

    if x1 == 0:
        print('there is no result for that, try again!')
    else:
        print('Good job!\n\n''X1=','%.1f' % x1, '\t','X2=','%.1f' % x2)

    print('_'*38,'\n','\n')

def main():
    n = 1
    while n < 4:
        main1()
        n+=1



if __name__ == '__main__':
    main()