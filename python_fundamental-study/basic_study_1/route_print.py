#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com


def main():
    import os
    import re
    route_n_result = os.popen('netstat -nr').read()
    #print(route_n_result)
    route_n_resultlist = route_n_result.split('      ')
    #route_n_resultlist = route_n_result[8:-8]
    #print(route_n_resultlist)
    #print(route_n_resultlist)
    for x in route_n_resultlist:
        if x.split() == 'UGSc':
            print(x, end='')
       # else:
        #   print('no gateway')


if __name__ == '__main__':
    main()