#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


def main():
    import sys
    import os
    a = sys.path
    #b = os.system('python --version')
    b = os.popen('python --help').read()
    #print(a)
    print(b, end='\n')

if __name__ == '__main__':
    main()