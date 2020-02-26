#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


def main():
    L = list(range(10))
    print(L)
    L1 = L[:3]
    L2 = L[-3:]
    print(L1)
    print(L2)

    T = tuple(range(10,20))
    print(T)
    T1 = T[-4:]
    print(T1)

def trim():
    s1 = str(input('input a string'))
    len1 = len(s1)
    n = 1


    if s1[0] ==' ':
        s = s1[n:len1]

    elif s1[len1-1] ==' ':
        s = s1[0:len1-n]
    else:
        s = s1

    return s

def trim1():
    s = input('input?')
    while s!='' and s[0] ==' ':
       s = s[1:]
       print(s)
    while s!='' and s[-1] == ' ':
        s = s[:-1]
        print(s)

    return s


if __name__ == '__main__':
    #trim1()
    print(trim1())