#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


def main1():
    import module1_print
    module1_print.main('hello world')

def main2():
    from module1_print import main
    main('good day')


if __name__ == '__main__':
    main2()