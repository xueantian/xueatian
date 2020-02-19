#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


def main():

    T = ('a','v','b','c','d')
    d = list(T)
    d.sort()
    T = tuple(d)
    e = sorted(T)
    T1 = tuple(e)

    print(d)
    print (T)
    print(T1)



if __name__ == '__main__':
    main()