#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com

'%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。'

'%d	整数'
'%f	浮点数'
'%s	字符串'
'%x	十六进制整数'


def main():
    score1 = 72
    score2 = 85
    rate1 = (85-72)/72
    print('%.1d%.1f%%' % (rate1,rate1))

if __name__ == '__main__':
    main()