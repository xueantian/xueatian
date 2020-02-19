#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com

a = [1,2,3,4,'q','a','q']
b = len(a)
c = [4,5,6,7]
#d = a + c
matrix = [[1,2,3],['a','b','c'],[4,5,6]]
e = matrix[2][0]
#d = a.insert(0,'aaaaaaa')
#d = a.remove(4)
#d = c.reverse()
#d = c
d = set(a) # set to reduce the repeat items


def main():



    for x in a:
        print(x)

    print(e)
    print(d)



__name__ == '__main__'


main()