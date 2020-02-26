#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


def main():
    import os
    f = open('123.txt','w')
    f.write('good days\n')
    f.write('hello Amy')
    f.close()

def main1():
    with open('123.txt','r') as f:
        s = f.read()
        print(s)


if __name__ == '__main__':
    main1()