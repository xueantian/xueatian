#!/usr/bin/env python3.7
# -*- coding=utf-8 -*-
# for self-exercise 
# email:xueatian@cisco.com

def write():
    myfile = open('123.txt', 'w')
    myfile.writable()
    myfile.write('happy new year\n')
    myfile.write('hello to my world\t\n')
    myfile.write('good to see you\n')
    myfile.close()

def standard_read():
    myfile = open('123.txt','r')
    print(myfile.read())
    #print(myfile.readline())

def for_read():
    for line1 in open('123.txt'):
        print(line1)

def main():
    write()
    #read()
    for_read()





if __name__ == '__main__':
    main()