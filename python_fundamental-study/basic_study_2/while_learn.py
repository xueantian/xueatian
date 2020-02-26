#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


def main():
    n = 100
    while n>=1:
        if n <=30:
            break
        else:
            print(n)
        n -=2
    print('END')

def main1():
    n = 100
    while n >= 1:
        n -= 10
        if n == 60:
            continue
        elif n == 30:
            break

        print(n)

    print('END')

if __name__ == '__main__':
    main1()