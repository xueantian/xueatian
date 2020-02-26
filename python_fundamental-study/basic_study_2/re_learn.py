#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


def main():
    import re
    import hashlib
    hashlib.__get_builtin_constructor()
    get_md

    test = input('please input a Chinese mobile number: ')

    result = re.match(r'\+86\s\d{11}$', test)
    if result:
        print('Input is fine')
    else:
        print('Input error, please try again!')






if __name__ == '__main__':

    n = 1
    while n < 5:
        main()
        n +=1